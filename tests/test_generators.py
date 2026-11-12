from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator

transactions = [
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        },
        "description": "Перевод организации"
    },
    {
        "operationAmount": {
            "currency": {"code": "RUB"}
        },
        "description": "Перевод со счета на счет"
    },
    {
        "operationAmount": {
            "currency": {"code": "USD"}
        },
        "description": "Перевод с карты на карту"
    }
]


def test_filter_by_currency():
    result = list(filter_by_currency(transactions, "USD"))

    assert len(result) == 2

    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == "USD"


def test_filter_by_currency_no_matches():
    result = list(filter_by_currency(transactions, "EUR"))

    assert result == []


def test_transaction_descriptions():
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту"
    ]


def test_card_number_generator():
    result = list(card_number_generator(1, 4))

    assert result == [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004"
    ]