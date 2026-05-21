"""Smoke tests verifying the package structure and basic imports."""

from pathlib import Path


def test_package_imports():
    from stig_converter import STIGConverter, __version__
    assert STIGConverter is not None
    assert __version__ == "2.3"


def test_converter_imports():
    from stig_converter.converters.ckl_to_csv import convert_ckl_to_csv
    from stig_converter.converters.ckl_to_json import convert_ckl_to_json
    from stig_converter.converters.csv_to_json import convert_csv_to_json
    from stig_converter.converters.json_to_ckl import convert_json_to_ckl
    from stig_converter.converters.json_to_markdown import (
        convert_checklist_to_md,
        write_stigs,
    )
    from stig_converter.converters.get_new_stigs import get_stig_json, get_stig_zip
    assert all([
        convert_ckl_to_csv, convert_ckl_to_json, convert_csv_to_json,
        convert_json_to_ckl, convert_checklist_to_md, write_stigs,
        get_stig_json, get_stig_zip,
    ])


def test_update_filename_no_date():
    """update_filename appends today's date when none exists."""
    import argparse
    from stig_converter.stig_converter import STIGConverter

    args = argparse.Namespace(input=Path("a.ckl"), output=Path("b.csv"), name=None, base_ckl=None)
    c = STIGConverter(args)
    result = c.update_filename("checklist.ckl")
    assert result.startswith("checklist-")
    assert result.endswith(".ckl")
    assert len(result) == len("checklist-YYYYMMDD.ckl")


def test_update_filename_replaces_date():
    """update_filename replaces an existing date with today's."""
    import argparse
    from stig_converter.stig_converter import STIGConverter

    args = argparse.Namespace(input=Path("a.ckl"), output=Path("b.csv"), name=None, base_ckl=None)
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
