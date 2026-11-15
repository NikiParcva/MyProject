# ProjectTest

## Описание проекта

Проект предназначен для обработки данных о банковских операциях. Он содержит функции для фильтрации операций по статусу и сортировки по дате.

## Установка

1. Клонируйте репозиторий.
2. Установите зависимости командой:

```bash
poetry install
```

## Использование

Функции проекта расположены в директории `src/`.

### Модуль masks.py

Модуль `src/masks.py` содержит функции для маскирования номеров банковских карт и счетов.

- `get_mask_card_number(card_number)` — маскирует номер банковской карты, оставляя видимыми первые 6 и последние 4 цифры.
- `get_mask_account(account_number)` — маскирует номер банковского счёта, оставляя видимыми последние 4 цифры.

Пример использования:

```python
from src.masks import get_mask_card_number, get_mask_account

print(get_mask_card_number("1234567890123456"))
# 1234 56** **** 3456

print(get_mask_account("123456789012"))
# **9012
```

### Фильтрация операций по статусу

Функция `filter_by_state(data, state="EXECUTED")` возвращает список операций с указанным статусом. По умолчанию выбираются операции со статусом `EXECUTED`.

Пример:

```python
from src.processing import filter_by_state

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29"},
    {"id": 2, "state": "CANCELED", "date": "2018-10-14T08:21:33"},
]

print(filter_by_state(operations))
print(filter_by_state(operations, "CANCELED"))
```

### Сортировка операций по дате

Функция `sort_by_date(data, descending=True)` возвращает новый список операций, отсортированный по дате.

- `descending=True` — от новых операций к старым (по умолчанию).
- `descending=False` — от старых операций к новым.

Пример:

```python
from src.processing import sort_by_date

sorted_operations = sort_by_date(operations)
print(sorted_operations)
```

### Модуль generators.py

Модуль `src/generators.py` содержит генераторы для работы с транзакциями:

- `filter_by_currency(transactions, currency)` — генерирует транзакции в заданной валюте.
- `transaction_descriptions(transactions)` — последовательно генерирует описания транзакций.
- `card_number_generator(start, end)` — генерирует номера банковских карт в заданном диапазоне.

## Тестирование

Для запуска автоматических тестов проекта используется команда:

```bash
poetry run python -m pytest
```

Тесты проверяют работу функций маскировки банковских карт и счетов, обработки данных, виджетов и генераторов транзакций.

**Результат последнего запуска:** 27 тестов успешно пройдены.

**Покрытие кода тестами:** 100%.

Для проверки покрытия используется команда:

```bash
poetry run python -m pytest --cov=src --cov-report=term-missing
```