"""Функции для маскирования номеров карт и счетов."""

def get_mask_card_number(card_number: str) -> str:
    """Возвращает замаскированный номер банковской карты."""
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_number


def get_mask_account(account_number: str) -> str:
    """Возвращает замаскированный номер банковского счёта."""
    masked_account = "**" + account_number[-4:]
    return masked_account
