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

Функции находятся в модуле `src/processing.py`.

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
