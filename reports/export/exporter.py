"""
MeshAnalyzer Pro
Modular Export Manager
"""

from pathlib import Path

from reports.export.image_export import ImageExportService
from reports.export.pdf_export import PDFExportService
from reports.export.project_export import ProjectExportService


class Exporter:

    def __init__(self, mesh):
        self.mesh = mesh

        self.image_export = ImageExportService(mesh)
        self.pdf_export = PDFExportService(mesh)
        self.project_export = ProjectExportService(mesh)

    def export_all(self, output_folder):
        output = Path(output_folder)
        output.mkdir(parents=True, exist_ok=True)

        exported = {}

        exported["pdf"] = self.pdf_export.export(output)
        exported["images"] = self.image_export.export(output)
        exported["mesh_csv"] = self.project_export.export_mesh_csv(output)
        exported["mesh_json"] = self.project_export.export_mesh_json(output)

        return exported