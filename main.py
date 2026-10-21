from src.APIAdapter import APIAdapter


if __name__ == "__main__":
    country = input("Введите название страны для запроса к API: ").strip()
    res = APIAdapter()
    print(res.get_aeroplanes(country))

