import pytest

from src.PlaneInfo import PlaneInfo


@pytest.fixture()
def fix_obj_aeroplane() -> PlaneInfo:
    """return class object PlaneInfo"""
    return PlaneInfo("BORT_007", "Canada", 250.4, 12545.5)


@pytest.fixture()
def fix_init_aeroplane() -> dict:
    """fixture for init plane"""
    return {
        "call_sign": "BOING_001",
        "reg_country": "USA",
        "velocity": 200.5,
        "altitude": 14444.5,
    }


@pytest.fixture()
def fix_list_aeroplanes() -> list[PlaneInfo]:
    return [
        PlaneInfo("UAE41P", "United Arab Emirates", 73.14, 68.58),
        PlaneInfo("GFA2004", "Bahrain", 555.57, 4145.28),
        PlaneInfo("FAD437", "Saudi Arabia", 139.49, 1569.72),
    ]