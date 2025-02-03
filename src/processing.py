def filter_by_state(dicts: list, state='EXECUTED') -> list:
    result = []
    for i in dicts:
        if i['state'] == state:
            result.append(i)
    return result


def sort_by_date(dicts: list, date=True) -> list:
    return sorted(dicts, reverse=date, key=lambda x: x['date'])
