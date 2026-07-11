"""
MeshAnalyzer Pro
Analysis Result Wrapper
"""

from .models import AnalysisResult


class ResultContainer:

    def __init__(self, result: AnalysisResult):
        self.result = result

    @property
    def mesh_name(self):
        return self.result.mesh_name

    @property
    def mesh_filename(self):
        return self.result.mesh_filename

    @property
    def geometry(self):
        return self.result.geometry

    @property
    def tolerance(self):
        return self.result.tolerance

    @property
    def health(self):
        return self.result.health

    @property
    def trend(self):
        return self.result.trend

    @property
    def diagnostic(self):
        return self.result.diagnostic

    @property
    def diagnostic_report(self):
        return self.result.diagnostic_report

    @property
    def tolerance_report(self):
        return self.result.tolerance_report

    @property
    def trend_report(self):
        return self.result.trend_report

    @property
    def smart_report(self):
        return self.result.smart_report

    @property
    def elapsed_ms(self):
        return self.result.elapsed_ms
