# BBank — обработка банковских операций

## Описание проекта

BBank — учебный Python-проект для обработки списка банковских операций. Проект содержит функции фильтрации операций по статусу и сортировки по дате.

## Функциональность

- 'filter_by_state' — фильтрует операции по статусу. По умолчанию возвращает операции со статусом 'EXECUTED'.
- 'sort_by_date' — сортирует операции по дате. По умолчанию сортирует от более поздней даты к более ранней.

## Требования

- Python 3.14
- Poetry для управления зависимостями проекта

## Установка

'''bash
git clone git@github.com:LovAlex/BBank.git
cd BBank
poetry install
''''

## Пример использования

'''python
import sys

sys.path.insert(0, "src")
from processing import filter_by_state, sort_by_date

operations = [
    {"state": "EXECUTED", "date": "2026-10-20"},
    {"state": "CANCELED", "date": "2026-10-22"},
    {"state": "EXECUTED", "date": "2026-10-25"},
]

print(filter_by_state(operations))
print(sort_by_date(operations))
'''

## Структура проекта

'''text
BBank/
├── src/
│   └── processing.py
├── README.md
├── pyproject.toml
└── poetry.lock
'''

## Статус проекта

Учебный проект в разработке.