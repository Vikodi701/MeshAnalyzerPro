"""
MeshAnalyzer Pro
Global Error Handler
"""

import sys
import traceback
from pathlib import Path

from PySide6.QtWidgets import QMessageBox

from utils.logger import logger


class ErrorHandler:

    @staticmethod
    def install():
        sys.excepthook = ErrorHandler.handle_exception

    @staticmethod
    def handle_exception(exc_type, exc_value, exc_traceback):

        text = "".join(
            traceback.format_exception(
                exc_type,
                exc_value,
                exc_traceback
            )
        )

        logger.critical(text)

        log_dir = Path("logs")
        log_dir.mkdir(exist_ok=True)

        crash_file = log_dir / "crash.log"

        with open(
            crash_file,
            "a",
            encoding="utf-8"
        ) as f:

            f.write("=" * 80 + "\n")
            f.write(text)
            f.write("\n")

        QMessageBox.critical(
            None,
            "Beklenmeyen Hata",
            (
                "Beklenmeyen bir hata oluştu.\n\n"
                "Hata bilgisi logs/crash.log dosyasına kaydedildi."
            )
        )