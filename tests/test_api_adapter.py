import pytest
import requests

import src.APIAdapter as api_clients
from src.APIAdapter import APIAdapter


class MockResponse:
    def __init__(self, json_data, status_code=200):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data


def test_api_clients(monkeypatch) -> None:
    """Check working APIAdapter with mocked queries for 2 API."""

    url_map = APIAdapter().openstreetmap_url
    url_sky = APIAdapter().opensky_url

    def mock_get(url, params=None, headers=None, timeout=10):
        if url == url_map:
            return MockResponse(
                json_data=[
                    {"boundingbox": ["10.0", "20.0", "30.0", "40.0"]},
                ],
                status_code=200,
            )
        if url == url_sky:
            return MockResponse(
                json_data={"states": [["plane1"], ["plane2"]]},
                status_code=200,
            )
        return MockResponse(json_data={}, status_code=400)

    # patch get function, imported from src.api_clients
    monkeypatch.setattr(api_clients, "get", mock_get)

    adapter = APIAdapter()
    adapter.get_aeroplanes("Russia")  # метод сам положит данные во внутренний атрибут

    data = adapter.aeroplanes
    assert isinstance(data, dict)
    assert "states" in data
    assert len(data["states"]) == 2