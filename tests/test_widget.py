import pytest

from widget import mask_account_card, get_date


@pytest.mark.parametrize(
    "info, expected",
    [
        ("Visa Platinum 1234567890123456", "Visa Platinum 1234 56** **** 3456"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("счет 1234567890", "счет **7890"),
    ],
)
def test_mask_account_card(info, expected):
    assert mask_account_card(info) == expected


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2024-03-11T02:26:18.000000", "11.03.2024"),
        ("2025-12-31T23:59:59.000000", "31.12.2025"),
        ("2026-01-01T00:00:00.000000", "01.01.2026"),
    ],
)
def test_get_date(date_string, expected):
    assert get_date(date_string) == expected


def test_get_date_invalid_format():
    with pytest.raises(ValueError):
        get_date("11.05.2022")