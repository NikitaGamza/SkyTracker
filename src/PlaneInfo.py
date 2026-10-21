class PlaneInfo:
    """Class for Planes information"""

    country: str
    call_sign: str
    speed: float
    high: float

    def __init__(self, country: str, call_sign: str, speed: float, high: float) -> None:
        self.country = country
        self.call_sign = call_sign
        self.speed = speed
        self.high = high
