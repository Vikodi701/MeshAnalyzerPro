"""
MeshAnalyzer Pro
PDF Export Service
"""

from pathlib import Path

from reports.pdf_report import PDFReport


class PDFExportService:

    def __init__(self, mesh):
        self.mesh = mesh
        self.report = PDFReport(mesh)

    def export(self, output_folder):
        output = Path(output_folder)
        output.mkdir(parents=True, exist_ok=True)

        filename = output / "Report.pdf"

        self.report.save(str(filename))

        return filename