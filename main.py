from src.APIAdapter import APIAdapter
from src.PlaneInfo import PlaneInfo
from src.utils import sort_aeroplanes, get_top_aeroplanes



if __name__ == "__main__":
    country = input("Введите название страны для запроса к API: ").strip()
    top = int(input("Введите количество самолётов в топ N по высоте: ").strip())
    res = APIAdapter()
    res.get_aeroplanes(country)

    planes = PlaneInfo.get_filter_aeroplanes(res.aeroplanes)

    sorted_planes = sort_aeroplanes(planes)
    top_aeroplanes = get_top_aeroplanes(sorted_planes, top)

    for plane in top_aeroplanes:
        print(plane)
