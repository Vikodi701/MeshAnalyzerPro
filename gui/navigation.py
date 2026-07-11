"""
MeshAnalyzer Pro
Modern SVG Navigation Sidebar
LanguageManager destekli
"""

import html
import re

from PySide6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QDialog, QTextBrowser, QDialogButtonBox, QApplication
from PySide6.QtCore import Signal, QSize, QUrl, QEvent, Qt
from PySide6.QtGui import QIcon, QDesktopServices

from languages import LanguageManager
from utils.app_icon import resource_path
from utils.dialog_buttons import install_dialog_button_language_filter


class Navigation(QWidget):

    pageChanged = Signal(int)

    def __init__(self):
        super().__init__()

        self.setObjectName("SideBar")
        self.setFixedWidth(315)
        self.setMinimumWidth(315)
        self.setMaximumWidth(315)

        self.buttons = []
        self.button_defs = []

        layout = QVBoxLayout(self)
        layout.setSpacing(10)
        layout.setContentsMargins(12, 16, 12, 16)

        self.title = QLabel()
        self.title.setObjectName("SideBarTitle")
        layout.addWidget(self.title)

        self.add_button(layout, "dashboard", "dashboard.svg", 0)
        self.add_button(layout, "mesh_view", "mesh.svg", 1)
        self.add_button(layout, "heatmap", "heatmap.svg", 2)
        self.add_button(layout, "topography", "topography.svg", 3)
        self.add_button(layout, "surface_3d", "surface3d.svg", 4)
        self.add_button(layout, "analysis", "analysis.svg", 5)
        self.add_button(layout, "diagnosis_recommendations", "diagnosis.svg", 6)
        self.add_button(layout, "compare", "compare.svg", 7)
        self.add_button(layout, "history", "history.svg", 8)

        layout.addStretch()
        self.build_conf_help_card(layout)

        self.retranslate()
        self.setCurrentPage(0)

    def eventFilter(self, obj, event):
        dialog = getattr(self, "_active_conf_help_dialog", None)

        if dialog is not None and dialog.isVisible():
            if event.type() == QEvent.Type.MouseButtonPress:
                global_pos = event.globalPosition().toPoint()

                if not dialog.frameGeometry().contains(global_pos):
                    self.close_active_conf_help_dialog()
                    return False

            if obj is dialog and event.type() == QEvent.Type.WindowDeactivate:
                self.close_active_conf_help_dialog()
                return False

        return super().eventFilter(obj, event)

    def close_active_conf_help_dialog(self):
        dialog = getattr(self, "_active_conf_help_dialog", None)

        if dialog is not None:
            try:
                dialog.accept()
            except Exception:
                dialog.close()

        app = QApplication.instance()
        if app is not None:
            try:
                app.removeEventFilter(self)
            except Exception:
                pass

        self._active_conf_help_dialog = None

    def build_conf_help_card(self, parent_layout):
        self.confHelpCard = QFrame()
        self.confHelpCard.setObjectName("ConfHelpCard")

        card_layout = QVBoxLayout(self.confHelpCard)
        card_layout.setContentsMargins(10, 10, 10, 10)
        card_layout.setSpacing(8)

        self.confHelpTitle = QLabel()
        self.confHelpTitle.setObjectName("ConfHelpTitle")
        self.confHelpTitle.setWordWrap(True)

        self.confWikiButton = QPushButton()
        self.confWikiButton.setObjectName("ConfHelpButton")
        self.confWikiButton.setMinimumHeight(32)

        self.confDeviceButton = QPushButton()
        self.confDeviceButton.setObjectName("ConfHelpButton")
        self.confDeviceButton.setMinimumHeight(32)

        self.confWikiButton.clicked.connect(self.show_anycubic_wiki_help)
        self.confDeviceButton.clicked.connect(self.show_device_export_help)

        card_layout.addWidget(self.confHelpTitle)
        card_layout.addWidget(self.confWikiButton)
        card_layout.addWidget(self.confDeviceButton)

        parent_layout.addWidget(self.confHelpCard)

    def message_to_html(self, message):
        message = message.replace("\\n", "\n")
        escaped = html.escape(message)

        url_pattern = r"(https?://[^\s<]+)"
        escaped = re.sub(
            url_pattern,
            r'<a href="\1">\1</a>',
            escaped
        )

        return escaped.replace("\n", "<br>")

    def show_conf_help_dialog(self, title_key, message_key):
        dialog = QDialog(self)
        dialog.setWindowTitle(LanguageManager.text(title_key))
        dialog.setMinimumWidth(720)
        dialog.setMinimumHeight(260)

        layout = QVBoxLayout(dialog)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        browser = QTextBrowser()
        browser.setObjectName("ConfHelpTextBrowser")
        browser.setOpenExternalLinks(False)
        browser.setOpenLinks(False)
        browser.anchorClicked.connect(self.open_external_link)
        browser.setHtml(
            "<div style='font-size:10.5pt; line-height:1.45;'>"
            + self.message_to_html(LanguageManager.text(message_key))
            + "</div>"
        )

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        install_dialog_button_language_filter().localize_buttons(buttons)
        buttons.accepted.connect(dialog.accept)

        layout.addWidget(browser)
        layout.addWidget(buttons)

        dialog.setModal(False)
        dialog.setWindowModality(Qt.WindowModality.NonModal)

        # Önce eski açık yardım penceresi varsa kapat.
        self.close_active_conf_help_dialog()

        self._active_conf_help_dialog = dialog
        app = QApplication.instance()
        if app is not None:
            app.installEventFilter(self)

        dialog.finished.connect(lambda _result: self.close_active_conf_help_dialog())
        dialog.show()
        dialog.raise_()
        dialog.activateWindow()

    def open_external_link(self, url):
        if isinstance(url, str):
            url = QUrl(url)

        QDesktopServices.openUrl(url)

    def show_anycubic_wiki_help(self):
        self.show_conf_help_dialog(
            "conf_help_wiki_title",
            "conf_help_wiki_message"
        )

    def show_device_export_help(self):
        self.show_conf_help_dialog(
            "conf_help_device_title",
            "conf_help_device_message"
        )

    def add_button(self, layout, text_key, icon_name, index):
        button = QPushButton()
        button.setObjectName("SideBarButton")
        button.setCheckable(True)
        button.setMinimumHeight(44)
        button.setIcon(self.icon(icon_name))
        button.setIconSize(QSize(22, 22))
        button.clicked.connect(
            lambda checked=False, i=index: self.change_page(i)
        )

        self.buttons.append(button)
        self.button_defs.append((button, text_key))
        layout.addWidget(button)

    def icon(self, filename):
        return QIcon(str(resource_path("assets", "icons", filename)))

    def change_page(self, index):
        self.setCurrentPage(index)
        self.pageChanged.emit(index)

    def setCurrentPage(self, index):
        for i, button in enumerate(self.buttons):
            button.setChecked(i == index)

    def retranslate(self):
        self.title.setText(LanguageManager.text("app_name"))

        if hasattr(self, "confHelpTitle"):
            self.confHelpTitle.setText(
                LanguageManager.text("conf_help_card_title")
            )
            self.confWikiButton.setText(
                LanguageManager.text("conf_help_wiki_button")
            )
            self.confDeviceButton.setText(
                LanguageManager.text("conf_help_device_button")
            )

        for button, text_key in self.button_defs:
            button.setText(LanguageManager.text(text_key))
