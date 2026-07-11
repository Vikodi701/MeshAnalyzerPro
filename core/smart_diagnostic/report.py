"""
MeshAnalyzer Pro
Smart Diagnostic - Report Generator
"""

from core.smart_diagnostic.engine import SmartDiagnosticEngine
from languages import LanguageManager


class SmartDiagnosticReport:

    def __init__(self, mesh):
        self.mesh = mesh
        self.engine = SmartDiagnosticEngine(mesh)

    def status_text(self, status):
        text = str(status).strip().upper()
        keys = {
            "PASS": "status_pass",
            "OK": "status_ok",
            "EXCELLENT": "status_excellent",
            "GOOD": "status_good",
            "WARNING": "status_warning",
            "WARN": "status_warning",
            "ACCEPTABLE": "status_acceptable",
            "FAIL": "status_fail",
            "ERROR": "status_error",
            "BAD": "status_bad",
            "CRITICAL": "status_critical",
        }

        key = keys.get(text)
        if not key:
            return str(status)

        translated = LanguageManager.text(key)
        return translated if translated != key else str(status)

    def text(self, key):
        return LanguageManager.text(key)

    def corner_name(self, key):
        return self.text(f"corner_{key}")

    def slope_direction(self, axis, value):
        if abs(value) < 0.03:
            return self.text(f"{axis}_axis_balanced")

        if axis == "x":
            if value > 0:
                return self.text("right_higher_than_left")
            return self.text("left_higher_than_right")

        if value > 0:
            return self.text("rear_higher_than_front")
        return self.text("front_higher_than_rear")

    def twist_direction(self, value):
        if abs(value) < 0.03:
            return self.text("no_significant_twist")

        if value > 0:
            return self.text("clockwise_twist")

        return self.text("counter_clockwise_twist")

    def twist_severity(self, value):
        value = abs(value)
        if value < 0.03:
            return self.text("severity_none")
        if value < 0.10:
            return self.text("severity_light")
        if value < 0.25:
            return self.text("severity_medium")
        return self.text("severity_high")

    def shim_action(self, delta):
        if abs(delta) < 0.03:
            return self.text("shim_no_change")
        if delta > 0:
            return self.text("shim_add_raise")
        return self.text("shim_reduce_lower")

    def tolerance_message(self, status):
        text = str(status).strip().upper()
        if text == "PASS":
            return self.text("mesh_within_tolerance")
        if text == "WARNING":
            return self.text("mesh_near_tolerance")
        if text == "FAIL":
            return self.text("mesh_out_of_tolerance")
        return str(status)

    def generate(self):
        result = self.engine.analyze()

        tolerance = result["tolerance"]
        corners = result["corners"]
        slopes = result["slopes"]
        twist = result["twist"]
        shim = result["shim"]
        issues = result["issues"]
        main = result["main_recommendation"]

        lines = []

        lines.append(self.text("quality_status").upper())
        lines.append("-" * 40)
        lines.append(
            f"{self.text('point_status')} : "
            f"{self.status_text(tolerance['status'])}"
        )
        lines.append(
            f"{self.text('message')} : "
            f"{self.tolerance_message(tolerance['status'])}"
        )
        lines.append("")

        lines.append(self.text("general_assessment").upper())
        lines.append("-" * 40)

        issue_lines = []
        if tolerance["status"] != "PASS":
            issue_lines.append(self.tolerance_message(tolerance["status"]))

        if abs(slopes["x_slope"]) > 0.05:
            issue_lines.append(self.slope_direction("x", slopes["x_slope"]))

        if abs(slopes["y_slope"]) > 0.05:
            issue_lines.append(self.slope_direction("y", slopes["y_slope"]))

        if abs(twist["twist"]) >= 0.03:
            issue_lines.append(self.twist_direction(twist["twist"]))

        if not issue_lines:
            lines.append(f"• {self.text('no_mechanical_issue')}")
        else:
            for issue in issue_lines:
                lines.append(f"• {issue}")

        lines.append("")

        lines.append(self.text("corner_analysis").upper())
        lines.append("-" * 40)
        lines.append(
            f"{self.text('lowest_corner')} : "
            f"{self.corner_name(corners['lowest_key'])} "
            f"({corners['lowest_value']:.4f} mm)"
        )
        lines.append(
            f"{self.text('highest_corner')} : "
            f"{self.corner_name(corners['highest_key'])} "
            f"({corners['highest_value']:.4f} mm)"
        )
        lines.append("")

        lines.append(self.text("slope_analysis").upper())
        lines.append("-" * 40)
        lines.append(f"{self.text('x_slope')} : {slopes['x_slope']:+.4f} mm")
        lines.append(f"{self.text('y_slope')} : {slopes['y_slope']:+.4f} mm")
        lines.append(
            f"{self.text('x_direction')}  : "
            f"{self.slope_direction('x', slopes['x_slope'])}"
        )
        lines.append(
            f"{self.text('y_direction')}  : "
            f"{self.slope_direction('y', slopes['y_slope'])}"
        )
        lines.append("")

        lines.append(self.text("twist_analysis").upper())
        lines.append("-" * 40)
        lines.append(
            f"{self.text('twist_value')} : {twist['twist']:+.4f} mm"
        )
        lines.append(
            f"{self.text('direction')} : "
            f"{self.twist_direction(twist['twist'])}"
        )
        lines.append(
            f"{self.text('severity')} : "
            f"{self.twist_severity(twist['twist'])}"
        )
        lines.append("")

        lines.append(self.text("shim_recommendations").upper())
        lines.append("-" * 40)

        sorted_recommendations = sorted(
            shim["recommendations"].items(),
            key=lambda pair: abs(pair[1]["delta"]),
            reverse=True
        )

        for index, (key, item) in enumerate(sorted_recommendations, start=1):
            lines.append(
                f"{index}. {self.corner_name(key):<10} : "
                f"{item['delta']:+.4f} mm  ->  "
                f"{self.shim_action(item['delta'])}"
            )

        lines.append("")
        lines.append(self.text("main_recommendation").upper())
        lines.append("-" * 40)
        lines.append(
            self.text("main_recommendation_sentence").format(
                name=self.corner_name(main.get("key", "")),
                delta=f"{main['delta']:+.4f}",
            )
        )
        lines.append(
            f"{self.text('action')} : {self.shim_action(main['delta'])}"
        )
        lines.append("")
        lines.append(self.text("recommended_action").upper())
        lines.append("-" * 40)
        lines.append(f"• {self.text('remeasure_after_adjustment')}")
        lines.append(f"• {self.text('apply_largest_shim_first')}")
        lines.append(f"• {self.text('run_auto_level_again')}")

        return "\n".join(lines)
