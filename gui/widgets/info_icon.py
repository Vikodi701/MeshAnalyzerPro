"""
MeshAnalyzer Pro
Theme-aware Info Icon Widget
"""

from core.config import Config
from PySide6.QtCore import Qt, QEvent
from PySide6.QtGui import QPainter, QColor, QFont
from PySide6.QtWidgets import QLabel

from gui.widgets.info_popup import InfoPopup


class InfoIcon(QLabel):

    def __init__(self, text="", parent=None):
        super().__init__(parent)

        self.popup = InfoPopup(text)

        self.setObjectName("InfoIcon")
        self.setFixedSize(20, 20)
        self.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def setText(self, text):
        self.popup.setHtml(str(text))

    def setToolTip(self, text):
        self.setText(text)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(
            QPainter.RenderHint.Antialiasing
        )

        text_color = self.palette().windowText().color()

        brightness = (
            text_color.red() * 0.299 +
            text_color.green() * 0.587 +
            text_color.blue() * 0.114
        )

        if brightness > 145:
            bg = QColor("#0284C7")
            fg = QColor("#FFFFFF")
        else:
            bg = QColor("#38BDF8")
            fg = QColor("#0F172A")

        painter.setBrush(bg)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(2, 2, 16, 16)

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)

        painter.setFont(font)
        painter.setPen(fg)

        painter.drawText(
            self.rect(),
            Qt.AlignmentFlag.AlignCenter,
            "i"
        )

        painter.end()

    def enterEvent(self, event):
        if not bool(Config().get("appearance_show_hover_info")):
            return super().enterEvent(event)
        self.popup.showNearCursor()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.popup.hide()
        super().leaveEvent(event)

    def changeEvent(self, event):
        if event.type() == QEvent.Type.PaletteChange:
            self.update()

        super().changeEvent(event)