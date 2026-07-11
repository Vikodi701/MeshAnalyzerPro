from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np

from core.config import Config
from languages import LanguageManager


class ContourWidget(FigureCanvasQTAgg):

    def __init__(self):
        self.figure = Figure()
        super().__init__(self.figure)

        self.axes = None
        self.cbar_ax = None

        self.mesh = None
        self.data = None
        self.contour = None
        self.lines = None
        self.cbar = None
        self.cmap_name = "terrain"
        self.theme_name = None
        self.filled_levels = 20
        self.line_levels = 10

        self.show_empty_state()

    def apply_canvas_background(self):
        colors = self.theme_colors()
        self.figure.patch.set_facecolor(colors["figure_bg"])
        self.figure.set_facecolor(colors["figure_bg"])
        self.setStyleSheet(
            f"background-color: {colors['figure_bg']}; border: none;"
        )
        return colors

    def show_empty_state(self):
        self.figure.clear()
        self.cbar_ax = None
        self.data = None
        self.contour = None
        self.lines = None
        self.cbar = None

        colors = self.apply_canvas_background()

        self.axes = self.figure.add_axes([0.0, 0.0, 1.0, 1.0])
        self.axes.set_axis_off()
        self.axes.set_facecolor(colors["figure_bg"])

        self.axes.text(
            0.5,
            0.55,
            LanguageManager.text("empty_conf_waiting_title"),
            ha="center",
            va="center",
            color=colors["text"],
            fontsize=18,
            fontweight="bold",
            transform=self.axes.transAxes,
        )

        self.axes.text(
            0.5,
            0.47,
            LanguageManager.text("empty_conf_waiting_message"),
            ha="center",
            va="center",
            color=colors.get("muted", colors["text"]),
            fontsize=11,
            alpha=0.90,
            transform=self.axes.transAxes,
        )

        self.draw()

    def clear(self):
        self.mesh = None
        self.show_empty_state()

    def coordinate_mm(self, index):
        return 5 + index * 60

    def set_theme_name(self, theme_name):
        if theme_name:
            self.theme_name = str(theme_name)

    def theme_colors(self):
        theme = str(self.theme_name or Config().get("theme"))

        if theme == "light":
            return {
                "figure_bg": "#F8FAFC",
                "axes_bg": "#FFFFFF",
                "text": "#0F172A",
                "muted": "#64748B",
                "grid": "#CBD5E1",
                "line": "#0F172A",
            }

        return {
            "figure_bg": "#0F172A",
            "axes_bg": "#0F172A",
            "text": "#F8FAFC",
            "muted": "#CBD5E1",
            "grid": "#334155",
            "line": "#F8FAFC",
        }

    def apply_theme(self):
        colors = self.theme_colors()

        self.figure.patch.set_facecolor(colors["figure_bg"])
        self.figure.set_facecolor(colors["figure_bg"])
        self.setStyleSheet(
            f"background-color: {colors['figure_bg']}; border: none;"
        )

        if self.axes is not None:
            self.axes.set_facecolor(colors["axes_bg"])
            self.axes.tick_params(colors=colors["text"])
            self.axes.xaxis.label.set_color(colors["text"])
            self.axes.yaxis.label.set_color(colors["text"])
            self.axes.title.set_color(colors["text"])

            for spine in self.axes.spines.values():
                spine.set_color(colors["grid"])

        if self.cbar_ax is not None:
            self.cbar_ax.set_facecolor(colors["figure_bg"])

        return colors

    def layout_axes(self):
        self.figure.clear()

        canvas_width = max(self.width(), 1)
        canvas_height = max(self.height(), 1)
        figure_ratio = canvas_width / canvas_height

        cbar_width = 0.025
        gap = 0.035

        max_map_width = 0.70
        max_map_height = 0.82

        map_width = min(
            max_map_width,
            max_map_height / figure_ratio
        )
        map_height = map_width * figure_ratio

        group_width = map_width + gap + cbar_width
        group_left = (1.0 - group_width) / 2.0

        map_left = group_left
        map_bottom = (1.0 - map_height) / 2.0

        cbar_left = map_left + map_width + gap
        cbar_height = min(0.70, map_height * 0.86)
        cbar_bottom = map_bottom + (map_height - cbar_height) / 2.0

        self.axes = self.figure.add_axes(
            [
                map_left,
                map_bottom,
                map_width,
                map_height,
            ]
        )

        self.cbar_ax = self.figure.add_axes(
            [
                cbar_left,
                cbar_bottom,
                cbar_width,
                cbar_height,
            ]
        )

    def plot(self, mesh, cmap="terrain", filled_levels=20, line_levels=10):
        self.mesh = mesh
        self.cmap_name = cmap
        self.filled_levels = filled_levels
        self.line_levels = line_levels

        self.layout_axes()
        colors = self.apply_theme()

        self.data = mesh.matrix
        rows, cols = self.data.shape

        x = np.array(
            [
                self.coordinate_mm(i)
                for i in range(cols)
            ]
        )

        y = np.array(
            [
                self.coordinate_mm(i)
                for i in range(rows)
            ]
        )

        X, Y = np.meshgrid(x, y)

        self.contour = self.axes.contourf(
            X,
            Y,
            self.data,
            levels=filled_levels,
            cmap=cmap
        )

        self.lines = self.axes.contour(
            X,
            Y,
            self.data,
            levels=line_levels,
            colors=colors["line"],
            linewidths=0.7,
            alpha=0.85
        )

        self.axes.clabel(
            self.lines,
            inline=True,
            fontsize=8,
            colors=colors["line"]
        )

        self.axes.set_xlabel(
            "X (mm)",
            fontsize=11,
            color=colors["text"]
        )

        self.axes.set_ylabel(
            "Y (mm)",
            fontsize=11,
            color=colors["text"]
        )

        self.axes.set_xticks(x)
        self.axes.set_yticks(y)

        self.axes.grid(
            True,
            color=colors["grid"],
            linewidth=0.5,
            alpha=0.45
        )

        self.axes.set_aspect(
            "equal",
            adjustable="box"
        )

        self.cbar = None
        if bool(Config().get("appearance_show_colorbar")):
            self.cbar_ax.set_visible(True)
            self.cbar = self.figure.colorbar(
                self.contour,
                cax=self.cbar_ax
            )

            self.cbar.set_label(
                "mm",
                fontsize=10,
                color=colors["text"]
            )

            self.cbar.ax.yaxis.set_tick_params(
                color=colors["text"]
            )

            for label in self.cbar.ax.get_yticklabels():
                label.set_color(colors["text"])

            for spine in self.cbar.ax.spines.values():
                spine.set_color(colors["grid"])
        else:
            self.cbar_ax.set_visible(False)

        self.draw()


    def refresh_theme(self, theme_name=None):
        if theme_name:
            self.theme_name = str(theme_name)

        if self.mesh is None:
            self.show_empty_state()
            return

        self.plot(
            self.mesh,
            cmap=self.cmap_name,
            filled_levels=self.filled_levels,
            line_levels=self.line_levels
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.mesh is not None:
            self.plot(
                self.mesh,
                cmap=self.cmap_name,
                filled_levels=self.filled_levels,
                line_levels=self.line_levels
            )
