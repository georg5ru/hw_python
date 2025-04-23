from external_api import convert_to_rub


def get_amount_in_rub(transaction):
    """
    Возвращает сумму транзакции в рублях.
    """
    amount = transaction['operationAmount']['amount']
    currency = transaction['operationAmount']['currency']['code']

    # Если валюта уже в рублях, возвращаем сумму
    if currency == "RUB":
        return float(amount)

    # Конвертируем сумму в рубли
    return convert_to_rub(amount, currency)