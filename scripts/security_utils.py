# security_utils.py
# Security utilities for STIG converter scripts

import os
from pathlib import Path


def validate_file_path(file_path, allowed_dirs):
    """
    Validate file paths to prevent directory traversal attacks
    :param file_path: The file path to validate
    :param allowed_dirs: List of allowed base directories
    :return: Validated absolute path
    :raises ValueError: If path is not allowed
    """
    # Convert to Path object and resolve
    path_obj = Path(file_path).resolve()
    abs_path = str(path_obj)

    # Check if path is within allowed directories
    for allowed_dir in allowed_dirs:
        allowed_abs = str(Path(allowed_dir).resolve())
        if abs_path.startswith(allowed_abs):
            return path_obj

    raise ValueError(f"File path not allowed: {file_path}")


def get_default_allowed_dirs():
    """
    Get default allowed directories for file operations
    :return: List of allowed base directories
    """
    return [
        Path.cwd(),
        Path.cwd() / "data",
        Path.cwd().parent / "data",
        Path.cwd() / "output",
        Path.cwd().parent / "output",
    ]


def validate_output_path(output_path, input_path=None, allowed_dirs=None):
    """
    Validate output file path and ensure parent directory exists
    :param output_path: Desired output path
    :param input_path: Optional input path for creating default output name
    :param allowed_dirs: List of allowed base directories
    :return: Validated output path
    """
    if allowed_dirs is None:
        allowed_dirs = get_default_allowed_dirs()

    output_path = Path(output_path)

    # If output_path is a directory, construct default filename
    if output_path.is_dir() and input_path:
        from datetime import datetime

        current_date = datetime.now().strftime("%Y%m%d")
        input_stem = Path(input_path).stem

        # Determine extension based on calling context (fallback to .txt)
        import inspect

        frame = inspect.currentframe().f_back
        if "csv" in frame.f_code.co_name:
            ext = ".csv"
        elif "json" in frame.f_code.co_name:
            ext = ".json"
        elif "markdown" in frame.f_code.co_name:
            ext = ".md"
        elif "ckl" in frame.f_code.co_name:
            ext = ".ckl"
        else:
            ext = ".txt"

        output_path = output_path / f"{input_stem}-{current_date}{ext}"

    # Validate the path
    validated_path = validate_file_path(output_path, allowed_dirs)

    # Ensure parent directory exists
    validated_path.parent.mkdir(parents=True, exist_ok=True)

    return validated_path
