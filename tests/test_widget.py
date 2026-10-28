import pytest

from widget import mask_account_card


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
