"""
MeshAnalyzer Pro
Analysis Cache
"""

from typing import Optional

from languages import LanguageManager
from core.config import Config

from .result import ResultContainer


class AnalysisCache:

    _instance = None

    def __init__(self):
        self._last_result: Optional[ResultContainer] = None
        self._mesh_key: Optional[str] = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def make_key(self, mesh):
        cfg = Config()

        return (
            f"{mesh.name}|{mesh.rows}x{mesh.cols}|"
            f"{mesh.minimum:.6f}|{mesh.maximum:.6f}|{mesh.rms:.6f}|"
            f"{LanguageManager.current_language()}|"
            f"{float(cfg.get('max_total_range')):.6f}|"
            f"{float(cfg.get('max_rms')):.6f}|"
            f"{float(cfg.get('max_plane_deviation')):.6f}"
        )

    def store(self, mesh, result: ResultContainer):
        self._mesh_key = self.make_key(mesh)
        self._last_result = result

    def get(self):
        return self._last_result

    def is_valid(self, mesh):
        return (
            self._last_result is not None
            and self._mesh_key == self.make_key(mesh)
        )

    def clear(self):
        self._last_result = None
        self._mesh_key = None
