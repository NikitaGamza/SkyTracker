class PlaneInfo:
    """Class for Planes information"""

    call_sign: str
    reg_country: str
    velocity: float
    altitude: float

    def __init__(self, call_sign: str, reg_country: str, velocity: float, altitude: float) -> None:
        self.call_sign = self.__validate_string(call_sign, "call_sign is empty")
        self.reg_country = self.__validate_string(reg_country, "reg_country is empty")
        self.velocity = self.__validate_number(velocity, "velocity", "velocity is not number")
        self.altitude = self.__validate_number(altitude, "altitude", "altitude is not number")

    # ===========> Private methods for checking data <===========

    def __validate_string(self, value: str, error_msg: str) -> str:
        """Checking not empty string"""
        if isinstance(value, str):
            if value := value.strip():
                return value
        raise ValueError(error_msg)

    def __validate_number(self, value: float, field_name: str, type_error_msg: str) -> float:
        """Checking numbers"""
        if not isinstance(value, (int, float)):
            raise TypeError(type_error_msg)
        if value < 0:
            raise ValueError(f"{field_name} cannot be negative")
        return float(value)

    def __str__(self) -> str:
        """String representation"""
        return f"{self.call_sign}, {self.reg_country}, {self.velocity}, {self.altitude}"