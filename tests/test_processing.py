import pytest

from processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    return [
        {"id": 1, "state": "EXECUTED"},
        {"id": 2, "state": "CANCELED"},
        {"id": 3, "state": "EXECUTED"},
    ]


@pytest.mark.parametrize(
    "state, expected",
    [
        (
        "EXECUTED",
    [
             {"id": 1, "state": "EXECUTED"},
             {"id": 3, "state": "EXECUTED"},
            ],
        ),
        ("CANCELED", [{"id": 2, "state": "CANCELED"}]),
        ("PENDING", []),
    ],
)
def test_filter_by_state(operations, state, expected):
    assert filter_by_state(operations, state) == expected


@pytest.fixture
def operations_by_date():
    return [
        {"id": 1, "date": "2024-03-11T02:26:18.000000"},
        {"id": 2, "date": "2022-01-01T00:00:00.000000"},
        {"id": 3, "date": "2023-05-15T12:00:00.000000"},
    ]


def test_sort_by_date_descending(operations_by_date):
    result = sort_by_date(operations_by_date)

    expected = [
        {"id": 1, "date": "2024-03-11T02:26:18.000000"},
        {"id": 3, "date": "2023-05-15T12:00:00.000000"},
        {"id": 2, "date": "2022-01-01T00:00:00.000000"},
    ]

    assert result == expected


def test_sort_by_date_ascending(operations_by_date):
    result = sort_by_date(operations_by_date, descending=False)

    expected = [
        {"id": 2, "date": "2022-01-01T00:00:00.000000"},
        {"id": 3, "date": "2023-05-15T12:00:00.000000"},
        {"id": 1, "date": "2024-03-11T02:26:18.000000"},
    ]

    assert result == expected