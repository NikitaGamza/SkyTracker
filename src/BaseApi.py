from abc import ABC, abstractmethod


class BaseApi(ABC):
    """Base abstract API class"""

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_aeroplanes(self, country: str) -> None:
        pass