"""
MeshAnalyzer Pro
PDF Canvas Utilities
"""

from reportlab.lib.pagesizes import A4


class PDFCanvasUtils:

    def __init__(self, font_name, font_bold):
        self.font_name = font_name
        self.font_bold = font_bold

    def draw_title(self, c, title, y):
        c.setFont(self.font_bold, 14)
        c.drawString(50, y, title)
        return y - 22

    def draw_text_lines(self, c, lines, x, y, line_height=15, font_size=10):
        width, height = A4
        c.setFont(self.font_name, font_size)

        for line in lines:
            if y < 60:
                c.showPage()
                y = height - 50
                c.setFont(self.font_name, font_size)

            c.drawString(x, y, str(line))
            y -= line_height

        return y

    def draw_report_block(self, c, title, text, y):
        width, height = A4

        if y < 120:
            c.showPage()
            y = height - 50

        y = self.draw_title(c, title, y)

        lines = str(text).splitlines()
        y = self.draw_text_lines(c, lines, 50, y, 15, 10)

        return y - 15