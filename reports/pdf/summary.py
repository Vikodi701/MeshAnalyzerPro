"""
MeshAnalyzer Pro
PDF Summary Builder
"""


class SummaryBuilder:

    def build(self, analysis):
        return {
            "mesh_name": analysis.mesh_name,
            "health_score": analysis.health.score,
            "health_label": analysis.health.label,
            "tolerance_status": analysis.tolerance["status"],
            "trend": analysis.trend.trend,
        }