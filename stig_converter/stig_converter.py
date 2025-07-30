"""
Name: stig_converter.py
TLDR: Converts STIG Checklists to other various file formats
Author: Allen Montgomery, IO Security
Date: Apr 2025
"""

import argparse
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

__version__ = "2.3"


class STIGConverter:
    """
    Converts STIG Checklists to/from various file formats (CSV, JSON, CKL)
    """

    def __init__(self, args: argparse.Namespace) -> None:
        self.input_file_path = args.input
        self.output_file_path = args.output
        self.project_name = getattr(args, 'name', None)
        self.event = getattr(args, 'event', False)
        self.encoding = "utf-8"
        self.date = datetime.now().strftime("%Y%m%d")

    def update_filename(self, filename: str) -> str:
        """
        Updates the timestamp of the checklist to the current date
        If the file already has a date in the filename, then it will replace it with the current date
        If the file doesn't have a date in the filename, then it will append the current date to the end
        Example: stig_checklist-20210723.ckl -> stig_checklist-20210724.ckl
        Example: stig_checklist.ckl -> stig_checklist-20210724.ckl
        """
        # Check if the filename has a date in it (eg -20210723)
        pattern = r"-(\d{8})"
        match = re.search(pattern, filename)

        if match:
            matched_sequence = match.group(1)
            # replace the date in the filename with the current date
            updated_filename = filename.replace(matched_sequence, self.date)
            # return the name of the file with the updated date
            return updated_filename
        else:
            # if there is no date in the filename, then add the current date to the end
            name, ext = filename.split(".")[:2]
            updated_filename = f"{name}-{self.date}.{ext}"
            return updated_filename


class ValidationError(Exception):
    """Custom exception for validation errors"""
    pass


def validate_file_conversion(input_path: Path, output_path: Path) -> None:
    """
    Validates that the file conversion is supported and paths are correct
    
    Args:
        input_path: Path to input file
        output_path: Path to output file
        
    Raises:
        ValidationError: If validation fails
    """
    supported_conversions = {
        "ckl": ["csv", "json", "md"],
        "csv": ["json"],
        "json": ["ckl", "md"],
    }
    
    # Check if input and output are the same
    if input_path.resolve() == output_path.resolve():
        raise ValidationError(f"Input and output files cannot be the same: {input_path}")
    
    # Check if input file exists
    if not input_path.is_file():
        raise ValidationError(f"Input file does not exist: {input_path}")
    
    # Get file extensions
    input_ext = input_path.suffix[1:].lower()
    output_ext = output_path.suffix[1:].lower()
    
    # Validate input file type
    if input_ext not in supported_conversions:
        valid_types = ', '.join(supported_conversions.keys())
        raise ValidationError(f"Unsupported input file type '{input_ext}'. Supported types: {valid_types}")
    
    # Validate conversion path
    if output_ext not in supported_conversions[input_ext]:
        valid_outputs = ', '.join(supported_conversions[input_ext])
        raise ValidationError(
            f"Cannot convert from '{input_ext}' to '{output_ext}'. "
            f"Valid outputs for '{input_ext}': {valid_outputs}"
        )
    
    # Ensure output directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)


def create_parser() -> argparse.ArgumentParser:
    """
    Creates and configures the argument parser
    
    Returns:
        Configured ArgumentParser instance
    """
    parser = argparse.ArgumentParser(
        prog='stig_converter',
        description='Convert DISA STIG checklists between various file formats (CKL, CSV, JSON, Markdown)',
        epilog='''
Examples:
  %(prog)s -i checklist.ckl -o report.csv
  %(prog)s --input data.json --output checklist.ckl --name "My Project"
  %(prog)s -i checklist.ckl -o report.md --event
        ''',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    # Required arguments
    parser.add_argument(
        '-i', '--input',
        type=Path,
        required=True,
        metavar='FILE',
        help='Input STIG checklist file (supported: .ckl, .csv, .json)'
    )
    
    parser.add_argument(
        '-o', '--output', 
        type=Path,
        required=True,
        metavar='FILE',
        help='Output file path (supported: .ckl, .csv, .json, .md)'
    )
    
    # Optional arguments
    parser.add_argument(
        '-n', '--name',
        metavar='NAME',
        help='Project name to include in output (optional)'
    )
    
    parser.add_argument(
        '-e', '--event',
        action='store_true',
        help='Enable event mode processing (optional)'
    )
    
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    return parser


def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """
    Parses command line arguments with validation
    
    Args:
        args: Optional list of arguments (for testing)
        
    Returns:
        Parsed and validated arguments
        
    Raises:
        SystemExit: On argument parsing or validation errors
    """
    parser = create_parser()
    
    try:
        parsed_args = parser.parse_args(args)
        
        # Validate file conversion
        validate_file_conversion(parsed_args.input, parsed_args.output)
        
        return parsed_args
        
    except ValidationError as e:
        parser.error(str(e))
    except Exception as e:
        parser.error(f"Unexpected error: {e}")


def main() -> None:
    """Main entry point for the STIG converter"""
    try:
        # Parse and validate arguments
        args = parse_args()
        
        # Create converter instance
        converter = STIGConverter(args)
        
        print(f"[*] Converting {args.input} to {args.output}")
        
        # TODO: Implement actual conversion methods based on file types
        # For now, this is a placeholder showing the improved structure
        print(f"[*] Input file: {converter.input_file_path}")
        print(f"[*] Output file: {converter.output_file_path}")
        if converter.project_name:
            print(f"[*] Project name: {converter.project_name}")
        if converter.event:
            print(f"[*] Event mode: enabled")
            
        # TODO: Call appropriate conversion method based on file extensions
        # converter.convert()
        
    except KeyboardInterrupt:
        print("\n[!] Operation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"[X] Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
