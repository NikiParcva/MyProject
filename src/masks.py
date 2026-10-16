def get_mask_card_number(card_number: str) -> str:
    masked_number = card_number[:4] + " " + card_number[4:6] + "** **** " + card_number[-4:]
    return masked_number


def get_mask_account(account_number: str) -> str:
    masked_account = "**" + account_number[-4:]
    return masked_account
