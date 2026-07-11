"""
MeshAnalyzer Pro
Reusable Section Title Widget
"""

from PySide6.QtWidgets import QWidget, QLabel, QHBoxLayout
from PySide6.QtCore import Qt

from gui.widgets.info_icon import InfoIcon


class SectionTitle(QWidget):

    def __init__(
        self,
        title="",
        icon="",
        tooltip="",
        parent=None,
    ):
        super().__init__(parent)

        self.setObjectName("SectionTitleWidget")

        self.icon = icon

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        self.titleLabel = QLabel()
        self.titleLabel.setObjectName("SectionTitleText")
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.infoIcon = InfoIcon(tooltip)

        layout.addStretch()
        layout.addWidget(self.titleLabel)
        layout.addWidget(self.infoIcon)
        layout.addStretch()

        self.setTitle(title)

    def setTitle(self, title):
        if self.icon:
            self.titleLabel.setText(f"{self.icon} {title}")
        else:
            self.titleLabel.setText(str(title))

    def setTooltip(self, tooltip):
        self.infoIcon.setToolTip(str(tooltip))