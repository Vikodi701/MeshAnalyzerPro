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
APP_USER_MODEL_ID = "com.vikodi.meshanalyzerpro.meshicon.v3"


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


def icon_candidates():
    candidates = [
        resource_path("assets", "icons", "app.ico"),
        resource_path("assets", "icons", "app.png"),
    ]

    if getattr(sys, "frozen", False):
        exe_dir = Path(sys.executable).resolve().parent
        candidates.extend([
            exe_dir / "assets" / "icons" / "app.ico",
            exe_dir / "assets" / "icons" / "app.png",
            exe_dir / "app.ico",
            exe_dir / "app.png",
        ])

    return candidates


def create_app_icon() -> QIcon:
    icon = QIcon()

    sizes = (16, 24, 32, 48, 64, 128, 256, 512)

    for icon_path in icon_candidates():
        if not icon_path.exists():
            continue

        suffix = icon_path.suffix.lower()

        if suffix == ".ico":
            for size in sizes:
                icon.addFile(
                    str(icon_path),
                    QSize(size, size),
                    QIcon.Mode.Normal,
                    QIcon.State.Off
                )
        else:
            for size in sizes:
                icon.addFile(
                    str(icon_path),
                    QSize(size, size),
                    QIcon.Mode.Normal,
                    QIcon.State.Off
                )

    return icon


def apply_window_icon_handle(window):
    """
    PyInstaller EXE çıktısında bazı Windows kurulumlarında Qt icon'u pencere
    ve görev çubuğuna geç iletebiliyor. HWND üzerinden de icon gönderiyoruz.
    """
    if os.name != "nt" or window is None:
        return

    try:
        import ctypes

        ico_path = resource_path("assets", "icons", "app.ico")
        if not ico_path.exists():
            return

        hwnd = int(window.winId())
        image_icon = 1
        load_from_file = 0x00000010
        lr_default_size = 0x00000040
        wm_seticon = 0x0080
        icon_small = 0
        icon_big = 1

        hicon_big = ctypes.windll.user32.LoadImageW(
            None,
            str(ico_path),
            image_icon,
            0,
            0,
            load_from_file | lr_default_size
        )

        hicon_small = ctypes.windll.user32.LoadImageW(
            None,
            str(ico_path),
            image_icon,
            16,
            16,
            load_from_file
        )

        if hicon_big:
            ctypes.windll.user32.SendMessageW(hwnd, wm_seticon, icon_big, hicon_big)

        if hicon_small:
            ctypes.windll.user32.SendMessageW(hwnd, wm_seticon, icon_small, hicon_small)
    except Exception:
        pass


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
        apply_window_icon_handle(window)

    return icon
