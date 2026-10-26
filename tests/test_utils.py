from src.PlaneInfo import PlaneInfo
from src.utils import (filter_aeroplanes, get_top_aeroplanes, load_aeroplanes_by_country,
                       sort_aeroplanes)


def test_load_aeroplanes_by_country():
    """Test load planes by country with empty arguments"""
    # Arrange
    country = ""

    # Act
    result = load_aeroplanes_by_country(country)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 0


def test_filter_aeroplanes(fix_list_aeroplanes):
    """Test filter planes by country"""
    # Arrange
    countries = ["Saudi Arabia"]

    # Act
    result = filter_aeroplanes(fix_list_aeroplanes, countries)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 1

    plane = result[0]
    assert isinstance(plane, PlaneInfo)
    assert plane.reg_country == "Saudi Arabia"
    assert plane.call_sign == "FAD437"


def test_sort_aeroplanes(fix_list_aeroplanes):
    """Тест сортировки самолетов"""
    # Arrange
    # fix_list_aeroplanes is in fixture

    # Act
    result = sort_aeroplanes(fix_list_aeroplanes)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 3
    assert result[0].reg_country == "Bahrain"


def test_get_top_aeroplanes(fix_list_aeroplanes):
    """Тест получения топ N самолетов"""
    # Arrange
    limit = 2

    # Act
    result = get_top_aeroplanes(fix_list_aeroplanes, limit)

    # Assert
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0].reg_country == "United Arab Emirates"