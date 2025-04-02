from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(card: str) -> str:
    words = card.split()
    counter = 1
    for i in words:
        if i[0] in "0123456789":
            number = i
            break
        counter += 1
    counter_two = 0
    type_card = ""
    while counter_two < counter - 1:
        if counter_two != 0:
            type_card += " "
        type_card += words[counter_two]
        counter_two += 1
    if type_card == "Счет":
        result = f"Счет {get_mask_account(int(number))}"
        return result
    else:
        result = f"{type_card} {get_mask_card_number(int(number))}"
        return result


def get_date(time: str) -> str:
    time_list = time.split("-")
    result = f"{time_list[2][:2]}.{time_list[1]}.{time_list[0]}"
    return result
