from pathlib import Path
from PySide6.QtWidgets import QApplication


class ThemeManager:

    _current = "dark"

    @classmethod
    def apply(cls, theme: str):
        cls._current = theme

        app = QApplication.instance()

        if app is None:
            return

        qss = Path("themes") / f"{theme}.qss"

        if qss.exists():
            app.setStyleSheet(
                qss.read_text(
                    encoding="utf-8"
                )
            )

    @classmethod
    def current(cls):
        return cls._current