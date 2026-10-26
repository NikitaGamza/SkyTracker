from src.APIAdapter import APIAdapter
from src.PlaneInfo import PlaneInfo
from src.process_file import Processing


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
    return [
        plane for plane in aeroplanes if plane.reg_country.lower() in reg_countries_norm
    ]


def load_aeroplanes_by_country(country: str) -> list[PlaneInfo]:
    """load and transform planes data by country."""
    api = APIAdapter()
    api.get_aeroplanes(country)

    if api.aeroplanes is None:
        print("No airplanes data")
        return []

    # transform array of data to list if objects PlaneInfo
    planes = PlaneInfo.get_filter_aeroplanes(api.aeroplanes)

    # Save all planes in JSON
    storage = Processing()
    for plane in planes:

        storage.add_aeroplane(
            {
                "callsign": plane.call_sign,
                "reg_country": plane.reg_country,
                "velocity": plane.velocity,
                "altitude": plane.altitude,
            }
        )
    return planes
