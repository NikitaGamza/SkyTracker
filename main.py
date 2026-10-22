from src.APIAdapter import APIAdapter
from src.PlaneInfo import PlaneInfo


if __name__ == "__main__":
    country = input("Введите название страны для запроса к API: ").strip()
    res = APIAdapter()
    res.get_aeroplanes(country)

    planes = PlaneInfo.get_filter_aeroplanes(res.aeroplanes)
    # for plane_info in planes:
    #     print(plane_info)
    print(planes)

