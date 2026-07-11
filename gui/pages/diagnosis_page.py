"""
MeshAnalyzer Pro
Diagnosis and Recommendations Page
"""

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
from PySide6.QtCore import Qt

from core.analysis import AnalysisEngine
from core.config import Config
from languages import LanguageManager
from gui.widgets.info_icon import InfoIcon


class DiagnosisPage(QWidget):

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
        self.content.setObjectName("DiagnosisContent")

        self.layout = QVBoxLayout(self.content)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(14)

        self.header = QLabel()
        self.header.setObjectName("DiagnosisHeader")
        self.layout.addWidget(self.header)

        self.smartText = self.create_text_section("")
        self.diagnosticText = self.create_text_section("")

        self.reportGrid = QGridLayout()
        self.reportGrid.setSpacing(14)
        self.reportGrid.addWidget(self.smartText["frame"], 0, 0)
        self.reportGrid.addWidget(self.diagnosticText["frame"], 0, 1)
        self.reportGrid.setColumnStretch(0, 1)
        self.reportGrid.setColumnStretch(1, 1)
        self.layout.addLayout(self.reportGrid, 1)

        self.scroll.setWidget(self.content)
        main_layout.addWidget(self.scroll)

        self.show_empty_state()
        self.refresh_theme()

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh_language()

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

    def create_text_section(self, title):
        frame = QFrame()
        frame.setObjectName("DiagnosisSection")
        frame.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(16, 14, 16, 16)
        layout.setSpacing(10)

        title_label = QLabel(title)
        title_label.setObjectName("DiagnosisSectionTitle")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title_row, info_icon = self.create_info_title_row(title_label)

        body = QTextEdit()
        body.setObjectName("DiagnosisText")
        body.setReadOnly(True)
        body.setMinimumHeight(220)
        body.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding
        )

        layout.addWidget(title_row)
        layout.addWidget(body, 1)

        return {
            "frame": frame,
            "title": title_label,
            "info": info_icon,
            "body": body,
        }

    def show_empty_state(self):
        self.header.setText(LanguageManager.text("diagnosis_empty"))
        self.smartText["body"].setText(LanguageManager.text("waiting_result"))
        self.diagnosticText["body"].setText(
            LanguageManager.text("waiting_result")
        )
        self.retranslate_static_texts()

    def update_mesh(self, mesh):
        self.current_mesh = mesh
        analysis = AnalysisEngine(mesh, use_cache=False).run()
        self.current_analysis = analysis

        self.retranslate_static_texts()
        self.header.setText(
            LanguageManager.text("diagnosis_result_for").format(
                name=mesh.name
            )
        )
        self.smartText["body"].setText(analysis.smart_report)
        self.diagnosticText["body"].setText(
            "\n".join(analysis.diagnostic_report)
        )

    def refresh_theme(self):
        theme = str(Config().get("theme"))

        if theme == "light":
            page_bg = "#F8FAFC"
            card_bg = "#FFFFFF"
            border = "#CBD5E1"
            text = "#0F172A"
            metric_bg = "#F8FAFC"
        else:
            page_bg = "#0F172A"
            card_bg = "#1E293B"
            border = "#334155"
            text = "#F8FAFC"
            metric_bg = "#111827"

        self.setStyleSheet(f"""
        QWidget#DiagnosisContent {{
            background: {page_bg};
        }}

        QLabel#DiagnosisHeader {{
            color: {text};
            font-size: 16pt;
            font-weight: 800;
            background: transparent;
        }}

        QFrame#DiagnosisSection {{
            background: {card_bg};
            border: 1px solid {border};
            border-radius: 10px;
        }}

        QLabel#DiagnosisSectionTitle {{
            color: {text};
            background: transparent;
            font-weight: 800;
        }}

        QTextEdit#DiagnosisText {{
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
        self.smartText["title"].setText(
            LanguageManager.text("smart_diagnostic")
        )
        self.smartText["info"].setToolTip(
            LanguageManager.text("tooltip_diagnosis_smart")
        )

        self.diagnosticText["title"].setText(
            LanguageManager.text("mechanical_diagnostic")
        )
        self.diagnosticText["info"].setToolTip(
            LanguageManager.text("tooltip_diagnosis_mechanical")
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
