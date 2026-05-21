"""
stig_converter.py
Converts DISA STIG checklists between various file formats (CKL, CSV, JSON, Markdown).

Usage:
    stig_converter -i checklist.ckl -o report.csv
    stig_converter -i checklist.ckl -o findings.json
    stig_converter -i findings.json -o checklist.ckl --base-ckl template.ckl
    stig_converter -i findings.json -o report.md
    python -m stig_converter -i checklist.ckl -o report.csv
"""

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional

__version__ = "2.3"

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
        self.base_ckl: Optional[Path] = getattr(args, "base_ckl", None)
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
        if not self.base_ckl:
            raise ValidationError("--base-ckl is required for JSON → CKL conversion")
        from stig_converter.converters.json_to_ckl import convert_json_to_ckl
        return convert_json_to_ckl(
            self.input_file_path, self.output_file_path, self.base_ckl
        )

    def _json_to_md(self) -> str:
        from stig_converter.converters.json_to_markdown import (
            convert_checklist_to_md,
            write_stigs,
        )
        with open(self.input_file_path, encoding="utf-8") as f:
            data = json.load(f)
        if isinstance(data, list):
            # Checklist format produced by convert_ckl_to_json / convert_csv_to_json
            return convert_checklist_to_md(data, self.output_file_path)
        # Stigviewer format produced by get_stig_json
        return write_stigs(self.input_file_path, self.output_file_path)

    def _ckl_to_md(self) -> str:
        """Two-step CKL → JSON (temp file) → Markdown."""
        from stig_converter.converters.ckl_to_json import convert_ckl_to_json
        from stig_converter.converters.json_to_markdown import convert_checklist_to_md

        tmp_path = self.output_file_path.parent / f"_tmp_{self.date}.json"
        try:
            convert_ckl_to_json(self.input_file_path, tmp_path)
            with open(tmp_path, encoding="utf-8") as f:
                findings = json.load(f)
            return convert_checklist_to_md(findings, self.output_file_path)
        finally:
            if tmp_path.exists():
                tmp_path.unlink()


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="stig_converter",
        description=(
            "Convert DISA STIG checklists between file formats "
            "(CKL, CSV, JSON, Markdown). "
            "Output paths must be within the current working directory."
        ),
        epilog="""
examples:
  %(prog)s -i checklist.ckl -o data/report.csv
  %(prog)s -i checklist.ckl -o data/findings.json
  %(prog)s -i data/findings.json -o data/checklist.ckl --base-ckl data/template.ckl
  %(prog)s -i data/findings.json -o output/report.md
  %(prog)s -i data/stigviewer.json -o output/reference.md
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        required=True,
        metavar="FILE",
        help="Input STIG file (.ckl, .csv, .json)",
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        required=True,
        metavar="FILE",
        help="Output file (.ckl, .csv, .json, .md)",
    )
    parser.add_argument(
        "-n", "--name",
        metavar="NAME",
        help="Project name (optional, included in output where applicable)",
    )
    parser.add_argument(
        "--base-ckl",
        dest="base_ckl",
        type=Path,
        metavar="FILE",
        help="Base CKL template (required for JSON → CKL conversion)",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )
    return parser


def parse_args(args: Optional[list] = None) -> argparse.Namespace:
    parser = create_parser()
    parsed = parser.parse_args(args)
    try:
        validate_file_conversion(parsed.input, parsed.output)
    except ValidationError as e:
        parser.error(str(e))
    return parsed


def main() -> None:
    """CLI entry point."""
    args = parse_args()
    try:
        converter = STIGConverter(args)
        converter.convert()
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
