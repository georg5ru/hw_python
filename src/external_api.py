import os
import requests
from dotenv import load_dotenv

load_dotenv()


def convert_to_rub(amount, currency):
    """
    Конвертирует сумму в рубли с использованием внешнего API.

    """
    if currency == "RUB":
        return float(amount)

    # Получаем токен API из переменных окружения
    api_key = os.getenv("API_KEY")
    if not api_key:
        raise ValueError("API_KEY не найден в переменных окружения.")

    url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}"

    headers = {
        "apikey": api_key
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Ошибка при запросе к API: {response.status_code}")


    result = response.json()
    return float(result['result'])