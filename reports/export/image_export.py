"""
MeshAnalyzer Pro
Image Export Service
"""

from pathlib import Path

from reports.pdf_report import PDFReport


class ImageExportService:

    def __init__(self, mesh):
        self.mesh = mesh
        self.report = PDFReport(mesh)

    def export(self, output_folder):
        output = Path(output_folder)
        output.mkdir(parents=True, exist_ok=True)

        files = {
            "heatmap": output / "Heatmap.jpg",
            "topographic": output / "Topographic.jpg",
            "surface3d": output / "Surface3D.jpg",
        }

        self.report.save_heatmap_jpeg(str(files["heatmap"]))
        self.report.save_contour_jpeg(str(files["topographic"]))
        self.report.save_surface_jpeg(str(files["surface3d"]))

        return files