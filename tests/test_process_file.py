from src.process_file import Processing


def test_get_aeroplanes_filters_by_country(tmp_path):
    # Use temporary file
    file_path = tmp_path / "planes.json"
    storage = Processing()
    storage._file_path = file_path  # reset attribute - path to file inly in test

    storage.add_aeroplane({"call_sign": "BOING_001", "reg_country": "Canada", "velocity": 200.5, "altitude": 14444.5})
    storage.add_aeroplane({"call_sign": "BOING_002", "reg_country": "Russia", "velocity": 210.0, "altitude": 12000.0})

    result = storage.get_aeroplanes(reg_country="Canada")

    assert isinstance(result, list)
    assert len(result) == 1
    plane = result[0]
    assert plane["call_sign"] == "BOING_001"
    assert plane["reg_country"] == "Canada"


def test_get_aeroplanes_filters_by_altitude(tmp_path):
    file_path = tmp_path / "planes.json"
    storage = Processing()
    storage._file_path = file_path

    storage.add_aeroplane({"call_sign": "LOW", "reg_country": "Iran", "velocity": 180.0, "altitude": 9000.0})
    storage.add_aeroplane({"call_sign": "MID", "reg_country": "Iran", "velocity": 190.0, "altitude": 12000.0})
    storage.add_aeroplane({"call_sign": "HIGH", "reg_country": "Iran", "velocity": 200.0, "altitude": 16000.0})

    result = storage.get_aeroplanes(reg_country="Iran", min_altitude=10000, max_altitude=15000)

    assert len(result) == 1
    assert result[0]["call_sign"] == "MID"