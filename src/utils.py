def get_top_aeroplanes(aeroplanes, top: int):
    """Возвращает топ N самолётов из уже отсортированного списка."""
    return list(aeroplanes)[:top]


def sort_aeroplanes(aeroplanes):
    """
    Сортировка самолётов, поскольку в Aeroplane реализованы __lt__/__eq__...,
    sorted() может использовать их напрямую.
    """
    return sorted(aeroplanes, reverse=True)


def filter_aeroplanes(aeroplanes, reg_countries: list[str]):
    """Фильтрация самолётов по стране регистрации (origin_country)"""
    if not reg_countries:
        return list(aeroplanes)

    reg_countries_norm = {c.strip().lower() for c in reg_countries if c.strip()}
    return [plane for plane in aeroplanes if plane.reg_country.lower() in reg_countries_norm]