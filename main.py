from src.APIAdapter import APIAdapter
from src.PlaneInfo import PlaneInfo
from src.utils import filter_aeroplanes, get_top_aeroplanes, sort_aeroplanes

if __name__ == "__main__":
    country = input("Введите название страны для запроса к API: ").strip()
    top = int(input("Введите количество самолётов в топ N по высоте: ").strip())
    filter_words = input(
        "Введите названия стран регистрации (через пробел) для фильтрации: "
    ).split()
    res = APIAdapter()
    res.get_aeroplanes(country)

    planes = PlaneInfo.get_filter_aeroplanes(res.aeroplanes)

    filtered_aeroplanes = filter_aeroplanes(planes, filter_words)
    sorted_planes = sort_aeroplanes(filtered_aeroplanes)
    top_aeroplanes = get_top_aeroplanes(sorted_planes, top)

    for plane in top_aeroplanes:
        print(plane)
