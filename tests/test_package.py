"""Smoke tests verifying the package structure and basic imports."""

from pathlib import Path


def test_package_imports():
    from stig_converter import STIGConverter, __version__
    assert STIGConverter is not None
    assert __version__ == "2.4"


def test_converter_imports():
    from stig_converter.converters.ckl_to_csv import convert_ckl_to_csv
    from stig_converter.converters.ckl_to_json import convert_ckl_to_json
    from stig_converter.converters.csv_to_json import convert_csv_to_json
    from stig_converter.converters.json_to_ckl import convert_json_to_ckl
    from stig_converter.converters.json_to_markdown import (
        convert_checklist_to_md,
        convert_json_to_md,
        write_stigs,
    )
    from stig_converter.converters.ckl_to_markdown import convert_ckl_to_md
    from stig_converter.get_new_stigs import get_stig_json, get_stig_zip
    assert all([
        convert_ckl_to_csv, convert_ckl_to_json, convert_csv_to_json,
        convert_json_to_ckl, convert_checklist_to_md, convert_json_to_md,
        convert_ckl_to_md, write_stigs, get_stig_json, get_stig_zip,
    ])


def test_update_filename_no_date():
    """update_filename appends today's date when none exists."""
    import argparse
    from stig_converter.stig_converter import STIGConverter

    args = argparse.Namespace(input=Path("a.ckl"), output=Path("b.csv"), name=None, template_ckl=None)
    c = STIGConverter(args)
    result = c.update_filename("checklist.ckl")
    assert result.startswith("checklist-")
    assert result.endswith(".ckl")
    assert len(result) == len("checklist-YYYYMMDD.ckl")


def test_update_filename_replaces_date():
    """update_filename replaces an existing date with today's."""
    import argparse
    from stig_converter.stig_converter import STIGConverter

    args = argparse.Namespace(input=Path("a.ckl"), output=Path("b.csv"), name=None, template_ckl=None)
    c = STIGConverter(args)
    result = c.update_filename("checklist-20210101.ckl")
    assert result.startswith("checklist-")
    assert result.endswith(".ckl")
    assert "20210101" not in result


def test_validate_file_conversion_same_file():
    from stig_converter.stig_converter import validate_file_conversion, ValidationError
    import pytest
    with pytest.raises(ValidationError, match="cannot be the same"):
        validate_file_conversion(Path("data/a.ckl"), Path("data/a.ckl"))


def test_validate_file_conversion_unsupported():
    from stig_converter.stig_converter import validate_file_conversion, ValidationError
    import pytest
    with pytest.raises(ValidationError, match="Unsupported input type"):
        validate_file_conversion(Path("data/a.txt"), Path("data/b.csv"))


def test_get_stig_zip_creates_parent_dir(tmp_path):
    """get_stig_zip must create the parent directory before writing."""
    from unittest.mock import patch, MagicMock
    from stig_converter.get_new_stigs import get_stig_zip

    nested = tmp_path / "new_subdir" / "output.zip"
    assert not nested.parent.exists()

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.content = b"PK\x03\x04"  # minimal zip magic bytes

    with patch("stig_converter.get_new_stigs.httpx.Client") as mock_client:
        mock_client.return_value.__enter__.return_value.get.return_value = mock_response
        get_stig_zip(str(nested), allowed_dirs=[tmp_path])

    assert nested.parent.exists()
    assert nested.exists()


def test_get_stig_json_creates_parent_dir(tmp_path):
    """get_stig_json must create the parent directory before writing."""
    from unittest.mock import patch, MagicMock
    from stig_converter.get_new_stigs import get_stig_json

    nested = tmp_path / "new_subdir" / "stigs.json"
    assert not nested.parent.exists()

    mock_response = MagicMock()
    mock_response.json.return_value = {"stig": {}}

    with patch("stig_converter.get_new_stigs.httpx.get", return_value=mock_response):
        get_stig_json(str(nested), allowed_dirs=[tmp_path])

    assert nested.parent.exists()
    assert nested.exists()
