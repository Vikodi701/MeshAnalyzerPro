"""
MeshAnalyzer Pro
Project Load Engine v3
.meshproj tam proje paketi açma
"""

import json
import zipfile
from pathlib import Path

from core.mesh import Mesh
from core.config import Config


class ProjectLoader:

    def __init__(self):
        self.config = Config()

    def load(self, filename):
        filename = Path(filename)

        if not filename.exists():
            raise FileNotFoundError("Proje dosyası bulunamadı.")

        with zipfile.ZipFile(filename, "r") as z:

            names = z.namelist()

            if "project.json" not in names:
                raise ValueError("Geçersiz proje dosyası: project.json yok.")

            data = json.loads(
                z.read("project.json").decode("utf-8")
            )

            if "meshes/current_mesh.json" in names:
                mesh_data = json.loads(
                    z.read("meshes/current_mesh.json").decode("utf-8")
                )
            else:
                mesh_data = data["mesh"]

            if "settings.json" in names:
                settings = json.loads(
                    z.read("settings.json").decode("utf-8")
                )
                self.config.save(settings)

        mesh = Mesh(
            name=mesh_data["name"],
            filename=mesh_data["filename"],
            values=mesh_data["values"],
        )

        return mesh