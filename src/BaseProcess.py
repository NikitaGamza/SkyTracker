from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseProcess(ABC):
    """Абстрактный класс для работы с файлами и данными о самолётах"""

    __filename: str

    def __init__(self, __filename: str = "aeroplanes.json") -> None:
        root_dir = Path(__file__).resolve().parent.parent  # src -> корень проекта
        data_dir = root_dir / "data"
        data_dir.mkdir(parents=True, exist_ok=True)  # создаём, если нет

        self._file_path = data_dir / __filename

    @property
    def file_path(self) -> Path:
        return self._file_path

    @abstractmethod
    def add_aeroplane(self, aeroplane_data: dict[str, Any]) -> None:
        """Добавить информацию о самолёте в файл"""
        raise NotImplementedError

    @abstractmethod
    def get_aeroplanes(self, **criteria: Any) -> list[dict[str, Any]]:
        """
        Получить данные из файла по указанным критериям.
        Пример критериев: reg_country="Iran", min_altitude=10000, max_altitude=15000.
        """
        raise NotImplementedError

    # @abstractmethod
    # def delete_aeroplanes(self, **criteria: Any) -> None:
    #     """Удалить информацию о самолётах в файле по указанным критериям"""
    #     raise NotImplementedError