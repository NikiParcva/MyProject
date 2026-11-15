import pytest

from src.generators import filter_by_currency
from src.generators import transaction_descriptions
from src.generators import card_number_generator


@pytest.fixture
def transactions():
    return [
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


@pytest.mark.parametrize(
    "currency, expected_count",
    [
        ("USD", 2),
        ("RUB", 1),
        ("EUR", 0)
    ]
)
def test_filter_by_currency(transactions, currency, expected_count):
    result = list(filter_by_currency(transactions, currency))

    assert len(result) == expected_count

    for transaction in result:
        assert transaction["operationAmount"]["currency"]["code"] == currency


def test_transaction_descriptions(transactions):
    result = list(transaction_descriptions(transactions))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод с карты на карту"
    ]


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            1,
            4,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
                "0000 0000 0000 0004"
            ]
        ),
        (
            6,
            6,
            ["0000 0000 0000 0006"]
        )
    ]
)
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))

    assert result == expected
