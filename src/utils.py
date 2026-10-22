def get_top_aeroplanes(aeroplanes, top: int):
    """Возвращает топ N самолётов из уже отсортированного списка."""
    return list(aeroplanes)[:top]


def sort_aeroplanes(aeroplanes):
    """
    Сортировка самолётов, поскольку в Aeroplane реализованы __lt__/__eq__...,
    sorted() может использовать их напрямую.
    """
    return sorted(aeroplanes, reverse=True)
