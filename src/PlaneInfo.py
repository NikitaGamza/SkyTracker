from typing import Any


class PlaneInfo:
    """Class for Planes information"""

    call_sign: str
    reg_country: str
    velocity: float
    altitude: float

    def __init__(
        self, call_sign: str, reg_country: str, velocity: float, altitude: float
    ) -> None:
        self.call_sign = self.__validate_string(call_sign, "call_sign is empty")
        self.reg_country = self.__validate_string(reg_country, "reg_country is empty")
        self.velocity = self.__validate_number(
            velocity, "velocity", "velocity is not number"
        )
        self.altitude = self.__validate_number(
            altitude, "altitude", "altitude is not number"
        )

    # ===========> Private methods for checking data <===========

    def __validate_string(self, value: str, error_msg: str) -> str:
        """Checking not empty string"""
        if isinstance(value, str):
            if value := value.strip():
                return value
        raise ValueError(error_msg)

    def __validate_number(
        self, value: float, field_name: str, type_error_msg: str
    ) -> float:
        """Checking numbers"""
        if not isinstance(value, (int, float)):
            raise TypeError(type_error_msg)
        if value < 0:
            raise ValueError(f"{field_name} cannot be negative")
        return float(value)

    # ===========> Шесть методов сравнения через functools <===========

    # functools по аналогии достроит другие 4 варианта сравнений (<=, >, >=, !=)
    def __eq__(self, other: object) -> bool:
        """Метод сравнения == равно, обязательный метод для functools"""
        if not isinstance(other, PlaneInfo):
            return NotImplemented
        # считаем самолёты равными, если совпадает скорость и высота
        return self.velocity == other.velocity and self.altitude == other.altitude

    def __lt__(self, other: object) -> bool:
        """Метод сравнения < меньше для построения functools"""
        if not isinstance(other, PlaneInfo):
            return NotImplemented
        # сначала сравниваем по высоте, при равной высоте — по скорости
        if self.altitude == other.altitude:
            return self.velocity < other.velocity
        return self.altitude < other.altitude

    @classmethod
    def get_filter_aeroplanes(cls, aeroplanes: dict[str, Any]) -> list["PlaneInfo"]:
        """
        Transform data from opensky (key 'states')
        into list of objects PlaneInfo.
        """
        states = aeroplanes.get("states") or []
        result: list[PlaneInfo] = []

        for state in states:
            try:
                call_sign = state[1] or ""
                reg_country = state[2] or ""
                altitude = state[7] or 0.0
                velocity = state[9] or 0.0
            except IndexError:
                continue

            try:
                plane = cls(
                    call_sign=call_sign,
                    reg_country=reg_country,
                    velocity=velocity,
                    altitude=altitude,
                )
            except TypeError, ValueError:
                # skip incorrect data
                continue

            result.append(plane)

        return result

    def __str__(self) -> str:
        """String representation"""
        return f"{self.call_sign}, {self.reg_country}, {self.velocity}, {self.altitude}"
