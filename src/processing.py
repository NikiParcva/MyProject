from typing import Any


def filter_by_state(data: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Фильтрует операции по указанному статусу."""
    result = []
    for elements in data:
        if elements["state"] == state:
            result.append(elements)
    return result


def sort_by_date(data: list[dict[str, Any]], descending: bool = True) -> list[dict[str, Any]]:
    """Сортирует операции по дате."""
    return sorted(data, key=lambda item: item["date"], reverse=descending)
