"""
MeshAnalyzer Pro
core/parser.py
"""

from pathlib import Path
import csv
import json
import re
import math
import pyzipper

from core.mesh import Mesh


class MeshParser:
    PACK_PASSWORD = (
        b"2YLVrATRvUEnMeXk6Vtc7qxfzYM4TJzrLnEBma8zpUKeGtseGWqp4LXs7e8KeU2u"
    )

    def load(self, filename: str) -> Mesh:
        path = Path(filename)
        suffix = path.suffix.lower()

        if suffix == ".pack":
            return self._load_pack(path)

        if suffix == ".csv":
            return self._load_csv(path)

        if suffix == ".txt":
            return self._load_txt(path)

        if suffix == ".json":
            return self._load_json(path)

        raise ValueError(f"Desteklenmeyen dosya türü: {suffix}")

    def validate_values(self, values, source="mesh"):
        if values is None:
            raise ValueError("Mesh verisi bulunamadı.")

        if not isinstance(values, list) or not values:
            raise ValueError("Mesh verisi boş.")

        if not all(isinstance(row, list) for row in values):
            raise ValueError("Mesh verisi satır listelerinden oluşmalıdır.")

        row_lengths = [
            len(row)
            for row in values
        ]

        if not row_lengths or min(row_lengths) == 0:
            raise ValueError("Mesh içinde boş satır var.")

        if len(set(row_lengths)) != 1:
            raise ValueError(
                "Mesh satır uzunlukları eşit değil. "
                "Tüm satırlar aynı sütun sayısına sahip olmalı."
            )

        rows = len(values)
        cols = row_lengths[0]

        if rows < 2 or cols < 2:
            raise ValueError(
                "Mesh en az 2 satır ve 2 sütundan oluşmalıdır."
            )

        validated = []

        for row_index, row in enumerate(values, start=1):
            validated_row = []

            for col_index, raw_value in enumerate(row, start=1):
                try:
                    value = float(raw_value)
                except Exception:
                    raise ValueError(
                        f"Geçersiz sayı: satır {row_index}, sütun {col_index}."
                    )

                if not math.isfinite(value):
                    raise ValueError(
                        f"Geçersiz sayı: satır {row_index}, sütun {col_index}."
                    )

                validated_row.append(value)

            validated.append(validated_row)

        flat = [
            value
            for row in validated
            for value in row
        ]

        if max(flat) - min(flat) > 10:
            raise ValueError(
                "Mesh değer aralığı olağan dışı büyük görünüyor. "
                "Dosya birimi veya formatı kontrol edilmeli."
            )

        return validated

    def make_mesh(self, path: Path, values):
        return Mesh(
            name=path.stem,
            filename=str(path),
            values=self.validate_values(values, str(path)),
        )

    def _load_pack(self, path: Path) -> Mesh:
        with pyzipper.AESZipFile(path) as z:
            z.setpassword(self.PACK_PASSWORD)

            target = None

            for name in z.namelist():
                if name.endswith("printer_mutable.cfg"):
                    target = name
                    break

            if target is None:
                raise FileNotFoundError("printer_mutable.cfg bulunamadı.")

            text = z.read(target).decode("utf-8", errors="ignore")

        return self._parse_anycubic_cfg(text, path)

    def _parse_anycubic_cfg(self, text: str, path: Path) -> Mesh:
        pattern = r'"points"\s*:\s*"(.+?)"'
        match = re.search(pattern, text, re.DOTALL)

        if not match:
            raise ValueError("Mesh points alanı bulunamadı.")

        raw = match.group(1)
        raw = raw.replace("\\n", "\n")

        values = []

        for line in raw.splitlines():
            line = line.strip()

            if not line:
                continue

            values.append([float(x.strip()) for x in line.split(",")])

        return self.make_mesh(path, values)

    def _load_csv(self, path: Path) -> Mesh:
        values = []

        with open(path, newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            for row in reader:
                if row:
                    values.append([float(x.strip()) for x in row])

        return self.make_mesh(path, values)

    def _load_txt(self, path: Path) -> Mesh:
        values = []

        with open(path, encoding="utf-8") as file:
            for line in file:
                line = line.strip()

                if line:
                    values.append([float(x.strip()) for x in line.split(",")])

        return self.make_mesh(path, values)

    def _load_json(self, path: Path) -> Mesh:
        with open(path, encoding="utf-8") as file:
            data = json.load(file)

        return Mesh(
            name=path.stem,
            filename=str(path),
            values=data["mesh"],
        )