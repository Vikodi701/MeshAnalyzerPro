"""
MeshAnalyzer Pro
Smart Diagnostic - Main Engine
"""

from core.tolerance import ToleranceEngine

from core.smart_diagnostic.corners import CornerAnalyzer
from core.smart_diagnostic.slope import SlopeAnalyzer
from core.smart_diagnostic.twist import TwistAnalyzer
from core.smart_diagnostic.shim import ShimRecommender


class SmartDiagnosticEngine:

    def __init__(self, mesh):
        self.mesh = mesh

        self.corner_analyzer = CornerAnalyzer(mesh)
        self.slope_analyzer = SlopeAnalyzer(mesh)
        self.twist_analyzer = TwistAnalyzer(mesh)
        self.shim_recommender = ShimRecommender(mesh)
        self.tolerance = ToleranceEngine(mesh)

    def analyze(self):
        corners = self.corner_analyzer.summary()
        slopes = self.slope_analyzer.summary()
        twist = self.twist_analyzer.summary()
        shim = self.shim_recommender.summary()
        tolerance = self.tolerance.check()

        issues = []

        if tolerance["status"] != "PASS":
            issues.append(tolerance["message"])

        if abs(slopes["x_slope"]) > 0.05:
            issues.append(slopes["x_direction"])

        if abs(slopes["y_slope"]) > 0.05:
            issues.append(slopes["y_direction"])

        if twist["severity"] != "Yok":
            issues.append(twist["direction"])

        strongest = shim["strongest"]

        return {
            "tolerance": tolerance,
            "corners": corners,
            "slopes": slopes,
            "twist": twist,
            "shim": shim,
            "issues": issues,
            "main_recommendation": strongest,
        }