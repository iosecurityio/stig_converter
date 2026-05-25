"""
stig_converter.py
Converts DISA STIG checklists between various file formats (CKL, CSV, JSON, Markdown)
and can fetch the latest STIG data from remote sources.

Usage:
    stig_converter convert -i checklist.ckl -o report.csv
    stig_converter convert -i checklist.ckl -o findings.json
    stig_converter convert -i findings.json -o checklist.ckl --template-ckl template.ckl
    stig_converter convert -i findings.json -o report.md
    stig_converter fetch --json output.json
    stig_converter fetch --zip output.zip [--stig-sys ASD] [--stig-ver V6R4]
    python -m stig_converter convert -i checklist.ckl -o report.csv
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

__version__ = "2.4"

_SUPPORTED_CONVERSIONS = {
    "ckl": ["csv", "json", "md"],
    "csv": ["json"],
    "json": ["ckl", "md"],
}


class ValidationError(Exception):
    """Raised when input/output path or conversion validation fails."""
    pass


def validate_file_conversion(input_path: Path, output_path: Path) -> None:
    """
    Validates that the conversion is supported and the paths are valid.

    :raises ValidationError: on any failure
    """
    if input_path.resolve() == output_path.resolve():
        raise ValidationError(
            f"Input and output files cannot be the same: {input_path}"
        )

    input_ext = input_path.suffix[1:].lower()
    output_ext = output_path.suffix[1:].lower()

    if input_ext not in _SUPPORTED_CONVERSIONS:
        valid = ", ".join(_SUPPORTED_CONVERSIONS)
        raise ValidationError(
            f"Unsupported input type '{input_ext}'. Supported: {valid}"
        )
    if output_ext not in _SUPPORTED_CONVERSIONS[input_ext]:
        valid = ", ".join(_SUPPORTED_CONVERSIONS[input_ext])
        raise ValidationError(
            f"Cannot convert '{input_ext}' → '{output_ext}'. Valid outputs: {valid}"
        )

    if not input_path.is_file():
        raise ValidationError(f"Input file does not exist: {input_path}")

    output_path.parent.mkdir(parents=True, exist_ok=True)


class STIGConverter:
    """Converts STIG Checklists to/from various file formats (CSV, JSON, CKL, Markdown)."""

    def __init__(self, args: argparse.Namespace) -> None:
        self.input_file_path: Path = args.input
        self.output_file_path: Path = args.output
        self.project_name: Optional[str] = getattr(args, "name", None)
        self.template_ckl: Optional[Path] = getattr(args, "template_ckl", None)
        self.date: str = datetime.now().strftime("%Y%m%d")

    def update_filename(self, filename: str) -> str:
        """
        Update or append a YYYYMMDD datestamp in a filename.

        Examples:
            stig_checklist-20210723.ckl  →  stig_checklist-<today>.ckl
            stig_checklist.ckl           →  stig_checklist-<today>.ckl
        """
        match = re.search(r"-(\d{8})", filename)
        if match:
            return filename.replace(match.group(1), self.date)
        p = Path(filename)
        return str(p.with_name(f"{p.stem}-{self.date}{p.suffix}"))

    def convert(self) -> str:
        """Dispatch conversion based on input/output file extensions."""
        input_ext = self.input_file_path.suffix[1:].lower()
        output_ext = self.output_file_path.suffix[1:].lower()

        if input_ext == "ckl" and output_ext == "csv":
            return self._ckl_to_csv()
        if input_ext == "ckl" and output_ext == "json":
            return self._ckl_to_json()
        if input_ext == "ckl" and output_ext == "md":
            return self._ckl_to_md()
        if input_ext == "csv" and output_ext == "json":
            return self._csv_to_json()
        if input_ext == "json" and output_ext == "ckl":
            return self._json_to_ckl()
        if input_ext == "json" and output_ext == "md":
            return self._json_to_md()

        raise ValidationError(
            f"Unsupported conversion: {input_ext} → {output_ext}"
        )

    # ------------------------------------------------------------------
    # Private conversion methods
    # ------------------------------------------------------------------

    def _ckl_to_csv(self) -> str:
        from stig_converter.converters.ckl_to_csv import convert_ckl_to_csv
        return convert_ckl_to_csv(self.input_file_path, self.output_file_path)

    def _ckl_to_json(self) -> str:
        from stig_converter.converters.ckl_to_json import convert_ckl_to_json
        return convert_ckl_to_json(self.input_file_path, self.output_file_path)

    def _csv_to_json(self) -> str:
        from stig_converter.converters.csv_to_json import convert_csv_to_json
        return convert_csv_to_json(self.input_file_path, self.output_file_path)

    def _json_to_ckl(self) -> str:
        if not self.template_ckl:
            raise ValidationError("--template-ckl is required for JSON → CKL conversion")
        from stig_converter.converters.json_to_ckl import convert_json_to_ckl
        return convert_json_to_ckl(
            self.input_file_path, self.output_file_path, self.template_ckl
        )

    def _json_to_md(self) -> str:
        from stig_converter.converters.json_to_markdown import convert_json_to_md
        return convert_json_to_md(self.input_file_path, self.output_file_path)

    def _ckl_to_md(self) -> str:
        from stig_converter.converters.ckl_to_markdown import convert_ckl_to_md
        return convert_ckl_to_md(self.input_file_path, self.output_file_path)


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stig_converter",
        description=(
            "Work with DISA STIG checklists: convert between formats or fetch the latest data.\n\n"
            "Subcommands:\n"
            "  convert  Convert a checklist between CKL, CSV, JSON, and Markdown\n"
            "  fetch    Download the latest STIG data from remote sources"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")
    subparsers.required = True

    # -- convert subcommand ------------------------------------------------
    convert_parser = subparsers.add_parser(
        "convert",
        help="convert a checklist between file formats",
        description=(
            "Convert DISA STIG checklists between CKL, CSV, JSON, and Markdown formats.\n\n"
            "Supported conversions:\n"
            "  CKL  →  CSV, JSON, Markdown\n"
            "  CSV  →  JSON\n"
            "  JSON →  CKL, Markdown\n\n"
            "CKL is the XML-based checklist format used by DISA STIG Viewer.\n"
            "JSON → CKL requires a --template-ckl file."
        ),
        epilog=(
            "examples:\n"
            "  %(prog)s -i checklist.ckl -o report.csv\n"
            "  %(prog)s -i checklist.ckl -o findings.json\n"
            "  %(prog)s -i checklist.ckl -o report.md\n"
            "  %(prog)s -i findings.json -o checklist.ckl --template-ckl template.ckl\n"
            "  %(prog)s -i findings.json -o report.md\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    convert_parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        metavar="FILE",
        help="input file (.ckl, .csv, .json)",
    )
    convert_parser.add_argument(
        "-o", "--output",
        type=Path,
        required=True,
        metavar="FILE",
        help="output file (.csv, .json, .ckl, .md)",
    )
    convert_parser.add_argument(
        "-n", "--name",
        metavar="NAME",
        help="project name included in output where applicable",
    )
    convert_parser.add_argument(
        "--template-ckl",
        dest="template_ckl",
        type=Path,
        metavar="FILE",
        help="CKL template file (required for JSON → CKL)",
    )

    # -- fetch subcommand --------------------------------------------------
    fetch_parser = subparsers.add_parser(
        "fetch",
        help="download the latest STIG data from remote sources",
        description=(
            "Download the latest STIG data.\n\n"
            "  --json  Fetches the ASD STIG checklist from stigviewer.com as JSON.\n"
            "  --zip   Downloads the official STIG package from DISA Cyber Exchange as ZIP.\n\n"
            "Exactly one of --json or --zip must be provided."
        ),
        epilog=(
            "examples:\n"
            "  %(prog)s --json data/latest_stigs.json\n"
            "  %(prog)s --zip data/U_ASD_V6R4_STIG.zip\n"
            "  %(prog)s --zip data/U_ASD_V6R4_STIG.zip --stig-sys ASD --stig-ver V6R4\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    fetch_group = fetch_parser.add_mutually_exclusive_group(required=True)
    fetch_group.add_argument(
        "--json",
        dest="fetch_json",
        metavar="FILE",
        help="output path for the downloaded JSON file (from stigviewer.com)",
    )
    fetch_group.add_argument(
        "--zip",
        dest="fetch_zip",
        metavar="FILE",
        help="output path for the downloaded ZIP file (from DISA Cyber Exchange)",
    )
    fetch_parser.add_argument(
        "--stig-sys",
        dest="stig_sys",
        default="ASD",
        metavar="SYS",
        help="STIG system identifier for ZIP download (default: ASD)",
    )
    fetch_parser.add_argument(
        "--stig-ver",
        dest="stig_ver",
        default="V6R4",
        metavar="VER",
        help="STIG version for ZIP download (default: V6R4)",
    )

    return parser


def parse_args(args: Optional[list] = None) -> argparse.Namespace:
    parser = create_parser()
    parsed = parser.parse_args(args)
    if parsed.command == "convert":
        try:
            validate_file_conversion(parsed.input, parsed.output)
        except ValidationError as e:
            parser.error(str(e))
    return parsed


def main() -> None:
    """CLI entry point."""
    if len(sys.argv) == 1:
        create_parser().print_help()
        sys.exit(0)
    args = parse_args()
    try:
        if args.command == "convert":
            converter = STIGConverter(args)
            converter.convert()
        elif args.command == "fetch":
            from stig_converter.get_new_stigs import get_stig_json, get_stig_zip
            if args.fetch_json:
                get_stig_json(args.fetch_json)
            else:
                get_stig_zip(args.fetch_zip, stig_sys=args.stig_sys, stig_ver=args.stig_ver)
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user", file=sys.stderr)
        sys.exit(1)
    except ValidationError as e:
        print(f"[X] {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"[X] Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
