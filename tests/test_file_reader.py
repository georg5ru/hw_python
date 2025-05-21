from unittest.mock import patch
from src.file_reader import read_json_file
from src.external_api import convert_to_rub


def test_read_json_file():
    result = read_json_file('data/operations.json')
    print(f"Result: {result}")
    assert isinstance(result, list)
    if result:
        assert result != []

