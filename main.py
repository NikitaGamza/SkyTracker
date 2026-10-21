from src.APIAdapter import APIAdapter
from src.PlaneInfo import PlaneInfo


if __name__ == "__main__":
    country = input("Введите название страны для запроса к API: ").strip()
    res = APIAdapter()
    res.get_aeroplanes(country)
    print(res.aeroplanes)
    # plane = PlaneInfo()

