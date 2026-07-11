"""
MeshAnalyzer Pro
Unified Analysis Engine
"""

from __future__ import annotations

import time
from typing import Any, Dict, List, Tuple

from utils.logger import logger

from core.geometry import GeometryAnalyzer
from core.diagnostics import DiagnosticEngine
from core.tolerance import ToleranceEngine
from core.trend.analyzer import TrendAnalyzer
from core.smart_diagnostic.health import HealthScore
from core.smart_diagnostic.engine import SmartDiagnosticEngine
from core.smart_diagnostic.report import SmartDiagnosticReport

from .cache import AnalysisCache
from .models import (
    AnalysisResult,
    GeometryResult,
    HealthResult,
    TrendResult,
    DiagnosticResult,
)
from .result import ResultContainer


class AnalysisEngine:

    def __init__(self, mesh, use_cache: bool = True):
        self.mesh = mesh
        self.use_cache = use_cache
        self.cache = AnalysisCache.instance()

    def run(self) -> ResultContainer:
        if self.use_cache and self.cache.is_valid(self.mesh):
            logger.info("Analysis cache kullanıldı: %s", self.mesh.name)
            return self.cache.get()

        start = time.perf_counter()

        logger.info("Analysis başladı: %s", self.mesh.name)

        geometry_raw = self._run_geometry()
        tolerance_raw, tolerance_text = self._run_tolerance()
        health_raw = self._run_health()
        trend_raw, trend_text = self._run_trend()
        diagnostic_raw, diagnostic_lines = self._run_diagnostics()
        smart_raw, smart_text = self._run_smart_diagnostic()

        elapsed_ms = (time.perf_counter() - start) * 1000

        result = AnalysisResult(
            mesh_name=self.mesh.name,
            mesh_filename=self.mesh.filename,
            geometry=self._build_geometry_result(geometry_raw),
            tolerance=tolerance_raw,
            health=self._build_health_result(health_raw),
            trend=self._build_trend_result(trend_raw),
            diagnostic=self._build_diagnostic_result(smart_raw),
            diagnostic_report=diagnostic_lines,
            tolerance_report=tolerance_text,
            trend_report=trend_text,
            smart_report=smart_text,
            elapsed_ms=elapsed_ms,
        )

        container = ResultContainer(result)
        self.cache.store(self.mesh, container)

        logger.info(
            "Analysis bitti: %s | %.2f ms",
            self.mesh.name,
            elapsed_ms,
        )

        return container

    def _run_geometry(self) -> Dict[str, Any]:
        logger.info("Geometry hesaplanıyor.")
        return GeometryAnalyzer(self.mesh).summary()

    def _run_tolerance(self) -> Tuple[Dict[str, Any], str]:
        logger.info("Tolerance hesaplanıyor.")
        engine = ToleranceEngine(self.mesh)
        return engine.check(), engine.report_text()

    def _run_health(self) -> Dict[str, Any]:
        logger.info("Health Score hesaplanıyor.")
        return HealthScore(self.mesh).calculate()

    def _run_trend(self) -> Tuple[Dict[str, Any], str]:
        logger.info("Trend hesaplanıyor.")
        analyzer = TrendAnalyzer()
        return analyzer.analyze(), analyzer.report_text()

    def _run_diagnostics(self) -> Tuple[Dict[str, Any], List[str]]:
        logger.info("Klasik diagnostics hesaplanıyor.")
        lines = DiagnosticEngine(self.mesh).analyze()
        return {"lines": lines}, lines

    def _run_smart_diagnostic(self) -> Tuple[Dict[str, Any], str]:
        logger.info("Smart Diagnostic hesaplanıyor.")
        raw = SmartDiagnosticEngine(self.mesh).analyze()
        text = SmartDiagnosticReport(self.mesh).generate()
        return raw, text

    def _build_geometry_result(self, raw: Dict[str, Any]) -> GeometryResult:
        return GeometryResult(
            max_deviation=float(raw["max_deviation"]),
            rms_deviation=float(raw["rms_deviation"]),
            x_slope=float(raw["x_slope"]),
            y_slope=float(raw["y_slope"]),
            raw=raw,
        )

    def _build_health_result(self, raw: Dict[str, Any]) -> HealthResult:
        return HealthResult(
            score=float(raw["score"]),
            status=str(raw["status"]),
            label=str(raw["label"]),
            color=str(raw["color"]),
            raw=raw,
        )

    def _build_trend_result(self, raw: Dict[str, Any]) -> TrendResult:
        return TrendResult(
            status=str(raw.get("status", "")),
            trend=str(raw.get("trend", "")),
            count=int(raw.get("count", 0)),
            raw=raw,
        )

    def _build_diagnostic_result(self, raw: Dict[str, Any]) -> DiagnosticResult:
        return DiagnosticResult(
            issues=list(raw.get("issues", [])),
            recommendation=dict(raw.get("main_recommendation", {})),
            raw=raw,
        )
