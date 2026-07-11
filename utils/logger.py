"""
MeshAnalyzer Pro
Central Logger
"""

import logging
from pathlib import Path


def setup_logger():
    log_folder = Path("logs")
    log_folder.mkdir(exist_ok=True)

    log_file = log_folder / "app.log"

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    return logging.getLogger("MeshAnalyzerPro")


logger = setup_logger()