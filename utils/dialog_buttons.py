"""
MeshAnalyzer Pro
Dialog button language helper

Qt'nin standart OK / Cancel / Yes / No butonları bazı Windows/EXE
çalıştırma durumlarında İngilizce kalabiliyor. Bu event filter açılan
dialoglardaki standart buton metinlerini aktif dil dosyasına göre düzeltir.
"""

from PySide6.QtCore import QObject, QEvent
from PySide6.QtWidgets import QApplication, QPushButton

from languages import LanguageManager


class DialogButtonLanguageFilter(QObject):

    STANDARD_TEXTS = {
        "ok",
        "&ok",
        "tamam",
        "&tamam",
        "cancel",
        "&cancel",
        "iptal",
        "i̇ptal",
        "&iptal",
        "&i̇ptal",
        "yes",
        "&yes",
        "evet",
        "&evet",
        "no",
        "&no",
        "hayır",
        "hayir",
        "&hayır",
        "&hayir",
        "open",
        "&open",
        "aç",
        "&aç",
        "save",
        "&save",
        "kaydet",
        "&kaydet",
    }

    def eventFilter(self, obj, event):
        if event.type() in (
            QEvent.Type.Show,
            QEvent.Type.Polish,
            QEvent.Type.WindowActivate,
        ):
            self.localize_buttons(obj)

        return super().eventFilter(obj, event)

    def localized_text(self, text):
        normalized = str(text).strip().replace("&", "").lower()

        if normalized == "ok" or normalized == "tamam":
            return LanguageManager.text("dialog_ok")

        if normalized == "cancel" or normalized in ("iptal", "i̇ptal"):
            return LanguageManager.text("dialog_cancel")

        if normalized == "yes" or normalized == "evet":
            return LanguageManager.text("dialog_yes")

        if normalized == "no" or normalized in ("hayır", "hayir"):
            return LanguageManager.text("dialog_no")

        if normalized == "open" or normalized == "aç":
            return LanguageManager.text("dialog_open")

        if normalized == "save" or normalized == "kaydet":
            return LanguageManager.text("dialog_save")

        return None

    def localize_buttons(self, widget):
        if widget is None:
            return

        try:
            buttons = widget.findChildren(QPushButton)
        except Exception:
            return

        for button in buttons:
            current = button.text()
            new_text = self.localized_text(current)

            if new_text:
                button.setText(new_text)


_dialog_button_filter = None


def install_dialog_button_language_filter(app=None):
    global _dialog_button_filter

    if app is None:
        app = QApplication.instance()

    if app is None:
        return None

    if _dialog_button_filter is None:
        _dialog_button_filter = DialogButtonLanguageFilter(app)
        app.installEventFilter(_dialog_button_filter)

    return _dialog_button_filter
