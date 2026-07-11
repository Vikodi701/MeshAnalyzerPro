"""
MeshAnalyzer Pro
Tolerance Engine
PASS / ACCEPTABLE / WARNING / FAIL
"""

from core.geometry import GeometryAnalyzer
from core.config import Config


class ToleranceEngine:

    def __init__(self, mesh, warning_ratio=0.80):

        self.mesh = mesh

        cfg = Config()

        self.max_total_range = cfg.get("max_total_range")
        self.max_rms = cfg.get("max_rms")
        self.max_plane_deviation = cfg.get("max_plane_deviation")

        self.warning_ratio = warning_ratio

        self.geometry = GeometryAnalyzer(mesh)
        self.geo = self.geometry.summary()

    def check_value(self, value, limit):

        acceptable_limit = limit * self.warning_ratio
        warning_limit = limit
        fail_limit = limit * 1.20

        if value <= acceptable_limit:
            return "PASS"

        if value <= warning_limit:
            return "ACCEPTABLE"

        if value <= fail_limit:
            return "WARNING"

        return "FAIL"

    def check(self):

        total_range = self.mesh.total_range
        rms = self.mesh.rms
        plane = self.geo["max_deviation"]

        range_status = self.check_value(
            total_range,
            self.max_total_range
        )

        rms_status = self.check_value(
            rms,
            self.max_rms
        )

        plane_status = self.check_value(
            plane,
            self.max_plane_deviation
        )

        if (
            range_status == "FAIL"
            or rms_status == "FAIL"
            or plane_status == "FAIL"
        ):

            status = "FAIL"
            message = "Mesh tolerans dışında."

        elif (
            range_status == "WARNING"
            or rms_status == "WARNING"
            or plane_status == "WARNING"
        ):

            status = "WARNING"
            message = "Mesh tolerans üstünde, kontrol önerilir."

        elif (
            range_status == "ACCEPTABLE"
            or rms_status == "ACCEPTABLE"
            or plane_status == "ACCEPTABLE"
        ):

            status = "ACCEPTABLE"
            message = "Mesh kabul edilebilir aralıkta."

        else:

            status = "PASS"
            message = "Mesh tolerans içinde."

        return {

            "status": status,

            "message": message,

            "total_range": total_range,

            "max_total_range": self.max_total_range,

            "range_status": range_status,

            "rms": rms,

            "max_rms": self.max_rms,

            "rms_status": rms_status,

            "plane_deviation": plane,

            "max_plane_deviation": self.max_plane_deviation,

            "plane_status": plane_status

        }

    def report_text(self):

        result = self.check()

        report = []

        report.append("KALİTE KONTROL")
        report.append("=" * 50)
        report.append(f"Durum : {result['status']}")
        report.append(result["message"])
        report.append("")

        report.append(
            f"Toplam Sapma : "
            f"{result['total_range']:.4f} mm"
        )

        report.append(
            f"Limit : "
            f"{result['max_total_range']:.4f} mm"
        )

        report.append(
            f"Sonuç : "
            f"{result['range_status']}"
        )

        report.append("")

        report.append(
            f"RMS : "
            f"{result['rms']:.4f} mm"
        )

        report.append(
            f"Limit : "
            f"{result['max_rms']:.4f} mm"
        )

        report.append(
            f"Sonuç : "
            f"{result['rms_status']}"
        )

        report.append("")

        report.append(
            f"Düzlem Sapması : "
            f"{result['plane_deviation']:.4f} mm"
        )

        report.append(
            f"Limit : "
            f"{result['max_plane_deviation']:.4f} mm"
        )

        report.append(
            f"Sonuç : "
            f"{result['plane_status']}"
        )

        return "\n".join(report)