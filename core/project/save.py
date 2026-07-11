"""
MeshAnalyzer Pro
Project Save Engine v3
.meshproj tam proje paketi
"""

import json
import zipfile
import tempfile
from pathlib import Path

from core.project.serializer import ProjectSerializer
from reports.pdf_report import PDFReport
from core.smart_diagnostic.health import HealthScore
from core.smart_diagnostic.report import SmartDiagnosticReport
from core.trend.analyzer import TrendAnalyzer
from core.config import Config


class ProjectSaver:

    def __init__(self):
        self.serializer = ProjectSerializer()
        self.config = Config()

    def save(self, mesh, filename):
        filename = Path(filename)

        if filename.suffix.lower() != ".meshproj":
            filename = filename.with_suffix(".meshproj")

        project_data = self.serializer.create_project_data(mesh)

        with tempfile.TemporaryDirectory() as temp_dir:
            temp_path = Path(temp_dir)

            report = PDFReport(mesh)

            heatmap_path = temp_path / "heatmap.jpg"
            contour_path = temp_path / "contour.jpg"
            surface_path = temp_path / "surface3d.jpg"
            report_path = temp_path / "report.pdf"

            report.save_heatmap_jpeg(str(heatmap_path))
            report.save_contour_jpeg(str(contour_path))
            report.save_surface_jpeg(str(surface_path))
            report.save(str(report_path))

            with zipfile.ZipFile(filename, "w", zipfile.ZIP_DEFLATED) as z:

                z.writestr(
                    "project.json",
                    json.dumps(project_data, indent=4, ensure_ascii=False)
                )

                z.writestr(
                    "settings.json",
                    json.dumps(self.config.load(), indent=4, ensure_ascii=False)
                )

                z.writestr(
                    "health_score.json",
                    json.dumps(
                        HealthScore(mesh).calculate(),
                        indent=4,
                        ensure_ascii=False
                    )
                )

                z.writestr(
                    "smart_diagnostic.txt",
                    SmartDiagnosticReport(mesh).generate()
                )

                z.writestr(
                    "trend_report.txt",
                    TrendAnalyzer().report_text()
                )

                z.writestr(
                    "meshes/current_mesh.json",
                    json.dumps(
                        self.serializer.mesh_to_dict(mesh),
                        indent=4,
                        ensure_ascii=False
                    )
                )

                z.write(report_path, "report.pdf")
                z.write(heatmap_path, "images/heatmap.jpg")
                z.write(contour_path, "images/contour.jpg")
                z.write(surface_path, "images/surface3d.jpg")
                z.write(heatmap_path, "images/preview.jpg")

        return str(filename)