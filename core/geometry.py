"""
======================================================
MeshAnalyzer Pro
Geometry Engine
Version : 1.1
======================================================
"""

import numpy as np


class GeometryAnalyzer:

    def __init__(self, mesh):

        self.mesh = mesh

        self.Z = mesh.matrix

        self.rows = mesh.rows
        self.cols = mesh.cols

        self.X, self.Y = np.meshgrid(
            np.arange(self.cols),
            np.arange(self.rows)
        )

    #######################################################

    def best_fit_plane(self):

        A = np.c_[
            self.X.ravel(),
            self.Y.ravel(),
            np.ones(self.rows * self.cols)
        ]

        C, _, _, _ = np.linalg.lstsq(
            A,
            self.Z.ravel(),
            rcond=None
        )

        a, b, c = C

        plane = (
            a * self.X +
            b * self.Y +
            c
        )

        return plane

    #######################################################

    def deviation_map(self):

        plane = self.best_fit_plane()

        return self.Z - plane

    #######################################################

    def maximum_deviation(self):

        return float(
            np.max(
                np.abs(
                    self.deviation_map()
                )
            )
        )

    #######################################################

    def rms_deviation(self):

        dev = self.deviation_map()

        return float(
            np.sqrt(
                np.mean(dev ** 2)
            )
        )

    #######################################################

    def x_slope(self):

        plane = self.best_fit_plane()

        return float(
            plane[0][-1] - plane[0][0]
        )

    #######################################################

    def y_slope(self):

        plane = self.best_fit_plane()

        return float(
            plane[-1][0] - plane[0][0]
        )

    #######################################################

    def summary(self):

        return {

            "plane": self.best_fit_plane(),

            "deviation": self.deviation_map(),

            "max_deviation": self.maximum_deviation(),

            "rms_deviation": self.rms_deviation(),

            "x_slope": self.x_slope(),

            "y_slope": self.y_slope()

        }