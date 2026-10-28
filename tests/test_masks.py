
import pytest

from masks import get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("1234567890123456", "1234 56** **** 3456"),
        ("7000696989606361", "7000 69** **** 6361"),
        ("0000000000000000", "0000 00** **** 0000"),
    ],
)
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


from masks import get_mask_account


@pytest.mark.parametrize(
    "account_number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("1234", "**1234"),
        ("676754321", "**4321"),
        ("00000000", "**0000"),
    ],
)
def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected
