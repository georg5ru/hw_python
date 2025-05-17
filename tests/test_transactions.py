import unittest
from unittest.mock import patch
from src.external_api import convert_to_rub
from src.transaction import get_amount_in_rub


class TestTransactions(unittest.TestCase):

    @patch('external_api.requests.get')
    def test_convert_to_rub(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'result': 7500.0}

        result = convert_to_rub("100", "USD")  # Оба аргумента переданы
        self.assertEqual(result, 7500.0)

    def test_get_amount_in_rub(self):
        transaction_rub = {
            "operationAmount": {
                "amount": "1000.00",
                "currency": {
                    "code": "RUB"
                }
            }
        }
        result = get_amount_in_rub(transaction_rub)
        self.assertEqual(result, 1000.0)

        with patch('src.external_api.convert_to_rub', return_value=7500.0):
            transaction_usd = {
                "operationAmount": {
                    "amount": "100.00",
                    "currency": {
                        "code": "USD"
                    }
                }
            }
            result = get_amount_in_rub(transaction_usd)
            self.assertEqual(result, 7500.0)


if __name__ == "__main__":
    unittest.main()