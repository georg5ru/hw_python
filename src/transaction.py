from src.external_api import convert_to_rub


def get_amount_in_rub(transaction):
    try:
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]
    except KeyError as e:
        raise ValueError(f"Missing required field in transaction: {e}")

    if currency == "RUB":
        return amount

    return convert_to_rub(amount, currency)