"""
MeshAnalyzer Pro
PDF Chart Builder
"""


class ChartBuilder:

    def build(self, analysis):
        return {
            "trend_status": analysis.trend.status,
            "trend_label": analysis.trend.trend,
        }