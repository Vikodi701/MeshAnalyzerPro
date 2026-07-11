"""
MeshAnalyzer Pro
Reusable Color Bar Widget
"""

from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PySide6.QtCore import Qt


class ColorBar(QWidget):

    def __init__(self, title="", parent=None):
        super().__init__(parent)

        self.setObjectName("ColorBarWidget")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(8)

        self.titleLabel = QLabel(title)
        self.titleLabel.setObjectName("ColorBarTitle")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.maxLabel = QLabel("--")
        self.maxLabel.setObjectName("ColorBarValue")
        self.maxLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.bar = QFrame()
        self.bar.setObjectName("ColorBarGradient")
        self.bar.setMinimumHeight(140)
        self.bar.setMaximumHeight(180)

        self.minLabel = QLabel("--")
        self.minLabel.setObjectName("ColorBarValue")
        self.minLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(self.titleLabel)
        layout.addWidget(self.maxLabel)
        layout.addWidget(self.bar)
        layout.addWidget(self.minLabel)

    def setTitle(self, text):
        self.titleLabel.setText(str(text))

    def setRange(self, minimum, maximum):
        self.maxLabel.setText(f"{maximum:.4f} mm")
        self.minLabel.setText(f"{minimum:.4f} mm")