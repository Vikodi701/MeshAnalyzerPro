"""
MeshAnalyzer Pro
Robust Windows application icon helper
"""

import os
import sys
from pathlib import Path

from PySide6.QtCore import QSize
from PySide6.QtGui import QIcon


# Icon değiştiğinde Windows eski taskbar icon cache'ini kullanmasın diye
# AppUserModelID de güncellendi.
APP_USER_MODEL_ID = "com.vikodi.meshanalyzerpro.meshicon.v2"


def app_root() -> Path:
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    return Path(__file__).resolve().parents[1]


def resource_path(*parts: str) -> Path:
    base = getattr(sys, "_MEIPASS", None)

    if base:
        candidate = Path(base).joinpath(*parts)
        if candidate.exists():
            return candidate

    return app_root().joinpath(*parts)


def set_windows_app_user_model_id():
    if os.name != "nt":
        return

    try:
        import ctypes

        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
            APP_USER_MODEL_ID
        )
    except Exception:
        pass


def create_app_icon() -> QIcon:
    icon = QIcon()

    ico_path = resource_path("assets", "icons", "app.ico")
    png_path = resource_path("assets", "icons", "app.png")

    # Windows için önce ICO dosyasını farklı boyutlarla ekliyoruz.
    if ico_path.exists():
        for size in (16, 24, 32, 48, 64, 128, 256):
            icon.addFile(
                str(ico_path),
                QSize(size, size),
                QIcon.Mode.Normal,
                QIcon.State.Off
            )

    # Qt bazı sistemlerde büyük PNG'yi daha iyi kullanıyor.
    if png_path.exists():
        for size in (16, 24, 32, 48, 64, 128, 256, 512):
            icon.addFile(
                str(png_path),
                QSize(size, size),
                QIcon.Mode.Normal,
                QIcon.State.Off
            )

    return icon


def apply_app_icon(app=None, window=None):
    icon = create_app_icon()

    if app is not None:
        try:
            app.setDesktopFileName(APP_USER_MODEL_ID)
        except Exception:
            pass

        if not icon.isNull():
            app.setWindowIcon(icon)

    if window is not None and not icon.isNull():
        window.setWindowIcon(icon)

    return icon
