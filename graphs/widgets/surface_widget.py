from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.colors import TwoSlopeNorm
from mpl_toolkits.mplot3d import proj3d
import numpy as np
from PySide6.QtGui import QCursor
from PySide6.QtWidgets import QToolTip

from core.config import Config
from languages import LanguageManager


class SurfaceWidget(FigureCanvasQTAgg):

    def __init__(self):
        self.figure = Figure()
        super().__init__(self.figure)

        self.axes = None
        self.cbar_ax = None

        self.mesh = None
        self.data = None
        self.x_values = None
        self.y_values = None
        self.surface = None
        self.wireframe = None
        self.probe_points = None
        self.zero_plane = None
        self.cbar = None
        self.cbar_marker = None
        self.cmap_name = "turbo"
        self.theme_name = None
        self.elevation = 32
        self.azimuth = -55
        self.display_mode = "mesh"
        self.show_wireframe = False
        self.show_zero_plane = False
        self.color_scale = 1.0
        self.box_scale = 1.0
        self.max_interactive_points = 70
        self.last_hover_cell = None

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
        self.x_values = None
        self.y_values = None
        self.surface = None
        self.wireframe = None
        self.probe_points = None
        self.zero_plane = None
        self.cbar = None
        self.cbar_marker = None
        self.last_hover_cell = None
        QToolTip.hideText()

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
                "pane": "#F8FAFC",
                "text": "#0F172A",
                "muted": "#64748B",
                "grid": "#CBD5E1",
                "edge": "#334155",
                "wire": "#0F172A",
                "wire_alpha": 0.72,
                "wire_width": 0.62,
                "probe": "#0F172A",
                "zero_plane": "#0284C7",
            }

        return {
            "figure_bg": "#0F172A",
            "axes_bg": "#0F172A",
            "pane": "#0F172A",
            "text": "#F8FAFC",
            "muted": "#CBD5E1",
            "grid": "#334155",
            "edge": "#E2E8F0",
            "wire": "#F8FAFC",
            "wire_alpha": 0.78,
            "wire_width": 0.72,
            "probe": "#F8FAFC",
            "zero_plane": "#38BDF8",
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
            self.axes.zaxis.label.set_color(colors["text"])
            self.axes.title.set_color(colors["text"])

            for axis in (self.axes.xaxis, self.axes.yaxis, self.axes.zaxis):
                axis.pane.set_facecolor(colors["pane"])
                axis.pane.set_edgecolor(colors["grid"])
                axis.pane.set_alpha(0.92)
                axis._axinfo["grid"]["color"] = colors["grid"]

        if self.cbar_ax is not None:
            self.cbar_ax.set_facecolor(colors["figure_bg"])

        return colors

    def layout_axes(self):
        self.figure.clear()

        canvas_width = max(self.width(), 1)
        canvas_height = max(self.height(), 1)
        figure_ratio = canvas_width / canvas_height

        max_surface_width = 0.68
        max_surface_height = 0.88

        surface_width = min(
            max_surface_width,
            max_surface_height / figure_ratio
        )

        surface_height = surface_width * figure_ratio
        cbar_width = 0.025
        gap = 0.035
        right_padding = 0.035

        group_width = surface_width + gap + cbar_width
        group_left = (1.0 - group_width) / 2.0
        surface_bottom = (1.0 - surface_height) / 2.0

        cbar_height = min(0.64, surface_height * 0.78)
        cbar_bottom = surface_bottom + (surface_height - cbar_height) / 2.0
        cbar_left = max(
            group_left + surface_width + gap,
            1.0 - right_padding - cbar_width
        )

        self.axes = self.figure.add_axes(
            [
                group_left,
                surface_bottom,
                surface_width,
                surface_height,
            ],
            projection="3d"
        )

        self.axes.set_proj_type("ortho")
        self.configure_mouse_controls()

        self.cbar_ax = self.figure.add_axes(
            [
                cbar_left,
                cbar_bottom,
                cbar_width,
                cbar_height,
            ]
        )

    def configure_mouse_controls(self):
        if self.axes is None:
            return

        try:
            self.axes.mouse_init(
                rotate_btn=1,
                pan_btn=[],
                zoom_btn=[]
            )
        except TypeError:
            self.axes.mouse_init(
                rotate_btn=1,
                zoom_btn=[]
            )

    def render_stride(self, rows, cols):
        row_stride = max(1, int(np.ceil(rows / self.max_interactive_points)))
        col_stride = max(1, int(np.ceil(cols / self.max_interactive_points)))

        return row_stride, col_stride

    def deviation_norm(self, mesh, color_scale=1.0):
        limit = max(
            abs(float(mesh.minimum)),
            abs(float(mesh.maximum)),
            0.001
        ) * max(float(color_scale), 0.1)
        vmin = -limit
        vmax = limit

        if abs(vmax - vmin) < 0.0001:
            vmax = vmin + 0.0001

        return TwoSlopeNorm(
            vmin=vmin,
            vcenter=0.0,
            vmax=vmax
        )

    def plot(
        self,
        mesh,
        cmap="turbo",
        elevation=32,
        azimuth=-55,
        display_mode="mesh",
        show_wireframe=False,
        show_zero_plane=False,
        color_scale=1.0,
        box_scale=1.0
    ):
        self.mesh = mesh
        self.cmap_name = cmap
        self.elevation = elevation
        self.azimuth = azimuth
        self.display_mode = display_mode
        self.show_wireframe = show_wireframe
        self.show_zero_plane = show_zero_plane
        self.color_scale = color_scale
        self.box_scale = box_scale

        self.layout_axes()
        self.cbar_marker = None
        colors = self.apply_theme()

        self.data = mesh.matrix

        rows, cols = self.data.shape

        x = np.arange(1, cols + 1)
        y = np.arange(1, rows + 1)
        self.x_values = x
        self.y_values = y

        X, Y = np.meshgrid(x, y)
        row_stride, col_stride = self.render_stride(rows, cols)
        norm = self.deviation_norm(mesh, color_scale)

        self.surface = self.axes.plot_surface(
            X,
            Y,
            self.data,
            cmap=cmap,
            norm=norm,
            edgecolor="none",
            linewidth=0,
            antialiased=False,
            shade=True,
            rstride=row_stride,
            cstride=col_stride
        )

        if display_mode == "probed":
            self.probe_points = self.axes.scatter(
                X.ravel(),
                Y.ravel(),
                self.data.ravel(),
                color=colors["probe"],
                edgecolors=colors["figure_bg"],
                linewidths=0.7,
                s=54,
                depthshade=False,
                zorder=10
            )

        if show_wireframe:
            z_offset = max(
                float(np.nanmax(self.data) - np.nanmin(self.data)) * 0.004,
                0.001
            )
            self.wireframe = self.axes.plot_wireframe(
                X,
                Y,
                self.data + z_offset,
                rstride=row_stride,
                cstride=col_stride,
                color=colors["wire"],
                linewidth=colors["wire_width"],
                alpha=colors["wire_alpha"]
            )

        if show_zero_plane:
            self.zero_plane = self.axes.plot_surface(
                X,
                Y,
                np.zeros_like(self.data),
                color=colors["zero_plane"],
                alpha=0.28,
                edgecolor=colors["zero_plane"],
                linewidth=0.25,
                antialiased=False,
                shade=False,
                rstride=row_stride,
                cstride=col_stride
            )

        self.axes.view_init(
            elev=elevation,
            azim=azimuth
        )

        self.axes.set_xlabel(
            "X",
            labelpad=10,
            color=colors["text"]
        )

        self.axes.set_ylabel(
            "Y",
            labelpad=10,
            color=colors["text"]
        )

        self.axes.set_zlabel(
            "Z (mm)",
            labelpad=10,
            color=colors["text"]
        )

        self.axes.set_xticks(x)
        self.axes.set_yticks(y)

        self.axes.set_xticklabels(
            [str(value) for value in x],
            color=colors["text"]
        )

        self.axes.set_yticklabels(
            [str(value) for value in y],
            color=colors["text"]
        )

        z_range = max(float(mesh.total_range), 0.001)
        z_min = min(float(mesh.minimum), 0.0)
        z_max = max(float(mesh.maximum), 0.0)
        z_padding = max(z_range * 0.12, 0.01)

        self.axes.set_zlim(
            z_min - z_padding,
            z_max + z_padding
        )

        z_aspect = max(
            0.25,
            min(1.5, z_range * 8 * box_scale / max(rows, cols, 1))
        )

        self.axes.set_box_aspect(
            (
                1,
                1,
                z_aspect,
            )
        )

        self.cbar = None
        if bool(Config().get("appearance_show_colorbar")):
            self.cbar_ax.set_visible(True)
            self.cbar = self.figure.colorbar(
                self.surface,
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

    def barycentric_weights(self, point, triangle):
        a, b, c = triangle
        denominator = (
            (b[1] - c[1]) * (a[0] - c[0]) +
            (c[0] - b[0]) * (a[1] - c[1])
        )

        if abs(denominator) < 1e-9:
            return None

        w1 = (
            (b[1] - c[1]) * (point[0] - c[0]) +
            (c[0] - b[0]) * (point[1] - c[1])
        ) / denominator
        w2 = (
            (c[1] - a[1]) * (point[0] - c[0]) +
            (a[0] - c[0]) * (point[1] - c[1])
        ) / denominator
        w3 = 1.0 - w1 - w2

        tolerance = -0.02
        if w1 < tolerance or w2 < tolerance or w3 < tolerance:
            return None

        return np.array([w1, w2, w3])

    def interpolated_surface_point(self, event):
        rows, cols = self.data.shape

        X, Y = np.meshgrid(self.x_values, self.y_values)
        x_proj, y_proj, _ = proj3d.proj_transform(
            X.ravel(),
            Y.ravel(),
            self.data.ravel(),
            self.axes.get_proj()
        )

        projected = self.axes.transData.transform(
            np.column_stack([x_proj, y_proj])
        ).reshape(rows, cols, 2)

        surface_x = X
        surface_y = Y
        surface_z = self.data
        mouse_point = np.array([event.x, event.y])

        for row in range(rows - 1):
            for col in range(cols - 1):
                triangles = (
                    (
                        (row, col),
                        (row, col + 1),
                        (row + 1, col),
                    ),
                    (
                        (row, col + 1),
                        (row + 1, col + 1),
                        (row + 1, col),
                    ),
                )

                for triangle_indices in triangles:
                    screen_triangle = np.array(
                        [
                            projected[r, c]
                            for r, c in triangle_indices
                        ]
                    )

                    weights = self.barycentric_weights(
                        mouse_point,
                        screen_triangle
                    )

                    if weights is None:
                        continue

                    data_points = np.array(
                        [
                            [
                                surface_x[r, c],
                                surface_y[r, c],
                                surface_z[r, c],
                            ]
                            for r, c in triangle_indices
                        ]
                    )

                    x_value, y_value, z_value = weights @ data_points

                    return {
                        "x": float(x_value),
                        "y": float(y_value),
                        "z": float(z_value),
                    }

        return self.nearest_surface_point(
            event,
            projected,
            surface_x,
            surface_y,
            surface_z
        )

    def nearest_surface_point(self, event, projected, surface_x, surface_y, surface_z):
        rows, cols = self.data.shape
        points = projected.reshape(rows * cols, 2)

        distances = np.hypot(
            points[:, 0] - event.x,
            points[:, 1] - event.y
        )

        nearest_index = int(np.argmin(distances))
        if distances[nearest_index] > 10:
            return None

        row_index, col_index = np.unravel_index(
            nearest_index,
            (rows, cols)
        )

        return {
            "x": float(surface_x[row_index, col_index]),
            "y": float(surface_y[row_index, col_index]),
            "z": float(surface_z[row_index, col_index]),
        }

    def on_mouse_move(self, event):
        if event.inaxes == self.cbar_ax:
            return

        if self.data is None or event.inaxes != self.axes:
            self.last_hover_cell = None
            self.clear_colorbar_marker()
            QToolTip.hideText()
            return

        hover_point = self.interpolated_surface_point(event)
        if hover_point is None:
            self.last_hover_cell = None
            self.clear_colorbar_marker()
            QToolTip.hideText()
            return

        hover_key = (
            round(hover_point["x"], 2),
            round(hover_point["y"], 2),
            round(hover_point["z"], 4),
        )

        if hover_key == self.last_hover_cell:
            return

        self.last_hover_cell = hover_key

        value = hover_point["z"]
        self.update_colorbar_marker(value)
        x_mm = self.coordinate_mm(hover_point["x"] - 1)
        y_mm = self.coordinate_mm(hover_point["y"] - 1)

        QToolTip.showText(
            QCursor.pos(),
            (
                f"{LanguageManager.text('surface_measurement')}: "
                f"X{hover_point['x']:.2f}, Y{hover_point['y']:.2f}<br>"
                f"{LanguageManager.text('surface_real_x')}: {x_mm:.1f} mm<br>"
                f"{LanguageManager.text('surface_real_y')}: {y_mm:.1f} mm<br>"
                f"Z: {value:.4f} mm<br>"
                f"{LanguageManager.text('surface_color_scale_position')}: "
                f"{value:.4f} mm"
            ),
            self
        )

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
            edgecolors=colors["zero_plane"],
            linewidths=2.8,
            zorder=20
        )

        self.draw_idle()

    def clear_colorbar_marker(self):
        if self.cbar_marker is None:
            return

        self.cbar_marker.remove()
        self.cbar_marker = None
        self.draw_idle()


    def refresh_theme(self, theme_name=None):
        if theme_name:
            self.theme_name = str(theme_name)

        if self.mesh is None:
            self.show_empty_state()
            return

        self.plot(
            self.mesh,
            cmap=self.cmap_name,
            elevation=self.elevation,
            azimuth=self.azimuth,
            display_mode=self.display_mode,
            show_wireframe=self.show_wireframe,
            show_zero_plane=self.show_zero_plane,
            color_scale=self.color_scale,
            box_scale=self.box_scale
        )

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self.mesh is not None:
            self.plot(
                self.mesh,
                cmap=self.cmap_name,
                elevation=self.elevation,
                azimuth=self.azimuth,
                display_mode=self.display_mode,
                show_wireframe=self.show_wireframe,
                show_zero_plane=self.show_zero_plane,
                color_scale=self.color_scale,
                box_scale=self.box_scale
            )
