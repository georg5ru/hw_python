def get_mask_card_number(number: int) -> str:
    result = ""
    counter = 1
    for i in str(number):
        if counter == 4:
            result += i
            result += " "
        elif counter == 8 or counter == 12:
            result += "* "
        elif counter > 6 and counter <= 12:
            result += "*"
        else:
            result += i
        counter += 1
    return result


def get_mask_account(number: int) -> str:
    result = "**" + str(number)[-4::]
    return result

