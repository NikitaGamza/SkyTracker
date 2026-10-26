import pytest

from src.PlaneInfo import PlaneInfo


def test_init_object(fix_obj_aeroplane: PlaneInfo, fix_init_aeroplane: dict) -> None:
    """Check creating object of PlaneInfo class"""
    # checking attribute
    assert fix_obj_aeroplane.call_sign == "BORT_007"
    assert fix_obj_aeroplane.reg_country == "Canada"
    assert fix_obj_aeroplane.velocity == 250.4
    assert fix_obj_aeroplane.altitude == 12545.5

    # Checking initialization
    test_obj = PlaneInfo(**fix_init_aeroplane)

    assert isinstance(test_obj, PlaneInfo)

    assert test_obj.call_sign == "BOING_001"
    assert test_obj.reg_country == "USA"
    assert test_obj.velocity == 200.5
    assert test_obj.altitude == 14444.5

    # Checking data types
    assert isinstance(fix_obj_aeroplane.call_sign, str)
    assert isinstance(fix_obj_aeroplane.reg_country, str)
    assert isinstance(fix_obj_aeroplane.velocity, float)
    assert isinstance(fix_obj_aeroplane.altitude, float)

    # checking methods
    result = test_obj.get_filter_aeroplanes(fix_init_aeroplane)
    assert isinstance(result, list)
    assert len(result) == 0
    assert result == []
    assert test_obj.__eq__(fix_obj_aeroplane) is False
    assert test_obj.__lt__(fix_obj_aeroplane) is False


@pytest.mark.parametrize(
    "call_sign, reg_country, velocity, altitude",
    [
        (1, "Canada", 250.4, 12545.5),           # call_sign not str
        ("BORT_007", 1, 250.4, 12545.5),         # reg_country not str
        ("BORT_007", "Canada", -345, 12545.5),   # velocity under 0
        ("BORT_007", "Canada", 250.4, -2345.7),  # altitude under 0
        ("BORT_007", "Canada", "123", 12545.5),  # velocity not int
        ("BORT_007", "Canada", 250.4, "123"),    # altitude not int
    ]
)
def test_init_invalid_types_raises(
    call_sign: str,
    reg_country: str,
    velocity: float,
    altitude: float
) -> None:
    """Checking call sign raises exception."""
    with pytest.raises((TypeError, ValueError)):
        PlaneInfo(call_sign, reg_country, velocity, altitude)  # type: ignore[arg-type]


def test_aeroplane_str(fix_init_aeroplane: dict) -> None:
    obj = PlaneInfo(**fix_init_aeroplane)
    assert str(obj) == "BOING_001, USA, 200.5, 14444.5"