"""
MeshAnalyzer Pro
PDF Styles
"""

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER

styles = getSampleStyleSheet()

TITLE_STYLE = styles["Heading1"]
TITLE_STYLE.alignment = TA_CENTER
TITLE_STYLE.textColor = colors.HexColor("#1F4E79")

HEADING_STYLE = styles["Heading2"]
HEADING_STYLE.textColor = colors.HexColor("#2F75B5")

NORMAL_STYLE = styles["BodyText"]

TABLE_HEADER_COLOR = colors.HexColor("#D9EAD3")
TABLE_GRID_COLOR = colors.grey