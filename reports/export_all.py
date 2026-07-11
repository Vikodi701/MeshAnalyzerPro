"""
MeshAnalyzer Pro
Export All Engine
Compatibility Wrapper
"""

from reports.export.exporter import Exporter


class ExportAll:
    """
    Eski API'yi koruyan uyumluluk katmanı.

    Eski kullanım:

        ExportAll(mesh).save(folder)

    Yeni sistem:

        Exporter(mesh).export_all(folder)
    """

    def __init__(self, mesh):
        self.exporter = Exporter(mesh)

    def save(self, folder):
        return self.exporter.export_all(folder)