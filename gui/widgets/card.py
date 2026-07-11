"""
MeshAnalyzer Pro
Base Card Widget
Central Theme Ready
"""

from PySide6.QtCore import (
    QPropertyAnimation,
    QEasingCurve,
)

from PySide6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QGraphicsDropShadowEffect,
)

from PySide6.QtGui import QColor


class BaseCard(QFrame):

    COLOR_MAP = {
        "#3B82F6": "blue",
        "#3498DB": "blue",
        "#2980B9": "blue",

        "#2ECC71": "green",
        "#22C55E": "green",
        "#27AE60": "green",

        "#F1C40F": "yellow",
        "#FACC15": "yellow",

        "#E74C3C": "red",
        "#EF4444": "red",
        "#DC2626": "red",
        "#C0392B": "red",

        "#9B59B6": "purple",

        "#E67E22": "orange",

        "#16A085": "teal",

        "#7F8C8D": "gray",
        "#95A5A6": "gray",
        "#34495E": "gray",
    }

    def __init__(self, title="", radius=14, parent=None):
        super().__init__(parent)

        self.radius = radius

        self.setObjectName("BaseCard")
        self.setProperty("accent", "blue")

        self.setMinimumHeight(150)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(24)
        self.shadow.setOffset(0, 4)
        self.shadow.setColor(QColor(0, 0, 0, 90))
        self.setGraphicsEffect(self.shadow)

        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(18, 18, 18, 18)
        self.layout.setSpacing(10)

        self.anim = QPropertyAnimation(
            self.shadow,
            b"blurRadius"
        )
        self.anim.setDuration(160)
        self.anim.setEasingCurve(
            QEasingCurve.Type.OutCubic
        )

    def setBorderColor(self, color: str):
        accent = self.COLOR_MAP.get(
            str(color).upper(),
            self.COLOR_MAP.get(str(color), "blue")
        )

        self.setProperty("accent", accent)

        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

    def enterEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(40)
        self.anim.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.anim.stop()
        self.anim.setStartValue(self.shadow.blurRadius())
        self.anim.setEndValue(24)
        self.anim.start()
        super().leaveEvent(event)