"""
MeshAnalyzer Pro
Smart Diagnostic - Shim Recommendation
"""

from core.smart_diagnostic.corners import CornerAnalyzer


class ShimRecommender:

    def __init__(self, mesh):
        self.mesh = mesh
        self.corner_analyzer = CornerAnalyzer(mesh)

    def recommendations(self):
        summary = self.corner_analyzer.summary()
        deltas = summary["deltas"]

        names = self.corner_analyzer.names()

        result = {}

        for key, delta in deltas.items():
            if abs(delta) < 0.03:
                action = "Değişiklik gerekmez"
            elif delta > 0:
                action = "Shim ekle / yükselt"
            else:
                action = "Shim azalt / alçalt"

            result[key] = {
                "key": key,
                "name": names[key],
                "delta": delta,
                "action": action,
            }

        return result

    def strongest_recommendation(self):
        recs = self.recommendations()

        strongest_key = max(
            recs,
            key=lambda k: abs(recs[k]["delta"])
        )

        return recs[strongest_key]

    def summary(self):
        return {
            "recommendations": self.recommendations(),
            "strongest": self.strongest_recommendation(),
        }
