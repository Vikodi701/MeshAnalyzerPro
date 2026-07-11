"""
MeshAnalyzer Pro
Smart Diagnostic - Machine Health Score
"""

from core.tolerance import ToleranceEngine
from core.smart_diagnostic.twist import TwistAnalyzer
from core.smart_diagnostic.slope import SlopeAnalyzer


class HealthScore:

    def __init__(self, mesh):
        self.mesh = mesh
        self.tolerance = ToleranceEngine(mesh)
        self.twist = TwistAnalyzer(mesh)
        self.slope = SlopeAnalyzer(mesh)

    def calculate(self):
        tolerance = self.tolerance.check()

        score = 100.0

        range_ratio = tolerance["total_range"] / tolerance["max_total_range"]
        rms_ratio = tolerance["rms"] / tolerance["max_rms"]
        plane_ratio = tolerance["plane_deviation"] / tolerance["max_plane_deviation"]

        score -= max(0, (range_ratio - 0.5) * 30)
        score -= max(0, (rms_ratio - 0.5) * 25)
        score -= max(0, (plane_ratio - 0.5) * 25)

        score -= abs(self.slope.x_slope()) * 20
        score -= abs(self.slope.y_slope()) * 20
        score -= abs(self.twist.twist_value()) * 30

        score = max(0, min(100, score))

        # Ekranda skor tam sayı olarak gösterildiği için
        # etiket eşikleri görünen değere göre belirlenir.
        # Böylece 89.5 -> 90 görünüyorsa "Mükemmel",
        # 74.5 -> 75 görünüyorsa "İyi",
        # 49.5 -> 50 görünüyorsa "Kabul Edilebilir" olur.
        display_score = round(score)

        if display_score >= 90:
            status = "EXCELLENT"
            label = "Mükemmel"
            color = "#2ECC71"
        elif display_score >= 75:
            status = "GOOD"
            label = "İyi"
            color = "#27AE60"
        elif display_score >= 50:
            status = "ACCEPTABLE"
            label = "Kabul Edilebilir"
            color = "#F1C40F"
        else:
            status = "CRITICAL"
            label = "Kritik"
            color = "#E74C3C"

        return {
            "score": score,
            "status": status,
            "label": label,
            "color": color,
        }

    def report_text(self):
        result = self.calculate()

        return (
            "MACHINE HEALTH SCORE\n"
            "====================\n"
            f"Skor  : {result['score']:.1f} / 100\n"
            f"Durum : {result['label']}"
        )