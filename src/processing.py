def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    result = []
    for elements in data:
        if elements["state"] == state:
            result.append(elements)
    return result


def sort_by_date(data: list, descending: bool = True) -> list:
    return sorted(data, key=lambda item: item["date"], reverse=descending)
