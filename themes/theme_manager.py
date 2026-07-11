"""
MeshAnalyzer Pro
Theme Manager
"""

from core.config import Config
from utils.app_icon import resource_path


class ThemeManager:

    @staticmethod
    def theme_file(theme_name):
        if theme_name == "light":
            return resource_path("themes", "light.qss")

        return resource_path("themes", "dark.qss")

    @staticmethod
    def load_qss(theme_name):
        file = ThemeManager.theme_file(theme_name)

        if not file.exists():
            return ""

        return file.read_text(encoding="utf-8")

    @staticmethod
    def apply(app, theme_name=None):
        config = Config()

        if theme_name is None:
            theme_name = config.get("theme")

        qss = ThemeManager.load_qss(theme_name)
        app.setStyleSheet(qss)