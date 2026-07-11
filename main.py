"""
MeshAnalyzer Pro
main.py
Application Entry Point
"""

import sys
from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow
from themes.theme_manager import ThemeManager

from utils.logger import logger
from utils.error_handler import ErrorHandler
from utils.dialog_buttons import install_dialog_button_language_filter
from utils.app_icon import apply_app_icon, set_windows_app_user_model_id


def main():

    logger.info("MeshAnalyzer Pro başlatılıyor.")

    # Windows taskbar icon identity
    set_windows_app_user_model_id()

    # Global hata yakalayıcı
    ErrorHandler.install()

    # Qt Application
    app = QApplication(sys.argv)

    # Uygulama ikonu
    set_windows_app_user_model_id()
    apply_app_icon(app=app)

    # Açılan dialoglardaki standart butonları aktif dile göre düzelt
    install_dialog_button_language_filter(app)

    # Tema
    ThemeManager.apply(app)

    # Ana pencere
    window = MainWindow()
    apply_app_icon(app=app, window=window)

    # Ayardaki başlangıç pencere durumunu uygula
    window.apply_startup_window_state()

    logger.info("Ana pencere açıldı.")

    exit_code = app.exec()

    logger.info("MeshAnalyzer Pro kapatılıyor.")

    sys.exit(exit_code)


if __name__ == "__main__":
    main()