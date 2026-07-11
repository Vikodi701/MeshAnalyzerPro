"""
MeshAnalyzer Pro
About Dialog
"""

from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QLabel,
    QPushButton,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from utils.app_info import (
    APP_NAME,
    APP_VERSION,
    APP_AUTHOR,
    APP_DESCRIPTION,
)


class AboutDialog(QDialog):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hakkında")
        self.setMinimumWidth(520)

        layout = QVBoxLayout(self)

        title = QLabel(APP_NAME)
        title.setAlignment(Qt.AlignCenter)

        font = QFont()
        font.setPointSize(18)
        font.setBold(True)

        title.setFont(font)

        layout.addWidget(title)

        version = QLabel(f"Versiyon : {APP_VERSION}")
        version.setAlignment(Qt.AlignCenter)

        layout.addWidget(version)

        author = QLabel(f"Geliştirici : {APP_AUTHOR}")
        author.setAlignment(Qt.AlignCenter)

        layout.addWidget(author)

        layout.addSpacing(15)

        desc = QLabel(APP_DESCRIPTION)
        desc.setWordWrap(True)
        desc.setAlignment(Qt.AlignCenter)

        layout.addWidget(desc)

        layout.addSpacing(20)

        features = QLabel(
            """
• Mesh Viewer

• Heatmap

• Contour Map

• 3D Surface

• Compare

• History

• Trend Analysis

• Smart Diagnostic

• Machine Health Score

• PDF Report v3

• Export All

• Project (.meshproj)
"""
        )

        features.setWordWrap(True)

        layout.addWidget(features)

        layout.addSpacing(20)

        close_button = QPushButton("Kapat")
        close_button.clicked.connect(self.accept)

        layout.addWidget(close_button)