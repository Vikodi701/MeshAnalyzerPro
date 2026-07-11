"""
MeshAnalyzer Pro
Smart Diagnostic - Corner Analysis
"""


class CornerAnalyzer:

    def __init__(self, mesh):
        self.mesh = mesh

    def corners(self):
        """
        Koordinat standardı:
        - Ön sıra = Y1 = mesh.values[0]
        - Arka sıra = Ymax = mesh.values[-1]
        - Sol = X1
        - Sağ = Xmax
        """
        return {
            "front_left": self.mesh.values[0][0],
            "front_right": self.mesh.values[0][-1],
            "rear_left": self.mesh.values[-1][0],
            "rear_right": self.mesh.values[-1][-1],
        }

    def names(self):
        return {
            "front_left": "Ön Sol",
            "front_right": "Ön Sağ",
            "rear_left": "Arka Sol",
            "rear_right": "Arka Sağ",
        }

    def average(self):
        c = self.corners()
        return sum(c.values()) / 4

    def lowest_corner(self):
        c = self.corners()
        return min(c, key=c.get)

    def highest_corner(self):
        c = self.corners()
        return max(c, key=c.get)

    def corner_deltas(self):
        avg = self.average()
        c = self.corners()

        return {
            key: avg - value
            for key, value in c.items()
        }

    def summary(self):
        c = self.corners()
        deltas = self.corner_deltas()
        names = self.names()

        lowest = self.lowest_corner()
        highest = self.highest_corner()

        return {
            "corners": c,
            "deltas": deltas,
            "average": self.average(),
            "lowest_key": lowest,
            "highest_key": highest,
            "lowest_name": names[lowest],
            "highest_name": names[highest],
            "lowest_value": c[lowest],
            "highest_value": c[highest],
        }