from src.APIAdapter import APIAdapter


if __name__ == "__main__":
    api = APIAdapter()
    print(api.get_aeroplanes('Germany'))
