from src.masks import get_mask_card_number, get_mask_account
import pytest


@pytest.fixture
def fixture_card_number():
    return '7000792289606361'


def test_get_mask_card_number(fixture_card_number):
    assert get_mask_card_number(fixture_card_number) == '7000 79** **** 6361'


@pytest.fixture
def fixture_mask_account():
    return '73654108430135874305'


def test_get_mask_account(fixture_mask_account):
    assert get_mask_account(fixture_mask_account) == '**4305'
