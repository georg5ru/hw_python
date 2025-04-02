def filter_by_currency(transactions: list, value: str) -> dict:
    """Функция должна возвращать итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной (например, USD)."""
    for i in transactions:
        if i['operationAmount']['currency']['code'] == value:
            yield i


def transaction_descriptions(transactions: list) -> str:
    """генератор, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди."""
    for i in transactions:
        yield i['description']

def card_number_generator(start: int, end: int) -> str:
    """генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999."""
    for i in range(start, end + 1):
        fours = (16 - len(str(i))) // 4
        zeros = 4 - (len(str(i)) % 4)
        if zeros == 4:
            zeros = 0
        counter = 1
        str_i = ''
        for j in str(i):
            str_i += j
            if counter == 4:
                str_i += ' '
                counter = 0
            counter += 1
        yield ('0000 ' * fours) + ('0' * zeros) + str_i
