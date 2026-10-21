class PlaneInfo:
    """Class for Planes information"""

    call_sign: str
    reg_country: str
    velocity: float
    altitude: float

    def __init__(self, call_sign: str, reg_country: str, velocity: float, altitude: float) -> None:
        self.reg_country = reg_country
        self.call_sign = call_sign
        self.velocity = velocity
        self.altitude = altitude

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
            raise ValueError(f"{field_name} не может быть отрицательной")
        return float(value)