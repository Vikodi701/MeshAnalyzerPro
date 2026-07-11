"""
MeshAnalyzer Pro
Analysis Page
Readable AnalysisEngine view
"""

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QScrollArea,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from core.analysis import AnalysisEngine
from core.config import Config
from languages import LanguageManager
from gui.widgets.info_icon import InfoIcon


class AnalysisPage(QWidget):

    def __init__(self):
        super().__init__()

        self.current_mesh = None
        self.current_analysis = None

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(18, 18, 18, 18)
        main_layout.setSpacing(14)

        self.scroll = QScrollArea()
        self.scroll.setWidgetResizable(True)
        self.scroll.setFrameShape(QFrame.Shape.NoFrame)

        self.content = QWidget()
        self.content.setObjectName("AnalysisContent")

        self.layout = QVBoxLayout(self.content)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(14)

        self.header = QLabel()
        self.header.setObjectName("AnalysisHeader")
        self.layout.addWidget(self.header)

        self.summaryGrid = QGridLayout()
        self.summaryGrid.setSpacing(12)
        self.layout.addLayout(self.summaryGrid)

        self.statusCard = self.create_score_card("")
        self.healthCard = self.create_score_card("")
        self.timeCard = self.create_score_card("")

        self.summaryGrid.addWidget(self.statusCard, 0, 0)
        self.summaryGrid.addWidget(self.healthCard, 0, 1)
        self.summaryGrid.addWidget(self.timeCard, 0, 2)

        self.meshSection, self.meshGrid = self.create_metric_section("")
        self.geometrySection, self.geometryGrid = self.create_metric_section("")
        self.toleranceSection, self.toleranceGrid = self.create_metric_section("")

        self.overviewGrid = QGridLayout()
        self.overviewGrid.setSpacing(14)
        self.overviewGrid.addWidget(self.meshSection, 0, 0)
        self.overviewGrid.addWidget(self.toleranceSection, 0, 1)
        self.overviewGrid.setColumnStretch(0, 1)
        self.overviewGrid.setColumnStretch(1, 1)

        self.layout.addLayout(self.overviewGrid)
        self.layout.addWidget(self.geometrySection)

        self.trendText = self.create_text_section("")

        self.layout.addWidget(self.trendText["frame"])
        self.layout.addStretch()

        self.scroll.setWidget(self.content)
        main_layout.addWidget(self.scroll)

        self.show_empty_state()
        self.refresh_theme()


    def create_info_title_row(self, title_label, tooltip=""):
        row = QWidget()
        row.setObjectName("CardTitleRow")

        row_layout = QHBoxLayout(row)
        row_layout.setContentsMargins(0, 0, 0, 0)
        row_layout.setSpacing(6)

        info_icon = InfoIcon(tooltip)

        row_layout.addStretch()
        row_layout.addWidget(title_label)
        row_layout.addWidget(info_icon)
        row_layout.addStretch()

        return row, info_icon

    def show_empty_state(self):
        self.header.setText(
            LanguageManager.text("analysis_empty")
        )

        for card in (self.statusCard, self.healthCard, self.timeCard):
            self.set_score_card(
                card,
                "--",
                LanguageManager.text("waiting_result"),
                "neutral"
            )

        self.clear_grid(self.meshGrid)
        self.clear_grid(self.geometryGrid)
        self.clear_grid(self.toleranceGrid)

        for section in (self.trendText,):
            section["body"].setText(LanguageManager.text("waiting_result"))

    def create_score_card(self, title):
        frame = QFrame()
        frame.setObjectName("AnalysisScoreCard")
        frame.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Fixed
        )

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(14, 10, 14, 10)
        layout.setSpacing(5)

        title_label = QLabel(title)
        title_label.setObjectName("AnalysisCardTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_row, info_icon = self.create_info_title_row(title_label)

        value_label = QLabel("--")
        value_label.setObjectName("AnalysisCardValue")
        value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        footer_label = QLabel("")
        footer_label.setObjectName("AnalysisCardFooter")
        footer_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        footer_label.setWordWrap(True)

        layout.addWidget(title_row)
        layout.addWidget(value_label)
        layout.addWidget(footer_label)

        frame.titleLabel = title_label
        frame.infoIcon = info_icon
        frame.valueLabel = value_label
        frame.footerLabel = footer_label
        return frame

    def set_score_card(self, card, value, footer, status):
        card.valueLabel.setText(str(value))
        card.footerLabel.setText(str(footer))
        card.setProperty("status", status)
        card.style().unpolish(card)
        card.style().polish(card)

    def create_metric_section(self, title):
        frame = QFrame()
        frame.setObjectName("AnalysisSection")

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(14, 12, 14, 14)
        layout.setSpacing(8)

        title_label = QLabel(title)
        title_label.setObjectName("AnalysisSectionTitle")

        title_row, info_icon = self.create_info_title_row(title_label)
        layout.addWidget(title_row)

        grid = QGridLayout()
        grid.setHorizontalSpacing(10)
        grid.setVerticalSpacing(8)
        layout.addLayout(grid)

        frame.titleLabel = title_label
        frame.infoIcon = info_icon
        return frame, grid

    def add_metric(self, grid, row, col, label, value, status=None, col_span=1):
        item = QFrame()
        item.setObjectName("AnalysisMetric")
        item.setMinimumHeight(54)
        if status is not None:
            item.setProperty("status", status)

        layout = QVBoxLayout(item)
        layout.setContentsMargins(10, 6, 10, 6)
        layout.setSpacing(2)

        label_widget = QLabel(label)
        label_widget.setObjectName("AnalysisMetricLabel")
        label_widget.setWordWrap(True)

        value_widget = QLabel(str(value))
        value_widget.setObjectName("AnalysisMetricValue")
        value_widget.setWordWrap(True)

        layout.addWidget(label_widget)
        layout.addWidget(value_widget)

        grid.addWidget(item, row, col, 1, col_span)
        item.style().unpolish(item)
        item.style().polish(item)

    def clear_grid(self, grid):
        while grid.count():
            item = grid.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

    def create_text_section(self, title):
        frame = QFrame()
        frame.setObjectName("AnalysisSection")

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(16, 14, 16, 16)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName("AnalysisSectionTitle")

        title_row, info_icon = self.create_info_title_row(title_label)

        body = QTextEdit()
        body.setObjectName("AnalysisText")
        body.setReadOnly(True)
        body.setMinimumHeight(92)

        layout.addWidget(title_row)
        layout.addWidget(body)

        return {
            "frame": frame,
            "title": title_label,
            "info": info_icon,
            "body": body,
        }

    def status_kind(self, status):
        text = str(status).upper()
        if text in ("PASS", "OK", "GOOD"):
            return "good"

        if text in ("WARNING", "WARN"):
            return "warning"

        if text in ("FAIL", "ERROR", "BAD"):
            return "bad"

        return "neutral"

    def status_text(self, status):
        text = str(status).strip().upper()
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

        key = keys.get(text)
        if not key:
            return str(status)

        translated = LanguageManager.text(key)
        return translated if translated != key else str(status)

    def update_mesh(self, mesh):
        self.current_mesh = mesh
        analysis = AnalysisEngine(mesh).run()
        self.current_analysis = analysis

        geo = analysis.geometry
        tolerance = analysis.tolerance
        health = analysis.health

        self.retranslate_static_texts()

        self.header.setText(
            LanguageManager.text("analysis_result_for").format(
                name=mesh.name
            )
        )

        status = tolerance["status"]
        self.set_score_card(
            self.statusCard,
            self.status_text(status),
            tolerance["message"],
            self.status_kind(status)
        )
        self.set_score_card(
            self.healthCard,
            f"{health.score:.1f} / 100",
            f"{health.label} | {self.status_text(health.status)}",
            self.status_kind(health.status)
        )
        self.set_score_card(
            self.timeCard,
            f"{analysis.elapsed_ms:.2f} ms",
            LanguageManager.text("analysis_calculation_time"),
            "neutral"
        )

        self.populate_mesh_section(mesh)
        self.populate_geometry_section(geo)
        self.populate_tolerance_section(tolerance)

        self.trendText["body"].setText(analysis.trend_report)

    def populate_mesh_section(self, mesh):
        self.clear_grid(self.meshGrid)

        metrics = (
            (LanguageManager.text("mesh_size"), f"{mesh.rows} x {mesh.cols}"),
            (LanguageManager.text("minimum"), f"{mesh.minimum:.4f} mm"),
            (LanguageManager.text("maximum"), f"{mesh.maximum:.4f} mm"),
            (LanguageManager.text("average"), f"{mesh.average:.4f} mm"),
            (
                LanguageManager.text("total_deviation"),
                f"{mesh.total_range:.4f} mm",
            ),
            (
                LanguageManager.text("standard_deviation"),
                f"{mesh.std:.4f} mm",
            ),
            ("RMS", f"{mesh.rms:.4f} mm"),
        )

        columns = 3
        for index, (label, value) in enumerate(metrics):
            is_last_single = (
                index == len(metrics) - 1 and len(metrics) % columns == 1
            )
            self.add_metric(
                self.meshGrid,
                index // columns,
                index % columns,
                label,
                value,
                col_span=columns if is_last_single else 1
            )

    def populate_geometry_section(self, geo):
        self.clear_grid(self.geometryGrid)

        metrics = (
            (
                LanguageManager.text("plane_max_deviation"),
                f"{geo.max_deviation:.4f} mm",
            ),
            (
                LanguageManager.text("plane_rms_deviation"),
                f"{geo.rms_deviation:.4f} mm",
            ),
            (LanguageManager.text("x_slope"), f"{geo.x_slope:.4f} mm"),
            (LanguageManager.text("y_slope"), f"{geo.y_slope:.4f} mm"),
        )

        for index, (label, value) in enumerate(metrics):
            self.add_metric(
                self.geometryGrid,
                index // 2,
                index % 2,
                label,
                value
            )

    def populate_tolerance_section(self, tolerance):
        self.clear_grid(self.toleranceGrid)

        rows = (
            (
                LanguageManager.text("total_deviation"),
                f"{tolerance['total_range']:.4f} / "
                f"{tolerance['max_total_range']:.4f} mm",
                tolerance["range_status"],
            ),
            (
                "RMS",
                f"{tolerance['rms']:.4f} / "
                f"{tolerance['max_rms']:.4f} mm",
                tolerance["rms_status"],
            ),
            (
                LanguageManager.text("plane_deviation"),
                f"{tolerance['plane_deviation']:.4f} / "
                f"{tolerance['max_plane_deviation']:.4f} mm",
                tolerance["plane_status"],
            ),
        )

        for index, (label, value, status) in enumerate(rows):
            self.add_metric(
                self.toleranceGrid,
                index,
                0,
                f"{label} ({self.status_text(status)})",
                value,
                self.status_kind(status)
            )

    def refresh_theme(self):
        theme = str(Config().get("theme"))

        if theme == "light":
            page_bg = "#F8FAFC"
            card_bg = "#FFFFFF"
            border = "#CBD5E1"
            text = "#0F172A"
            muted = "#64748B"
            metric_bg = "#F8FAFC"
        else:
            page_bg = "#0F172A"
            card_bg = "#1E293B"
            border = "#334155"
            text = "#F8FAFC"
            muted = "#CBD5E1"
            metric_bg = "#111827"

        self.setStyleSheet(f"""
        QWidget#AnalysisContent {{
            background: {page_bg};
        }}

        QLabel#AnalysisHeader {{
            color: {text};
            font-size: 16pt;
            font-weight: 800;
            background: transparent;
        }}

        QFrame#AnalysisScoreCard,
        QFrame#AnalysisSection {{
            background: {card_bg};
            border: 1px solid {border};
            border-radius: 10px;
        }}

        QFrame#AnalysisScoreCard[status="good"],
        QFrame#AnalysisMetric[status="good"] {{
            border-color: #16A34A;
        }}

        QFrame#AnalysisScoreCard[status="warning"],
        QFrame#AnalysisMetric[status="warning"] {{
            border-color: #CA8A04;
        }}

        QFrame#AnalysisScoreCard[status="bad"],
        QFrame#AnalysisMetric[status="bad"] {{
            border-color: #DC2626;
        }}

        QLabel#AnalysisCardTitle,
        QLabel#AnalysisSectionTitle {{
            color: {text};
            background: transparent;
            font-weight: 800;
        }}

        QLabel#AnalysisCardValue {{
            color: {text};
            background: transparent;
            font-size: 17pt;
            font-weight: 900;
        }}

        QLabel#AnalysisCardFooter,
        QLabel#AnalysisMetricLabel {{
            color: {muted};
            background: transparent;
            font-weight: 600;
        }}

        QFrame#AnalysisMetric {{
            background: {metric_bg};
            border: 1px solid {border};
            border-radius: 8px;
        }}

        QLabel#AnalysisMetricValue {{
            color: {text};
            background: transparent;
            font-size: 12pt;
            font-weight: 800;
        }}

        QTextEdit#AnalysisText {{
            background: {metric_bg};
            color: {text};
            border: 1px solid {border};
            border-radius: 8px;
            padding: 8px;
            font-family: Consolas, monospace;
            font-size: 10pt;
        }}
        """)

    def retranslate_static_texts(self):
        self.statusCard.titleLabel.setText(
            LanguageManager.text("overall_status")
        )
        self.statusCard.infoIcon.setToolTip(
            LanguageManager.text("tooltip_analysis_overall_status")
        )

        self.healthCard.titleLabel.setText(
            LanguageManager.text("machine_health")
        )
        self.healthCard.infoIcon.setToolTip(
            LanguageManager.text("tooltip_machine_health")
        )

        self.timeCard.titleLabel.setText(
            LanguageManager.text("analysis_duration")
        )
        self.timeCard.infoIcon.setToolTip(
            LanguageManager.text("tooltip_analysis_duration")
        )

        self.meshSection.titleLabel.setText(
            LanguageManager.text("mesh_summary")
        )
        self.meshSection.infoIcon.setToolTip(
            LanguageManager.text("tooltip_analysis_mesh_summary")
        )

        self.geometrySection.titleLabel.setText(
            LanguageManager.text("geometry_section")
        )
        self.geometrySection.infoIcon.setToolTip(
            LanguageManager.text("tooltip_analysis_geometry")
        )

        self.toleranceSection.titleLabel.setText(
            LanguageManager.text("quality_control")
        )
        self.toleranceSection.infoIcon.setToolTip(
            LanguageManager.text("tooltip_analysis_quality_control")
        )

        self.trendText["title"].setText(LanguageManager.text("trend"))
        self.trendText["info"].setToolTip(
            LanguageManager.text("tooltip_analysis_trend")
        )

    def refresh_language(self):
        self.retranslate_static_texts()
        if self.current_mesh is None:
            self.show_empty_state()
        else:
            self.update_mesh(self.current_mesh)

    def refresh_page(self):
        self.refresh_language()
        self.refresh_theme()
