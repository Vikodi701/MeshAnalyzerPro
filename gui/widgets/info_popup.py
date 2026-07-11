"""
MeshAnalyzer Pro
Modern Info Popup
Theme-aware + Screen-safe positioning
"""

from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QApplication,
)
from PySide6.QtGui import QCursor


class InfoPopup(QFrame):

    def __init__(self, html="", parent=None):
        super().__init__(parent)

        self.setWindowFlags(
            Qt.WindowType.ToolTip |
            Qt.WindowType.FramelessWindowHint
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_ShowWithoutActivating
        )

        self.setAttribute(
            Qt.WidgetAttribute.WA_TransparentForMouseEvents
        )

        self.setObjectName("InfoPopup")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(16, 16, 16, 16)

        self.label = QLabel()
        self.label.setObjectName("InfoPopupLabel")
        self.label.setWordWrap(True)
        self.label.setTextFormat(Qt.TextFormat.RichText)
        self.label.setText(html)

        layout.addWidget(self.label)

        self.setMinimumWidth(220)
        self.setMaximumWidth(460)
        self.label.setMaximumWidth(420)
        self.adjustSize()

    def setHtml(self, html):
        self.label.setText(str(html))
        self.label.adjustSize()
        self.adjustSize()

    def showNearCursor(self):
        self.adjustSize()

        cursor_pos = QCursor.pos()
        screen = QApplication.screenAt(cursor_pos)

        if screen is None:
            screen = QApplication.primaryScreen()

        screen_rect = screen.availableGeometry()

        popup_width = self.width()
        popup_height = self.height()

        x = cursor_pos.x() + 18
        y = cursor_pos.y() + 18

        if x + popup_width > screen_rect.right():
            x = cursor_pos.x() - popup_width - 18

        if y + popup_height > screen_rect.bottom():
            y = cursor_pos.y() - popup_height - 18

        if x < screen_rect.left():
            x = screen_rect.left() + 8

        if y < screen_rect.top():
            y = screen_rect.top() + 8

        self.move(QPoint(x, y))
        self.show()
