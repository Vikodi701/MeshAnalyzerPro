"""
MeshAnalyzer Pro
Trend Analysis Engine
Language-aware report output
"""

from database.database import Database
from languages import LanguageManager


class TrendAnalyzer:

    def __init__(self):
        self.db = Database()

    def text(self, key):
        return LanguageManager.text(key)

    def load_history(self):
        rows = self.db.get_history()
        return list(reversed(rows))

    def localized_trend(self, status):
        mapping = {
            "NO_DATA": "trend_no_data",
            "IMPROVING": "trend_improving",
            "DEGRADING": "trend_degrading",
            "STABLE": "trend_stable",
        }
        return self.text(mapping.get(status, "trend_stable"))

    def analyze(self):
        rows = self.load_history()

        if len(rows) < 2:
            status = "NO_DATA"
            trend = self.localized_trend(status)
            return {
                "status": status,
                "message": self.text("trend_min_records_required"),
                "count": len(rows),
                "range_change": 0.0,
                "rms_change": 0.0,
                "trend": trend,
            }

        first = rows[0]
        last = rows[-1]

        first_range = float(first[7])
        last_range = float(last[7])

        first_rms = float(first[8])
        last_rms = float(last[8])

        range_change = last_range - first_range
        rms_change = last_rms - first_rms

        if range_change < -0.05 and rms_change < -0.02:
            status = "IMPROVING"

        elif range_change > 0.05 or rms_change > 0.02:
            status = "DEGRADING"

        else:
            status = "STABLE"

        trend = self.localized_trend(status)

        return {
            "status": status,
            "message": trend,
            "count": len(rows),

            "first_range": first_range,
            "last_range": last_range,
            "range_change": range_change,

            "first_rms": first_rms,
            "last_rms": last_rms,
            "rms_change": rms_change,

            "trend": trend,
        }

    def report_text(self):
        result = self.analyze()

        lines = []

        lines.append(
            f"{self.text('trend_record_count')} : {result['count']}"
        )
        lines.append(
            f"{self.text('trend_status')}        : {result['trend']}"
        )

        if result["status"] == "NO_DATA":
            lines.append("")
            lines.append(result["message"])
            return "\n".join(lines)

        lines.append("")

        lines.append(
            f"{self.text('trend_first_total_deviation')} : "
            f"{result['first_range']:.4f} mm"
        )

        lines.append(
            f"{self.text('trend_last_total_deviation')}  : "
            f"{result['last_range']:.4f} mm"
        )

        lines.append(
            f"{self.text('trend_change')}                : "
            f"{result['range_change']:+.4f} mm"
        )

        lines.append("")

        lines.append(
            f"{self.text('trend_first_rms')} : "
            f"{result['first_rms']:.4f} mm"
        )

        lines.append(
            f"{self.text('trend_last_rms')}  : "
            f"{result['last_rms']:.4f} mm"
        )

        lines.append(
            f"{self.text('trend_change')}    : "
            f"{result['rms_change']:+.4f} mm"
        )

        return "\n".join(lines)
