"""
MeshAnalyzer Pro
PDF Report Engine v3
Language-aware PDF + JPG export
"""

from datetime import datetime
from io import BytesIO

import numpy as np
import matplotlib
import matplotlib.pyplot as plt

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors

from core.analysis import AnalysisEngine
from core.config import Config
from reports.pdf.utils import PDFCanvasUtils
from languages import LanguageManager


class PDFReport:

    def __init__(self, mesh):
        self.mesh = mesh
        self.config = Config()

        # Rapor çıktıları dil ayarına bağlı metin içerdiği için cache kullanmıyoruz.
        # Böylece dil değiştirildikten sonra PDF/JPG çıktıları eski dilde kalmaz.
        self.analysis = AnalysisEngine(mesh, use_cache=False).run()

        self.font_name = "DejaVuSans"
        self.font_bold = "DejaVuSans-Bold"

        self.register_fonts()

        self.utils = PDFCanvasUtils(
            self.font_name,
            self.font_bold
        )

    # -----------------------------------------------------
    # Language helpers
    # -----------------------------------------------------

    def text(self, key):
        return LanguageManager.text(key)

    def label(self, key, value):
        return f"{self.text(key)}: {value}"

    def setting_enabled(self, key, default=True):
        value = self.config.get(key)
        if value is None:
            return default
        return bool(value)

    def section_title(self, number, key):
        return f"{number}. {self.text(key)}"

    def health_summary_text(self):
        health = self.analysis.health
        status = str(health.status).strip().upper()

        if status in ("GOOD", "EXCELLENT", "OK", "PASS"):
            return self.text("report_summary_status_good")
        if status in ("WARNING", "WARN", "ACCEPTABLE"):
            return self.text("report_summary_status_warning")
        return self.text("report_summary_status_critical")

    def main_problem_text(self):
        tolerance = self.analysis.tolerance
        geo = self.analysis.geometry

        if str(tolerance.get("status", "")).strip().upper() == "FAIL":
            return self.text("report_summary_problem_tolerance")

        if abs(geo.max_deviation) >= 0.30:
            return self.text("report_summary_problem_plane")

        if abs(geo.x_slope) >= 0.20:
            return self.text("report_summary_problem_x_slope")

        if abs(geo.y_slope) >= 0.20:
            return self.text("report_summary_problem_y_slope")

        return self.text("report_summary_problem_none")

    def main_recommendation_text(self):
        recommendation = self.analysis.diagnostic.recommendation or {}

        name = recommendation.get("name")
        delta = recommendation.get("delta")

        if name is not None and delta is not None:
            return self.text("report_summary_recommendation_shim").format(
                name=name,
                delta=abs(float(delta))
            )

        return self.text("report_summary_recommendation_remeasure")

    def result_summary_lines(self):
        health = self.analysis.health
        tolerance = self.analysis.tolerance

        return [
            self.label("report_summary_general_status", self.health_summary_text()),
            self.label("report_summary_score", f"{health.score:.1f} / 100"),
            self.label("report_summary_tolerance", self.status_text(tolerance.get("status"))),
            self.label("report_summary_main_problem", self.main_problem_text()),
            self.label("report_summary_recommended_action", self.main_recommendation_text()),
            self.text("dashboard_disclaimer").replace("<b>", "").replace("</b>", ""),
        ]

    def status_text(self, status):
        raw = str(status).strip().upper()
        keys = {
            "PASS": "status_pass",
            "OK": "status_ok",
            "EXCELLENT": "status_excellent",
            "GOOD": "status_good",
            "WARNING": "status_warning",
            "WARN": "status_warning",
            "ACCEPTABLE": "status_acceptable",
            "FAIL": "status_fail",
            "ERROR": "status_error",
            "BAD": "status_bad",
            "CRITICAL": "status_critical",
        }

        key = keys.get(raw)
        if not key:
            return str(status)

        translated = self.text(key)
        return translated if translated != key else str(status)

    # -----------------------------------------------------
    # Fonts
    # -----------------------------------------------------

    def register_fonts(self):
        font_path = matplotlib.get_data_path() + "/fonts/ttf/DejaVuSans.ttf"
        bold_path = matplotlib.get_data_path() + "/fonts/ttf/DejaVuSans-Bold.ttf"

        pdfmetrics.registerFont(TTFont(self.font_name, font_path))
        pdfmetrics.registerFont(TTFont(self.font_bold, bold_path))

    # -----------------------------------------------------
    # Matplotlib figures used by PDF and JPG exports
    # -----------------------------------------------------

    def create_heatmap_figure(self):
        data = self.mesh.matrix

        fig, ax = plt.subplots(figsize=(6, 5))
        image = ax.imshow(data, origin="lower", cmap="coolwarm")

        rows, cols = data.shape

        ax.set_xticks(range(cols))
        ax.set_yticks(range(rows))
        ax.set_xticklabels([f"X{i + 1}" for i in range(cols)])
        ax.set_yticklabels([f"Y{i + 1}" for i in range(rows)])

        if self.setting_enabled("export_jpg_show_cell_values", True):
            for y in range(rows):
                for x in range(cols):
                    ax.text(
                        x,
                        y,
                        f"{data[y, x]:.3f}",
                        ha="center",
                        va="center",
                        color="white",
                        fontsize=9,
                        fontweight="bold",
                    )

        ax.set_title(self.text("report_heatmap_title"))
        ax.set_xlabel(self.text("report_x_coordinate"))
        ax.set_ylabel(self.text("report_y_coordinate"))

        fig.colorbar(
            image,
            ax=ax,
            label=self.text("report_height_mm")
        )
        fig.tight_layout()

        return fig

    def create_contour_figure(self):
        data = self.mesh.matrix

        rows, cols = data.shape

        x = np.arange(1, cols + 1)
        y = np.arange(1, rows + 1)

        X, Y = np.meshgrid(x, y)

        fig, ax = plt.subplots(figsize=(6, 5))

        contour = ax.contourf(
            X,
            Y,
            data,
            levels=20,
            cmap="coolwarm"
        )

        lines = ax.contour(
            X,
            Y,
            data,
            levels=10,
            colors="black",
            linewidths=0.5,
        )

        ax.clabel(lines, inline=True, fontsize=8)

        ax.set_title(self.text("report_topography_title"))
        ax.set_xlabel(self.text("report_x_coordinate"))
        ax.set_ylabel(self.text("report_y_coordinate"))

        ax.set_xticks(x)
        ax.set_yticks(y)

        fig.colorbar(
            contour,
            ax=ax,
            label=self.text("report_height_mm")
        )
        fig.tight_layout()

        return fig

    def create_surface_figure(self):
        data = self.mesh.matrix

        rows, cols = data.shape

        x = np.arange(1, cols + 1)
        y = np.arange(1, rows + 1)

        X, Y = np.meshgrid(x, y)

        fig = plt.figure(figsize=(6, 5))
        ax = fig.add_subplot(111, projection="3d")

        surface = ax.plot_surface(
            X,
            Y,
            data,
            cmap="coolwarm",
            edgecolor="black",
            linewidth=0.4,
            antialiased=True,
        )

        ax.set_title(self.text("report_surface_title"))
        ax.set_xlabel(self.text("report_x_coordinate"))
        ax.set_ylabel(self.text("report_y_coordinate"))
        ax.set_zlabel(self.text("report_height_mm"))

        ax.set_xticks(x)
        ax.set_yticks(y)

        fig.colorbar(
            surface,
            ax=ax,
            shrink=0.6,
            label=self.text("report_height_mm"),
        )

        fig.tight_layout()

        return fig

    def figure_to_reader(self, fig):
        buffer = BytesIO()
        fig.savefig(buffer, format="png", dpi=160)
        plt.close(fig)
        buffer.seek(0)
        return ImageReader(buffer)

    # -----------------------------------------------------
    # Standalone JPG exports
    # -----------------------------------------------------

    def save_heatmap_jpeg(self, filename):
        fig = self.create_heatmap_figure()
        fig.savefig(filename, format="jpg", dpi=220, bbox_inches="tight")
        plt.close(fig)

    def save_contour_jpeg(self, filename):
        fig = self.create_contour_figure()
        fig.savefig(filename, format="jpg", dpi=220, bbox_inches="tight")
        plt.close(fig)

    def save_surface_jpeg(self, filename):
        fig = self.create_surface_figure()
        fig.savefig(filename, format="jpg", dpi=220, bbox_inches="tight")
        plt.close(fig)

    # -----------------------------------------------------
    # Mesh table
    # -----------------------------------------------------

    def draw_mesh_table_5x5(self, c, y):
        """
        PDF raporun Mesh Tablosu bölümünü koordinat başlıklarıyla çizer.

        Koordinat standardı:
        - Sol Ön  = X1 / Y1
        - Sağ Ön  = Xmax / Y1
        - Sol Arka = X1 / Ymax
        - Sağ Arka = Xmax / Ymax

        PDF tablosunda üst satır arka tarafı gösterecek şekilde
        Ymax'tan Y1'e doğru yazılır.
        """
        width, height = A4

        values = self.mesh.values
        total_rows = len(values)
        total_cols = len(values[0]) if total_rows else 0

        row_count = min(5, total_rows)
        col_count = min(5, total_cols)

        if row_count == 0 or col_count == 0:
            c.setFont(self.font_name, 10)
            c.drawString(50, y, "-")
            return y - 20

        row_header_w = 42
        cell_w = 82
        cell_h = 34
        header_h = 28

        table_w = row_header_w + (cell_w * col_count)
        table_h = header_h + (cell_h * row_count)

        x0 = (width - table_w) / 2
        y_top = y - 8

        if y_top - table_h < 60:
            c.showPage()
            y_top = height - 70

        # Koordinat standardı notu
        c.setFont(self.font_name, 8)
        c.setFillColor(colors.HexColor("#475569"))
        c.drawString(
            x0,
            y_top + 8,
            self.text("report_mesh_table_coordinate_note")
        )

        # Genel tablo zemini
        c.setLineWidth(0.7)
        c.setStrokeColor(colors.HexColor("#475569"))
        c.setFillColor(colors.HexColor("#F8FAFC"))
        c.rect(x0, y_top - table_h, table_w, table_h, fill=1, stroke=1)

        # Sol üst boş koordinat hücresi
        c.setFillColor(colors.HexColor("#E2E8F0"))
        c.rect(
            x0,
            y_top - header_h,
            row_header_w,
            header_h,
            fill=1,
            stroke=1
        )

        c.setFont(self.font_bold, 8)
        c.setFillColor(colors.HexColor("#0F172A"))
        corner_text = "Y / X"
        c.drawString(
            x0 + (row_header_w - c.stringWidth(corner_text, self.font_bold, 8)) / 2,
            y_top - (header_h / 2) - 3,
            corner_text
        )

        # X koordinat başlıkları
        for col in range(col_count):
            x = x0 + row_header_w + (col * cell_w)

            c.setFillColor(colors.HexColor("#E2E8F0"))
            c.setStrokeColor(colors.HexColor("#CBD5E1"))
            c.rect(x, y_top - header_h, cell_w, header_h, fill=1, stroke=1)

            header_text = f"X{col + 1}"
            text_width = c.stringWidth(header_text, self.font_bold, 8)

            c.setFont(self.font_bold, 8)
            c.setFillColor(colors.HexColor("#0F172A"))
            c.drawString(
                x + (cell_w - text_width) / 2,
                y_top - (header_h / 2) - 3,
                header_text
            )

        # Y başlıkları ve değer hücreleri
        for r in range(row_count):
            source_row = row_count - 1 - r
            y_coord = source_row + 1
            y_cell = y_top - header_h - ((r + 1) * cell_h)

            # Y koordinat başlığı
            c.setFillColor(colors.HexColor("#E2E8F0"))
            c.setStrokeColor(colors.HexColor("#CBD5E1"))
            c.rect(x0, y_cell, row_header_w, cell_h, fill=1, stroke=1)

            y_text = f"Y{y_coord}"
            c.setFont(self.font_bold, 8)
            c.setFillColor(colors.HexColor("#0F172A"))
            c.drawString(
                x0 + (row_header_w - c.stringWidth(y_text, self.font_bold, 8)) / 2,
                y_cell + (cell_h / 2) - 3,
                y_text
            )

            for col in range(col_count):
                x = x0 + row_header_w + (col * cell_w)

                c.setFillColor(colors.white)
                c.setStrokeColor(colors.HexColor("#CBD5E1"))
                c.rect(x, y_cell, cell_w, cell_h, fill=1, stroke=1)

                value_text = f"{values[source_row][col]:+.4f}"
                c.setFont(self.font_name, 8)
                text_width = c.stringWidth(value_text, self.font_name, 8)

                c.setFillColor(colors.black)
                c.drawString(
                    x + (cell_w - text_width) / 2,
                    y_cell + (cell_h / 2) - 3,
                    value_text,
                )

        return y_top - table_h - 25

    # -----------------------------------------------------
    # PDF export
    # -----------------------------------------------------

    def save(self, filename):
        c = canvas.Canvas(filename, pagesize=A4)

        width, height = A4
        y = height - 50

        c.setFont(self.font_bold, 20)
        c.drawString(50, y, self.text("report_title"))
        y -= 35

        c.setFont(self.font_name, 10)
        c.drawString(
            50,
            y,
            self.label(
                "report_date",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ),
        )
        y -= 18

        c.drawString(
            50,
            y,
            self.label("report_file", self.mesh.name)
        )
        y -= 35

        y = self.utils.draw_title(
            c,
            self.section_title(1, "report_result_summary_section"),
            y
        )

        y = self.utils.draw_text_lines(
            c,
            self.result_summary_lines(),
            50,
            y,
            17,
            10
        )
        y -= 20

        y = self.utils.draw_title(
            c,
            self.section_title(2, "report_mesh_summary_section"),
            y
        )

        summary = [
            self.label("mesh_size", f"{self.mesh.rows} x {self.mesh.cols}"),
            self.label("minimum", f"{self.mesh.minimum:.4f} mm"),
            self.label("maximum", f"{self.mesh.maximum:.4f} mm"),
            self.label("average", f"{self.mesh.average:.4f} mm"),
            self.label("total_deviation", f"{self.mesh.total_range:.4f} mm"),
            self.label("standard_deviation", f"{self.mesh.std:.4f} mm"),
            f"RMS: {self.mesh.rms:.4f} mm",
        ]

        y = self.utils.draw_text_lines(c, summary, 50, y, 17, 11)
        y -= 20

        geo = self.analysis.geometry

        y = self.utils.draw_title(
            c,
            self.section_title(3, "report_geometry_section"),
            y
        )

        geometry_lines = [
            self.label("plane_max_deviation", f"{geo.max_deviation:.4f} mm"),
            self.label("plane_rms_deviation", f"{geo.rms_deviation:.4f} mm"),
            self.label("x_slope", f"{geo.x_slope:.4f} mm"),
            self.label("y_slope", f"{geo.y_slope:.4f} mm"),
        ]

        y = self.utils.draw_text_lines(c, geometry_lines, 50, y, 17, 11)
        y -= 20

        health = self.analysis.health

        y = self.utils.draw_title(
            c,
            self.section_title(4, "report_machine_health_section"),
            y
        )

        health_lines = [
            self.label("report_score", f"{health.score:.1f} / 100"),
            self.label("report_status", self.status_text(health.status)),
            self.label("report_category", self.status_text(health.status)),
        ]

        y = self.utils.draw_text_lines(c, health_lines, 50, y, 17, 11)
        y -= 20

        section_no = 5

        if self.setting_enabled("report_include_graphs", True):
            if y < 360:
                c.showPage()
                y = height - 50

            y = self.utils.draw_title(
                c,
                self.section_title(section_no, "report_heatmap_section"),
                y
            )
            section_no += 1

            heatmap = self.figure_to_reader(
                self.create_heatmap_figure()
            )

            c.drawImage(
                heatmap,
                55,
                y - 300,
                width=480,
                height=300,
                preserveAspectRatio=True,
                mask="auto",
            )

            y -= 330

            if y < 360:
                c.showPage()
                y = height - 50

            y = self.utils.draw_title(
                c,
                self.section_title(section_no, "report_topography_section"),
                y
            )
            section_no += 1

            contour = self.figure_to_reader(
                self.create_contour_figure()
            )

            c.drawImage(
                contour,
                55,
                y - 300,
                width=480,
                height=300,
                preserveAspectRatio=True,
                mask="auto",
            )

            y -= 330

            if y < 360:
                c.showPage()
                y = height - 50

            y = self.utils.draw_title(
                c,
                self.section_title(section_no, "report_surface_section"),
                y
            )
            section_no += 1

            surface = self.figure_to_reader(
                self.create_surface_figure()
            )

            c.drawImage(
                surface,
                55,
                y - 300,
                width=480,
                height=300,
                preserveAspectRatio=True,
                mask="auto",
            )

            y -= 330

        if self.setting_enabled("report_include_diagnostics", True):
            if y < 120:
                c.showPage()
                y = height - 50

            y = self.utils.draw_report_block(
                c,
                self.section_title(section_no, "report_smart_diagnostic_section"),
                self.analysis.smart_report,
                y,
            )
            section_no += 1

            diagnostic_lines = self.analysis.diagnostic_report

            y = self.utils.draw_report_block(
                c,
                self.section_title(section_no, "report_mechanical_diagnostic_section"),
                "\n".join(diagnostic_lines),
                y,
            )
            section_no += 1

        if self.setting_enabled("report_include_mesh_table", True):
            if y < 180:
                c.showPage()
                y = height - 50

            y = self.utils.draw_title(
                c,
                self.section_title(section_no, "report_mesh_table_section"),
                y
            )

            y = self.draw_mesh_table_5x5(c, y)

        c.save()
