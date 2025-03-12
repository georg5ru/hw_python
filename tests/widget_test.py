from src.widget import mask_account_card, get_date
import pytest


@pytest.fixture
def fixture_mask_account_card():
    return 'Visa Platinum 7000792289606361', 'Счет 73654108430135874305'


def test_mask_account_card(fixture_mask_account_card):
    first, second = fixture_mask_account_card
    assert mask_account_card(first) == 'Visa Platinum 7000 79** **** 6361'
    assert mask_account_card(second) == 'Счет **4305'


@pytest.fixture
def fixture_get_date():
    return '2024-03-11T02:26:18.671407'


def test_get_date(fixture_get_date):
    assert get_date(fixture_get_date) == '11.03.2024'
