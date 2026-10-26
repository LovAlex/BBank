def filter_by_state(data: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Возвращает операции с указанным статусом."""
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: list[dict], reverse: bool = True) -> list[dict]:
    """Сортирует операции по дате."""
    return sorted(data, key=lambda item: item.get("date", ""), reverse=reverse)


