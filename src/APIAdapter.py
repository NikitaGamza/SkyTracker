from requests import get
from src.BaseApi import BaseApi


class APIAdapter(BaseApi):

    def __init__(self) -> None:
        self.openstreetmap_url = 'https://nominatim.openstreetmap.org/search'
        self.opensky_url = 'https://opensky-network.org/api/states/all?'
        self.__aeroplanes = None

    def get_aeroplanes(self, country: str) -> None:
        # Headers с user-agent - обязательный параметр при запросе к nominatim.openstreetmap.
        # Вы можете использовать любое название вместо test-app/1.0, например просто test-app.
        headers_nominatim = {
            'User-Agent': 'test-app/1.0',
        }

        # Указываем параметры: в каком формате возвращать данные и максимальную длину списка стран в ответе.
        params_nominatim = {
            'country': country,
            'format': 'json',
            'limit': 1,
        }

        response = get(url=self.openstreetmap_url, params=params_nominatim, headers=headers_nominatim)

        if response.status_code != 200:
            print(f"nominatim.openstreetmap.org wrong answer: " f"{response.status_code}")
            self.__aeroplanes = None
            return

        data = response.json()

        if not data or  data[0].get('boundingbox'):
            print("nominatim.openstreetmap.org is enpty result")
            self.__aeroplanes = None
            return

        # Пример ответа от nominatim.openstreetmap можно посмотреть в задании курсовой.
        geo_coordinates = data[0].get('boundingbox')

        if not geo_coordinates or len(geo_coordinates) < 4:
            print("Could not get geo coordinates")
            self.__aeroplanes = None
            return

        # Параметры для фильтрации самолетов по их географическим координатам.
        params = {
            'lamin': geo_coordinates[0],
            'lamax': geo_coordinates[1],
            'lomin': geo_coordinates[2],
            'lomax': geo_coordinates[3],
        }

        response = get(url=self.opensky_url, params=params)

        # Пример ответа от opensky-network можно посмотреть в задании курсовой.
        self.__aeroplanes = response.json()

    @property
    def aeroplanes(self):
        """return aeroplanes."""
        return self.__aeroplanes
