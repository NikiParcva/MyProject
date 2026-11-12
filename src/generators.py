def filter_by_currency(transactions: list, currency: str):
    """Фильтрует транзакции по заданной валюте."""

    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction

def transaction_descriptions(transactions: list):
    """Генерирует описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start: int, end: int):
    """Генерирует номера карт в заданном диапазоне."""

    for number in range(start, end + 1):
        formatted_number = str(number).zfill(16)
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:]}"
