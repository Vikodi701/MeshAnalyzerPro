"""
MeshAnalyzer Pro
Configuration Manager
"""

import json
from pathlib import Path


class Config:

    DEFAULT = {

        "max_total_range": 0.600,

        "max_rms": 0.250,

        "max_plane_deviation": 0.300,

        "theme": "dark",

        "default_heatmap_palette": "turbo",

        "default_topography_palette": "terrain",

        "default_surface_palette": "turbo",

        "default_surface_view": "default",

        "report_include_graphs": True,

        "report_include_diagnostics": True,

        "report_include_mesh_table": True,

        "export_jpg_show_cell_values": True,

        "appearance_show_table_values": True,

        "appearance_show_colorbar": True,

        "appearance_show_hover_info": True,

        "appearance_start_maximized": True,

        "language": "tr"

    }

    def __init__(self):

        self.folder = Path("config")
        self.folder.mkdir(exist_ok=True)

        self.file = self.folder / "config.json"

        if not self.file.exists():
            self.save(self.DEFAULT)

    def load(self):

        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f)

    def save(self, data):

        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(
                data,
                f,
                indent=4,
                ensure_ascii=False
            )

    def get(self, key):

        data = self.load()

        return data.get(
            key,
            self.DEFAULT.get(key)
        )

    def set(self, key, value):

        data = self.load()

        data[key] = value

        self.save(data)