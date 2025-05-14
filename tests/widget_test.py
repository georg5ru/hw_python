from src.widget import mask_account_card, get_date
import pytest



@pytest.fixture
def fixture_get_date():
    return '2024-03-11T02:26:18.671407'


def test_get_date(fixture_get_date):
    assert get_date(fixture_get_date) == '11.03.2024'
