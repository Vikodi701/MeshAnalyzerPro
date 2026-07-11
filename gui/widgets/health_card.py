"""
MeshAnalyzer Pro
Health Card Widget
Theme Ready
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout

from gui.widgets.card import BaseCard
from gui.widgets.circular_gauge import CircularGauge
from gui.widgets.info_icon import InfoIcon


class HealthCard(BaseCard):

    def __init__(self, score=0, label="", parent=None):
        super().__init__("", parent=parent)

        self.gauge = CircularGauge(score)

        self.titleTextLabel = QLabel("")
        self.titleTextLabel.setObjectName("CardTitleText")

        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.titleTextLabel.setFont(font)

        self.infoIcon = InfoIcon("")

        self.titleRow = QWidget()
        self.titleRow.setObjectName("CardTitleRow")

        title_layout = QHBoxLayout(self.titleRow)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.setSpacing(6)

        title_layout.addStretch()
        title_layout.addWidget(self.titleTextLabel)
        title_layout.addWidget(self.infoIcon)
        title_layout.addStretch()

        self.statusLabel = QLabel(label)
        self.statusLabel.setObjectName("CardValue")
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        status_font = QFont()
        status_font.setPointSize(13)
        status_font.setBold(True)
        self.statusLabel.setFont(status_font)

        self.layout.addWidget(self.titleRow)
        self.layout.addStretch()
        self.layout.addWidget(
            self.gauge,
            alignment=Qt.AlignmentFlag.AlignCenter
        )
        self.layout.addStretch()
        self.layout.addWidget(self.statusLabel)

        self.setHealth(score, label)

    def setHealth(self, score, label):
        self.gauge.setValue(score)
        self.statusLabel.setText(str(label))

        if score >= 75:
            self.setBorderColor("#22C55E")
        elif score >= 50:
            self.setBorderColor("#FACC15")
        else:
            self.setBorderColor("#EF4444")

    def setTitle(self, text):
        self.titleTextLabel.setText(str(text))

    def setTooltip(self, text):
        self.infoIcon.setToolTip(str(text))