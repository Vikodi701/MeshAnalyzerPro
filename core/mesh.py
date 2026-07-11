"""
======================================================
MeshAnalyzer Pro
Mesh Data Model
Version : 1.0
======================================================
"""

from dataclasses import dataclass, field
from typing import List
import numpy as np


@dataclass
class Mesh:

    name: str = ""

    filename: str = ""

    values: List[List[float]] = field(default_factory=list)

    ##########################################################

    @property
    def rows(self):

        return len(self.values)

    ##########################################################

    @property
    def cols(self):

        if self.rows == 0:
            return 0

        return len(self.values[0])

    ##########################################################

    @property
    def matrix(self):

        return np.array(self.values)

    ##########################################################

    @property
    def minimum(self):

        return float(np.min(self.matrix))

    ##########################################################

    @property
    def maximum(self):

        return float(np.max(self.matrix))

    ##########################################################

    @property
    def average(self):

        return float(np.mean(self.matrix))

    ##########################################################

    @property
    def std(self):

        return float(np.std(self.matrix))

    ##########################################################

    @property
    def rms(self):

        return float(np.sqrt(np.mean(self.matrix ** 2)))

    ##########################################################

    @property
    def total_range(self):

        return self.maximum - self.minimum

    ##########################################################

    def corner(self):

        # Koordinat standardı:
        # Ön Sol  = X1 / Y1
        # Ön Sağ  = Xmax / Y1
        # Arka Sol = X1 / Ymax
        # Arka Sağ = Xmax / Ymax
        return {

            "front_left": self.values[0][0],

            "front_right": self.values[0][-1],

            "rear_left": self.values[-1][0],

            "rear_right": self.values[-1][-1]

        }

    ##########################################################

    def info(self):

        return {

            "rows": self.rows,

            "cols": self.cols,

            "min": self.minimum,

            "max": self.maximum,

            "avg": self.average,

            "std": self.std,

            "rms": self.rms,

            "range": self.total_range,

            "corners": self.corner()

        }