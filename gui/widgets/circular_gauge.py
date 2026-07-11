"""
MeshAnalyzer Pro
Circular Gauge Widget
Theme Ready
"""

from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import (
    QColor,
    QFont,
    QPainter,
    QPen,
)
from PySide6.QtWidgets import QWidget


class CircularGauge(QWidget):

    def __init__(self, value=0, maximum=100, parent=None):
        super().__init__(parent)

        self.value = value
        self.maximum = maximum

        self.setMinimumSize(180, 180)

    def setValue(self, value):
        self.value = max(0, min(value, self.maximum))
        self.update()

    def color(self):
        ratio = self.value / self.maximum

        if ratio >= 0.80:
            return QColor("#22C55E")

        if ratio >= 0.60:
            return QColor("#FACC15")

        return QColor("#EF4444")

    def textColor(self):
        return self.palette().windowText().color()

    def backgroundRingColor(self):
        text_color = self.textColor()

        brightness = (
            text_color.red() * 0.299 +
            text_color.green() * 0.587 +
            text_color.blue() * 0.114
        )

        if brightness > 145:
            return QColor("#CBD5E1")

        return QColor("#334155")

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        size = min(self.width(), self.height()) - 20

        rect = QRectF(
            10,
            10,
            size,
            size
        )

        # Arka halka
        pen = QPen(self.backgroundRingColor())
        pen.setWidth(12)

        painter.setPen(pen)

        painter.drawArc(
            rect,
            0,
            360 * 16
        )

        # Değer halkası
        pen = QPen(self.color())
        pen.setWidth(12)
        pen.setCapStyle(Qt.PenCapStyle.RoundCap)

        painter.setPen(pen)

        span = int(-360 * (self.value / self.maximum) * 16)

        painter.drawArc(
            rect,
            90 * 16,
            span
        )

        # Ana değer
        font = QFont()
        font.setPointSize(24)
        font.setBold(True)

        painter.setFont(font)
        painter.setPen(self.textColor())

        painter.drawText(
            rect,
            Qt.AlignmentFlag.AlignCenter,
            f"{self.value:.0f}"
        )

        # /100
        font.setPointSize(10)
        font.setBold(False)

        painter.setFont(font)
        painter.setPen(self.textColor())

        painter.drawText(
            rect.adjusted(0, 55, 0, 0),
            Qt.AlignmentFlag.AlignCenter,
            "/100"
        )

        painter.end()