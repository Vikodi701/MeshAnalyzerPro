"""
======================================================
MeshAnalyzer Pro
Diagnostic Engine
Version : 1.2
======================================================
"""

from core.geometry import GeometryAnalyzer
from core.smart_diagnostic.corners import CornerAnalyzer
from languages import LanguageManager


class DiagnosticEngine:

    def __init__(self, mesh):

        self.mesh = mesh

        self.geometry = GeometryAnalyzer(mesh)

        self.corner_analyzer = CornerAnalyzer(mesh)

        self.geo = self.geometry.summary()

    def text(self, key):
        return LanguageManager.text(key)

    def corner_name(self, key):
        names = self.corner_analyzer.names()
        if key in names:
            return names[key]

        return self.text(f"corner_{key}")

    ###########################################################

    def analyze(self):

        report = []

        report.extend(self._table_analysis())
        report.extend(self._gantry_analysis())
        report.extend(self._corner_analysis())
        report.extend(self._surface_analysis())
        report.extend(self._recommendations())

        return report

    ###########################################################

    def _table_analysis(self):

        text = []

        dev = self.geo["max_deviation"]

        if dev < 0.05:

            text.append(f"OK {self.text('table_almost_flat')}")

        elif dev < 0.15:

            text.append(f"OK {self.text('table_good_condition')}")

        elif dev < 0.30:

            text.append(f"! {self.text('table_slight_warp')}")

        else:

            text.append(f"X {self.text('table_serious_warp')}")

        text.append("")

        return text

    ###########################################################

    def _gantry_analysis(self):

        text = []

        x = self.geo["x_slope"]
        y = self.geo["y_slope"]

        if abs(x) > 0.20:

            if x > 0:

                text.append(
                    f"! {self.text('x_right_side_high')}"
                )

            else:

                text.append(
                    f"! {self.text('x_left_side_high')}"
                )

        else:

            text.append(
                f"OK {self.text('x_axis_balanced')}"
            )

        if abs(y) > 0.20:

            if y > 0:

                text.append(
                    f"! {self.text('rear_higher_than_front')}"
                )

            else:

                text.append(
                    f"! {self.text('front_higher_than_rear')}"
                )

        else:

            text.append(
                f"OK {self.text('y_axis_balanced')}"
            )

        text.append("")

        return text

    ###########################################################

    def _corner_analysis(self):

        text = []

        # Aynı koordinat standardı kullanılır:
        # Ön Sol  = X1 / Y1
        # Ön Sağ  = Xmax / Y1
        # Arka Sol = X1 / Ymax
        # Arka Sağ = Xmax / Ymax
        c = self.corner_analyzer.corners()

        lowest = min(c, key=c.get)
        highest = max(c, key=c.get)

        text.append(
            f"{self.text('lowest_corner')} : {self.corner_name(lowest)}"
        )

        text.append(
            f"{self.text('highest_corner')} : {self.corner_name(highest)}"
        )

        text.append("")

        return text

    ###########################################################

    def _surface_analysis(self):

        text = []

        rms = self.geo["rms_deviation"]

        if rms < 0.03:

            text.append(
                f"OK {self.text('surface_very_smooth')}"
            )

        elif rms < 0.08:

            text.append(
                f"OK {self.text('surface_acceptable')}"
            )

        elif rms < 0.15:

            text.append(
                f"! {self.text('surface_local_waves')}"
            )

        else:

            text.append(
                f"X {self.text('surface_serious_deformation')}"
            )

        text.append("")

        return text

    ###########################################################

    def _recommendations(self):

        text = []

        text.append(self.text("mechanical_priority_recommendations").upper())
        text.append("-" * 40)

        # Mekanik önerilerde de aynı köşe eşlemesi kullanılmalı.
        c = self.corner_analyzer.corners()

        avg = sum(c.values()) / 4

        recommendations = []

        for key, value in c.items():

            delta = avg - value

            if abs(delta) < 0.03:

                continue

            direction = self.text("raise")

            if delta < 0:
                direction = self.text("lower")

            recommendations.append(
                {
                    "key": key,
                    "name": self.corner_name(key),
                    "direction": direction,
                    "delta": delta,
                    "amount": abs(delta),
                }
            )

        recommendations.sort(
            key=lambda item: item["amount"],
            reverse=True
        )

        if not recommendations:
            text.append(f"OK {self.text('no_priority_correction_needed')}")
            return text

        text.append(self.text("apply_largest_correction_first"))

        for index, item in enumerate(recommendations, start=1):

            text.append(
                f"{index}. {item['name']} -> "
                f"{item['direction']} ({item['amount']:.3f} mm)"
            )

        text.append("")
        text.append(f"• {self.text('remeasure_after_adjustment')}")
        text.append(f"• {self.text('run_auto_level_again')}")

        return text
