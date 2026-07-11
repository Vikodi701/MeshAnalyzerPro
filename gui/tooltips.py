"""
MeshAnalyzer Pro
Dashboard Tooltips
"""

from languages import LanguageManager


class ToolTips:

    @staticmethod
    def quality_status():
        return LanguageManager.text("tooltip_quality_status")

    @staticmethod
    def machine_health():
        return LanguageManager.text("tooltip_machine_health")

    @staticmethod
    def total_range():
        return LanguageManager.text("tooltip_total_range")

    @staticmethod
    def rms():
        return LanguageManager.text("tooltip_rms")

    @staticmethod
    def plane_deviation():
        return LanguageManager.text("tooltip_plane_deviation")

    @staticmethod
    def mesh_size():
        return LanguageManager.text("tooltip_mesh_size")

    @staticmethod
    def minimum():
        return LanguageManager.text("tooltip_minimum")

    @staticmethod
    def maximum():
        return LanguageManager.text("tooltip_maximum")

    @staticmethod
    def average():
        return LanguageManager.text("tooltip_average")

    @staticmethod
    def file_info():
        return LanguageManager.text("tooltip_file_info")

    @staticmethod
    def analysis_result():
        return LanguageManager.text("tooltip_analysis_result")
    
    @staticmethod
    def mesh_summary():
        return LanguageManager.text("tooltip_mesh_summary")
    