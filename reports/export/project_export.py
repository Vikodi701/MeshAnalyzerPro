"""
MeshAnalyzer Pro
Project Export Service
"""

from pathlib import Path
import json


class ProjectExportService:

    def __init__(self, mesh):
        self.mesh = mesh

    def export_mesh_csv(self, output_folder):
        output = Path(output_folder)
        output.mkdir(parents=True, exist_ok=True)

        filename = output / "Mesh.csv"

        with open(filename, "w", encoding="utf-8") as file:
            for row in self.mesh.values:
                file.write(",".join(str(v) for v in row))
                file.write("\n")

        return filename

    def export_mesh_json(self, output_folder):
        output = Path(output_folder)
        output.mkdir(parents=True, exist_ok=True)

        filename = output / "Mesh.json"

        data = {
            "name": self.mesh.name,
            "filename": self.mesh.filename,
            "rows": self.mesh.rows,
            "cols": self.mesh.cols,
            "values": self.mesh.values,
        }

        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

        return filename