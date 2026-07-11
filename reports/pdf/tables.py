"""
MeshAnalyzer Pro
PDF Table Builder
"""

from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors

from .styles import TABLE_HEADER_COLOR, TABLE_GRID_COLOR


class TableBuilder:

    @staticmethod
    def create(data):
        table = Table(data)

        table.setStyle(
            TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), TABLE_HEADER_COLOR),
                ("GRID", (0, 0), (-1, -1), 0.5, TABLE_GRID_COLOR),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
            ])
        )

        return table