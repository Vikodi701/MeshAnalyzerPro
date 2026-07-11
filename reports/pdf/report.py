"""
MeshAnalyzer Pro
Modular PDF Report Entry Point
"""

from reports.pdf.summary import SummaryBuilder
from reports.pdf.tables import TableBuilder
from reports.pdf.charts import ChartBuilder
from reports.pdf.images import ImageExporter


class PDFReport:

    def __init__(self, analysis_result):
        self.analysis = analysis_result

        self.summary_builder = SummaryBuilder()
        self.table_builder = TableBuilder()
        self.chart_builder = ChartBuilder()

    def build(self, output_file):
        """
        PDF oluşturma akışı:

        1. Özet
        2. Tablolar
        3. Grafikler
        4. Görseller

        Bu sınıf Sprint 2.2 içinde aşamalı olarak doldurulacak.
        """

        raise NotImplementedError(
            "Modular PDF builder henüz tamamlanmadı."
        )