"""
MeshAnalyzer Pro
core/compare.py
"""

import numpy as np


class MeshCompare:

    def __init__(self, before_mesh, after_mesh):
        self.before = before_mesh
        self.after = after_mesh

        if self.before.rows != self.after.rows or self.before.cols != self.after.cols:
            raise ValueError("Mesh boyutları aynı değil.")

    def delta(self):
        return self.after.matrix - self.before.matrix

    def before_range(self):
        return self.before.total_range

    def after_range(self):
        return self.after.total_range

    def improvement_percent(self):
        before = self.before_range()
        after = self.after_range()

        if before == 0:
            return 0

        return ((before - after) / before) * 100

    def before_rms(self):
        return float(self.before.rms)

    def after_rms(self):
        return float(self.after.rms)

    def rms_improvement_percent(self):
        before = self.before_rms()
        after = self.after_rms()

        if before == 0:
            return 0

        return ((before - after) / before) * 100

    def coordinate_label(self, row, col):
        return f"X{col + 1} / Y{row + 1}"

    def regional_changes(self):
        before_abs = np.abs(self.before.matrix)
        after_abs = np.abs(self.after.matrix)
        improvement_map = before_abs - after_abs

        best_index = np.unravel_index(
            int(np.argmax(improvement_map)),
            improvement_map.shape
        )
        worst_index = np.unravel_index(
            int(np.argmin(improvement_map)),
            improvement_map.shape
        )

        best_row, best_col = best_index
        worst_row, worst_col = worst_index

        return {
            "best_location": self.coordinate_label(best_row, best_col),
            "best_value": float(improvement_map[best_row, best_col]),
            "worst_location": self.coordinate_label(worst_row, worst_col),
            "worst_value": float(improvement_map[worst_row, worst_col]),
        }

    def summary(self):
        d = self.delta()
        regional = self.regional_changes()

        return {
            "before_range": self.before_range(),
            "after_range": self.after_range(),
            "improvement": self.improvement_percent(),
            "before_rms": self.before_rms(),
            "after_rms": self.after_rms(),
            "rms_improvement": self.rms_improvement_percent(),
            "delta_min": float(np.min(d)),
            "delta_max": float(np.max(d)),
            "delta_avg": float(np.mean(d)),
            "delta_abs_max": float(np.max(np.abs(d))),
            **regional,
        }
