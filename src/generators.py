def filter_by_currency(transactions: list, value: str) -> dict:
    for i in transactions:
        if i['operationAmount']['currency']['code'] == value:
            yield i


def transaction_descriptions(transactions: list) -> str:
    for i in transactions:
        yield i['description']

def card_number_generator(start: int, end: int) -> str:
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
