"""
MeshAnalyzer Pro
Help Dialog
"""

from PySide6.QtWidgets import (
    QApplication,
    QDialog,
    QVBoxLayout,
    QTextEdit,
    QPushButton,
)

from PySide6.QtCore import QEvent, Qt

from languages import LanguageManager
from utils.app_icon import resource_path


class HelpDialog(QDialog):

    def __init__(self, topic, parent=None):
        super().__init__(parent)

        self.topic = topic

        self.setWindowTitle(self.title_for_topic(topic))
        self.resize(720, 560)

        layout = QVBoxLayout(self)

        self.text = QTextEdit()
        self.text.setReadOnly(True)

        close_button = QPushButton(LanguageManager.text("close"))
        close_button.clicked.connect(self.accept)

        layout.addWidget(self.text)
        layout.addWidget(close_button)

        self.load_content()

    def eventFilter(self, obj, event):
        if event.type() == QEvent.Type.MouseButtonPress:
            global_pos = event.globalPosition().toPoint()

            if self.isVisible() and not self.frameGeometry().contains(global_pos):
                self.accept()
                return False

        if obj is self and event.type() == QEvent.Type.WindowDeactivate:
            self.accept()
            return False

        return super().eventFilter(obj, event)

    def showEvent(self, event):
        super().showEvent(event)

        app = QApplication.instance()
        if app is not None:
            try:
                app.installEventFilter(self)
            except Exception:
                pass

    def closeEvent(self, event):
        app = QApplication.instance()
        if app is not None:
            try:
                app.removeEventFilter(self)
            except Exception:
                pass

        super().closeEvent(event)

    def open_non_modal(self):
        self.setModal(False)
        self.setWindowModality(Qt.WindowModality.NonModal)
        self.show()
        self.raise_()
        self.activateWindow()

    def title_for_topic(self, topic):
        titles = {
            "dashboard": LanguageManager.text("dashboard"),
            "mesh": LanguageManager.text("mesh_view"),
            "heatmap": LanguageManager.text("heatmap"),
            "topography": LanguageManager.text("topography"),
            "surface3d": LanguageManager.text("surface_3d"),
            "analysis": LanguageManager.text("analysis"),
            "diagnosis": LanguageManager.text("diagnosis_recommendations"),
            "compare": LanguageManager.text("compare"),
            "history": LanguageManager.text("history"),
            "settings": LanguageManager.text("settings"),
        }

        return titles.get(topic, "Help")

    def load_content(self):
        lang = LanguageManager.current_language()

        file_path = resource_path("help", lang, f"{self.topic}.md")

        if not file_path.exists():
            file_path = resource_path("help", "tr", f"{self.topic}.md")

        if file_path.exists():
            content = file_path.read_text(encoding="utf-8")
        else:
            content = "Yardım içeriği bulunamadı."

        self.text.setMarkdown(content)