"""
MeshAnalyzer Pro
Modern Info Card
Theme Ready + InfoIcon destekli
"""

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QWidget, QHBoxLayout

from gui.widgets.card import BaseCard
from gui.widgets.info_icon import InfoIcon


class InfoCard(BaseCard):

    def __init__(
        self,
        title="",
        value="",
        footer="",
        color="#3B82F6",
        tooltip="",
        parent=None,
    ):
        super().__init__("", parent=parent)

        self.border_color = color

        self.titleTextLabel = QLabel(title)
        self.titleTextLabel.setObjectName("CardTitleText")

        title_font = QFont()
        title_font.setPointSize(11)
        title_font.setBold(True)
        self.titleTextLabel.setFont(title_font)

        self.infoIcon = InfoIcon(tooltip)

        self.titleRow = QWidget()
        self.titleRow.setObjectName("CardTitleRow")

        titleLayout = QHBoxLayout(self.titleRow)
        titleLayout.setContentsMargins(0, 0, 0, 0)
        titleLayout.setSpacing(6)

        titleLayout.addStretch()
        titleLayout.addWidget(self.titleTextLabel)
        titleLayout.addWidget(self.infoIcon)
        titleLayout.addStretch()

        self.valueLabel = QLabel(value)
        self.valueLabel.setObjectName("CardValue")
        self.valueLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        value_font = QFont()
        value_font.setPointSize(22)
        value_font.setBold(True)
        self.valueLabel.setFont(value_font)

        self.footerLabel = QLabel(footer)
        self.footerLabel.setObjectName("CardFooter")
        self.footerLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        footer_font = QFont()
        footer_font.setPointSize(10)
        self.footerLabel.setFont(footer_font)

        self.layout.addWidget(self.titleRow)
        self.layout.addStretch()
        self.layout.addWidget(self.valueLabel)
        self.layout.addStretch()
        self.layout.addWidget(self.footerLabel)

        self.setBorderColor(color)

    def setTitle(self, text):
        self.titleTextLabel.setText(str(text))

    def setValue(self, value):
        self.valueLabel.setText(str(value))

    def setFooter(self, footer):
        self.footerLabel.setText(str(footer))

    def setColor(self, color):
        self.border_color = color
        self.setBorderColor(color)

    def setTooltip(self, text):
        self.infoIcon.setToolTip(str(text))