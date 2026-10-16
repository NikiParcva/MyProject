from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_card(info: str) -> str:
    parts = info.split()
    number = parts[-1]
    card_name = " ".join(parts[:-1])

    if card_name.lower() == "счет":
        masked_number = get_mask_account(number)
    else:
        masked_number = get_mask_card_number(number)

    return f"{card_name} {masked_number}"


def get_date(time: str) -> str:
    formated_time = datetime.strptime(time, "%Y-%m-%dT%H:%M:%S.%f")
    return formated_time.strftime("%d.%m.%Y")
