"""
MeshAnalyzer Pro
Project Validator v3
"""

import zipfile
from pathlib import Path


class ProjectValidator:

    REQUIRED_FILES = [
        "project.json",
        "settings.json",
        "meshes/current_mesh.json",
    ]

    OPTIONAL_FILES = [
        "report.pdf",
        "smart_diagnostic.txt",
        "trend_report.txt",
        "health_score.json",
        "images/heatmap.jpg",
        "images/contour.jpg",
        "images/surface3d.jpg",
        "images/preview.jpg",
    ]

    def validate(self, filename):
        filename = Path(filename)

        if not filename.exists():
            return False, "Dosya bulunamadı."

        if filename.suffix.lower() != ".meshproj":
            return False, "Dosya uzantısı .meshproj değil."

        try:
            with zipfile.ZipFile(filename, "r") as z:
                names = z.namelist()

                for required in self.REQUIRED_FILES:
                    if required not in names:
                        return False, f"Eksik proje içeriği: {required}"

        except zipfile.BadZipFile:
            return False, "Geçersiz proje dosyası."

        return True, "Geçerli proje dosyası."