from src.APIAdapter import APIAdapter
from src.PlaneInfo import PlaneInfo

def sort_aeroplanes(aeroplanes):
    """
    Сортировка самолётов, поскольку в Aeroplane реализованы __lt__/__eq__...,
    sorted() может использовать их напрямую.
    """
    return sorted(aeroplanes, reverse=True)

if __name__ == "__main__":
    country = input("Введите название страны для запроса к API: ").strip()
    # top = int(input("Введите количество самолётов в топ N по высоте: ").strip())
    res = APIAdapter()
    res.get_aeroplanes(country)

    planes = PlaneInfo.get_filter_aeroplanes(res.aeroplanes)

    sorted_planes = sort_aeroplanes(planes)

    for plane in sorted_planes:
        print(plane)
