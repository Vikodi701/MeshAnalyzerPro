"""
MeshAnalyzer Pro
PDF Image Tools
"""

from pathlib import Path


class ImageExporter:

    def __init__(self, output_folder):
        self.output_folder = Path(output_folder)
        self.output_folder.mkdir(parents=True, exist_ok=True)

    def heatmap_path(self):
        return self.output_folder / "heatmap.jpg"

    def contour_path(self):
        return self.output_folder / "topographic.jpg"

    def surface_path(self):
        return self.output_folder / "surface3d.jpg"

    def export_from_report(self, report):
        heatmap = self.heatmap_path()
        contour = self.contour_path()
        surface = self.surface_path()

        report.save_heatmap_jpeg(str(heatmap))
        report.save_contour_jpeg(str(contour))
        report.save_surface_jpeg(str(surface))

        return {
            "heatmap": heatmap,
            "contour": contour,
            "surface": surface,
        }