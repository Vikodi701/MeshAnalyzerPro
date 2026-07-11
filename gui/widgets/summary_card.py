"""
MeshAnalyzer Pro
Reusable Summary Card Widget
"""

from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QGridLayout,
    QLabel,
)

from PySide6.QtCore import Qt

from gui.widgets.section_title import SectionTitle


class SummaryCard(QFrame):

    def __init__(
        self,
        title="",
        icon="",
        tooltip="",
        parent=None,
    ):
        super().__init__(parent)

        self.setObjectName("SummaryCard")

        self.labels = {}
        self.values = {}

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(14)

        self.titleWidget = SectionTitle(
            title=title,
            icon=icon,
            tooltip=tooltip,
        )

        layout.addWidget(self.titleWidget)

        self.grid = QGridLayout()
        self.grid.setVerticalSpacing(12)
        self.grid.setHorizontalSpacing(12)

        layout.addLayout(self.grid)
        layout.addStretch()

    def addRow(self, key, label_text="", value_text="--"):
        row = len(self.labels)

        label = QLabel(label_text)
        label.setObjectName("SummaryLabel")

        value = QLabel(value_text)
        value.setObjectName("SummaryValue")
        value.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.labels[key] = label
        self.values[key] = value

        self.grid.addWidget(label, row, 0)
        self.grid.addWidget(value, row, 1)

    def setLabel(self, key, text):
        if key in self.labels:
            self.labels[key].setText(str(text))

    def setValue(self, key, text):
        if key in self.values:
            self.values[key].setText(str(text))

    def setTitle(self, title):
        self.titleWidget.setTitle(title)

    def setTooltip(self, tooltip):
        self.titleWidget.setTooltip(tooltip)