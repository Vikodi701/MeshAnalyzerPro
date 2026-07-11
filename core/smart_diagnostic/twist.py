"""
MeshAnalyzer Pro
Smart Diagnostic - Twist Analysis
"""


from core.smart_diagnostic.corners import CornerAnalyzer


class TwistAnalyzer:

    def __init__(self, mesh):
        self.mesh = mesh
        self.corner_analyzer = CornerAnalyzer(mesh)

    def twist_value(self):
        corners = self.corner_analyzer.corners()

        diagonal_1 = (
            corners["front_left"] +
            corners["rear_right"]
        ) / 2

        diagonal_2 = (
            corners["front_right"] +
            corners["rear_left"]
        ) / 2

        return diagonal_1 - diagonal_2

    def direction(self):
        twist = self.twist_value()

        if abs(twist) < 0.03:
            return "Belirgin burulma yok"

        if twist > 0:
            return "Saat yönü burulma eğilimi"

        return "Saat yönü tersi burulma eğilimi"

    def severity(self):
        twist = abs(self.twist_value())

        if twist < 0.03:
            return "Yok"

        if twist < 0.10:
            return "Hafif"

        if twist < 0.25:
            return "Orta"

        return "Yüksek"

    def summary(self):
        return {
            "twist": self.twist_value(),
            "direction": self.direction(),
            "severity": self.severity(),
        }