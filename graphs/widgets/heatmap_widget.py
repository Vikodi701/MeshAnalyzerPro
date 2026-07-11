from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.patches import Rectangle
import numpy as np

from core.config import Config
from languages import LanguageManager


class HeatmapWidget(FigureCanvasQTAgg):
    """
    MeshAnalyzer Pro
    Responsive Heatmap Widget
    """

    def __init__(self):
        self.figure = Figure()
        super().__init__(self.figure)

        self.axes = None
        self.cbar_ax = None

        self.mesh = None
        self.data = None
        self.image = None
        self.cbar = None
        self.cmap_name = "coolwarm"
        self.theme_name = None

        self.hover_rect = None
        self.cbar_marker = None

        self.mpl_connect(
            "motion_notify_event",
            self.on_mouse_move
        )

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
        self.image = None
        self.cbar = None
        self.hover_rect = None
        self.cbar_marker = None

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
                # Canvas background: navigation/sidebar ile aynı ana zemin
                "figure_bg": "#F8FAFC",
                # Actual plotting area
                "axes_bg": "#FFFFFF",
                "text": "#0F172A",
                "muted": "#64748B",
                "grid": "#CBD5E1",
                "hover": "#0284C7",
            }

        return {
            # Canvas background: navigation/sidebar ile aynı ana zemin
            "figure_bg": "#0F172A",
            # Actual plotting area
            "axes_bg": "#0F172A",
            "text": "#F8FAFC",
            "muted": "#CBD5E1",
            "grid": "#334155",
            "hover": "#38BDF8",
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

            for spine in self.axes.spines.values():
                spine.set_color(colors["grid"])

        if self.cbar_ax is not None:
            self.cbar_ax.set_facecolor(colors["figure_bg"])

        return colors

    def layout_axes(self):
        self.figure.clear()

        cbar_width = 0.025
        gap = 0.035

        heat_width = 0.56
        group_width = heat_width + gap + cbar_width
        group_left = (1.0 - group_width) / 2.0

        heat_left = group_left
        heat_bottom = 0.12
        heat_height = 0.78

        cbar_left = heat_left + heat_width + gap
        cbar_bottom = 0.16
        cbar_height = 0.70

        self.axes = self.figure.add_axes(
            [
                heat_left,
                heat_bottom,
                heat_width,
                heat_height,
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

    def plot(self, mesh, cmap="coolwarm"):
        self.mesh = mesh
        self.cmap_name = cmap

        self.layout_axes()

        self.hover_rect = None
        self.cbar_marker = None

        colors = self.apply_theme()

        self.data = mesh.matrix

        self.image = self.axes.imshow(
            self.data,
            origin="lower",
            cmap=cmap,
            aspect="equal"
        )

        rows, cols = self.data.shape

        x_coords = [
            self.coordinate_mm(i)
            for i in range(cols)
        ]

        y_coords = [
            self.coordinate_mm(i)
            for i in range(rows)
        ]

        self.axes.set_xticks(range(cols))
        self.axes.set_yticks(range(rows))

        self.axes.set_xticklabels(
            [f"{value} mm" for value in x_coords],
            fontsize=10,
            color=colors["text"]
        )

        self.axes.set_yticklabels(
            [f"{value} mm" for value in y_coords],
            fontsize=10,
            color=colors["text"]
        )

        for y in range(rows):
            for x in range(cols):
                value = self.data[y, x]

                self.axes.text(
                    x,
                    y,
                    f"{value:.3f}",
                    ha="center",
                    va="center",
                    color="#FFFFFF",
                    fontsize=10,
                    fontweight="bold"
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

        self.cbar = None
        if bool(Config().get("appearance_show_colorbar")):
            self.cbar_ax.set_visible(True)
            self.cbar = self.figure.colorbar(
                self.image,
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

    def on_mouse_move(self, event):
        if self.data is None or self.image is None:
            return

        if event.inaxes != self.axes:
            self.clear_hover()
            return

        if event.xdata is None or event.ydata is None:
            self.clear_hover()
            return

        x = int(round(event.xdata))
        y = int(round(event.ydata))

        rows, cols = self.data.shape

        if x < 0 or x >= cols or y < 0 or y >= rows:
            self.clear_hover()
            return

        value = self.data[y, x]

        self.update_hover_cell(x, y)
        if self.cbar is not None:
            self.update_colorbar_marker(value)

        self.draw_idle()

    def update_hover_cell(self, x, y):
        colors = self.theme_colors()

        if self.hover_rect is not None:
            self.hover_rect.remove()
            self.hover_rect = None

        self.hover_rect = Rectangle(
            (x - 0.5, y - 0.5),
            1,
            1,
            fill=False,
            edgecolor=colors["hover"],
            linewidth=3,
            zorder=10
        )

        self.axes.add_patch(self.hover_rect)

    def update_colorbar_marker(self, value):
        if self.cbar is None:
            return

        colors = self.theme_colors()

        if self.cbar_marker is not None:
            self.cbar_marker.remove()
            self.cbar_marker = None

        self.cbar_marker = self.cbar.ax.scatter(
            [0.5],
            [value],
            transform=self.cbar.ax.get_yaxis_transform(),
            s=150,
            facecolors="none",
            edgecolors=colors["hover"],
            linewidths=2.8,
            zorder=20
        )

    def clear_hover(self):
        changed = False

        if self.hover_rect is not None:
            self.hover_rect.remove()
            self.hover_rect = None
            changed = True

        if self.cbar_marker is not None:
            self.cbar_marker.remove()
            self.cbar_marker = None
            changed = True

        if changed:
            self.draw_idle()


    def refresh_theme(self, theme_name=None):
        if theme_name:
            self.theme_name = str(theme_name)

        if self.mesh is None:
            self.show_empty_state()
            return

        self.plot(
            self.mesh,
            cmap=self.cmap_name
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.mesh is not None:
            self.plot(
                self.mesh,
                cmap=self.cmap_name
            )
