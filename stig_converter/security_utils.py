# security_utils.py
# Security utilities for STIG converter scripts

from pathlib import Path


def validate_file_path(file_path, allowed_dirs):
    """
    Validate file paths to prevent directory traversal attacks.
    :param file_path: The file path to validate
    :param allowed_dirs: List of allowed base directories
    :return: Validated absolute path
    :raises ValueError: If path is not within any allowed directory
    """
    path_obj = Path(file_path).resolve()

    for allowed_dir in allowed_dirs:
        allowed_path = Path(allowed_dir).resolve()
        try:
            path_obj.relative_to(allowed_path)
            return path_obj
        except ValueError:
            continue

    raise ValueError(f"File path not allowed: {file_path}")


def get_default_allowed_dirs():
    """
    Get default allowed directories for file operations.
    :return: List of allowed base directories
    """
    return [
        Path.cwd(),
        Path.cwd() / "data",
        Path.cwd().parent / "data",
        Path.cwd() / "output",
        Path.cwd().parent / "output",
    ]


def validate_output_path(output_path, input_path=None, allowed_dirs=None, extension=None):
    """
    Validate output file path and ensure parent directory exists.
    :param output_path: Desired output path (file or directory)
    :param input_path: Optional input path used to derive a default filename
    :param allowed_dirs: List of allowed base directories
    :param extension: File extension to use when output_path is a directory (e.g. ".csv")
    :return: Validated output path
    """
    if allowed_dirs is None:
        allowed_dirs = get_default_allowed_dirs()

    output_path = Path(output_path)

    # If output_path is a directory, construct a default filename from the input stem
    if output_path.is_dir() and input_path:
        from datetime import datetime

        current_date = datetime.now().strftime("%Y%m%d")
        input_stem = Path(input_path).stem
        ext = extension or ".txt"
        output_path = output_path / f"{input_stem}-{current_date}{ext}"

    validated_path = validate_file_path(output_path, allowed_dirs)
    validated_path.parent.mkdir(parents=True, exist_ok=True)

    return validated_path
