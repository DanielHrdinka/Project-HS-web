import pytest
from unittest.mock import MagicMock

from companies import Company
from curencies import CurrencyAPIClient

def test_company_attributes():
    c = Company("Haas", "US", "machine tools")
    assert c.name == "Haas"
    assert c.country == "US"
    assert c.spec == "machine tools"

@pytest.fixture
def converter_fixture():
    mocked_client = MagicMock(spec=CurrencyAPIClient)
    mocked_client.get_rate.return_value = 25
    return mocked_client

def test_convert_to_czk(converter_fixture):
    amount = 10
    result = amount * converter_fixture.get_rate("CZK")
    assert result == 250
