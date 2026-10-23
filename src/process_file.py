import json
from typing import Any

from src.BaseProcess import BaseProcess


class Processing(BaseProcess):
    """Class to save data in JSON format"""

    def _read_all(self) -> list[dict[str, Any]]:
        if not self.file_path.exists():
            return []
        with self.file_path.open("r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
        if not isinstance(data, list):
            return []
        return data

    def _write_all(self, data: list[dict[str, Any]]) -> None:
        with self.file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add_aeroplane(self, aeroplane_data: dict[str, Any]) -> None:
        """Add record into planes file with avoiding doubles"""
        data = self._read_all()

        callsign = aeroplane_data.get("callsign")
        reg_country = aeroplane_data.get("reg_country")

        # Check if plane is already in file
        for item in data:
            if item.get("callsign") == callsign and item.get("reg_country") == reg_country:
                return

        data.append(aeroplane_data)
        self._write_all(data)

    def get_aeroplanes(self, **criteria: Any) -> list[dict[str, Any]]:
        """
        Get filtered planes by criteria
        """
        data = self._read_all()

        reg_country = criteria.get("reg_country")
        min_altitude = criteria.get("min_altitude")
        max_altitude = criteria.get("max_altitude")

        result: list[dict[str, Any]] = []

        for item in data:
            ok = True

            if reg_country is not None:
                if str(item.get("reg_country", "")).lower() != str(reg_country).lower():
                    ok = False

            altitude = item.get("altitude")
            if min_altitude is not None and altitude is not None:
                if altitude < min_altitude:
                    ok = False
            if max_altitude is not None and altitude is not None:
                if altitude > max_altitude:
                    ok = False

            if ok:
                result.append(item)

        return result
