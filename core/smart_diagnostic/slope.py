"""
MeshAnalyzer Pro
Smart Diagnostic - Slope Analysis
"""


class SlopeAnalyzer:

    def __init__(self, mesh):
        self.mesh = mesh

    def x_slope(self):
        left_values = []
        right_values = []

        for row in self.mesh.values:
            left_values.append(row[0])
            right_values.append(row[-1])

        left_avg = sum(left_values) / len(left_values)
        right_avg = sum(right_values) / len(right_values)

        return right_avg - left_avg

    def y_slope(self):
        # Ön sıra Y1, arka sıra Ymax kabul edilir.
        front = self.mesh.values[0]
        rear = self.mesh.values[-1]

        rear_avg = sum(rear) / len(rear)
        front_avg = sum(front) / len(front)

        return rear_avg - front_avg

    def x_direction(self):
        slope = self.x_slope()

        if abs(slope) < 0.03:
            return "X ekseni dengeli"

        if slope > 0:
            return "Sağ taraf sol tarafa göre yüksek"

        return "Sol taraf sağ tarafa göre yüksek"

    def y_direction(self):
        slope = self.y_slope()

        if abs(slope) < 0.03:
            return "Y ekseni dengeli"

        if slope > 0:
            return "Arka taraf ön tarafa göre yüksek"

        return "Ön taraf arka tarafa göre yüksek"

    def summary(self):
        return {
            "x_slope": self.x_slope(),
            "y_slope": self.y_slope(),
            "x_direction": self.x_direction(),
            "y_direction": self.y_direction(),
        }