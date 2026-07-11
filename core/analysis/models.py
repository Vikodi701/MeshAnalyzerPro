"""
MeshAnalyzer Pro
Analysis Models
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class GeometryResult:
    max_deviation: float
    rms_deviation: float
    x_slope: float
    y_slope: float
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class HealthResult:
    score: float
    status: str
    label: str
    color: str
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class TrendResult:
    status: str
    trend: str
    count: int
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class DiagnosticResult:
    issues: List[str]
    recommendation: Dict[str, Any]
    raw: Dict[str, Any] = field(default_factory=dict)


@dataclass
class AnalysisResult:
    mesh_name: str
    mesh_filename: str
    geometry: GeometryResult
    tolerance: Dict[str, Any]
    health: HealthResult
    trend: TrendResult
    diagnostic: DiagnosticResult
    diagnostic_report: List[str]
    tolerance_report: str
    trend_report: str
    smart_report: str
    elapsed_ms: float = 0.0
