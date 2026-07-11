"""
MeshAnalyzer Pro
Compare Page
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel,
    QTextEdit, QFileDialog, QGridLayout, QFrame, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.colors import TwoSlopeNorm
from matplotlib.patches import Rectangle
from matplotlib.lines import Line2D
import numpy as np

from core.config import Config
from core.parser import MeshParser
from core.compare import MeshCompare
from database.database import Database
from languages import LanguageManager
from gui.widgets.info_icon import InfoIcon


class MiniCompareHeatmap(FigureCanvasQTAgg):

    def __init__(self):
        self.figure = Figure(figsize=(5, 4), dpi=100)
        super().__init__(self.figure)

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )
        self.setMinimumSize(260, 220)

        self.axes = None
        self.cbar = None
        self.cbar_ax = None
        self.data = None
        self.hover_rect = None
        self.hover_annotation = None
        self.cbar_marker = None
        self.hover_callback = None
        self.hover_sync_callback = None

        self._matrix = None
        self._cmap = "turbo"
        self._center_zero = False
        self._vmin = None
        self._vmax = None

        self.mpl_connect("motion_notify_event", self.on_mouse_move)

        self.show_empty_state()

    def coordinate_mm(self, index):
        return 5 + index * 60

    def theme_colors(self):
        theme = str(Config().get("theme"))

        if theme == "light":
            return {
                "figure_bg": "#F8FAFC",
                "axes_bg": "#FFFFFF",
                "text": "#0F172A",
                "grid": "#CBD5E1",
                "hover": "#0284C7",
            }

        return {
            "figure_bg": "#0F172A",
            "axes_bg": "#111827",
            "text": "#F8FAFC",
            "grid": "#334155",
            "hover": "#38BDF8",
        }

    def apply_canvas_background(self):
        colors = self.theme_colors()
        self.figure.patch.set_facecolor(colors["figure_bg"])
        self.setStyleSheet(
            f"background-color: {colors['figure_bg']}; border: none;"
        )
        return colors

    def show_empty_state(self):
        self.figure.clear()
        self.cbar = None
        self.cbar_ax = None
        self.data = None
        self.hover_rect = None
        self.hover_annotation = None
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
            fontsize=15,
            fontweight="bold",
            transform=self.axes.transAxes,
        )

        self.axes.text(
            0.5,
            0.46,
            LanguageManager.text("empty_conf_waiting_message"),
            ha="center",
            va="center",
            color=colors["text"],
            fontsize=9,
            alpha=0.78,
            transform=self.axes.transAxes,
        )

        self.draw()

    def clear_plot(self):
        self._matrix = None
        self.show_empty_state()

    def responsive_positions(self):
        width_px, height_px = self.get_width_height()
        width_px = max(width_px, 320)
        height_px = max(height_px, 240)

        margin_x = 26
        margin_y = 22
        gap = 20
        cbar_width = 22

        available_width = max(160, width_px - (margin_x * 2))
        available_height = max(140, height_px - (margin_y * 2))

        heat_size = min(
            available_height,
            available_width - gap - cbar_width,
        )
        heat_size = max(120, heat_size)

        group_width = heat_size + gap + cbar_width
        group_left = (width_px - group_width) / 2
        heat_bottom = (height_px - heat_size) / 2

        heat_pos = [
            group_left / width_px,
            heat_bottom / height_px,
            heat_size / width_px,
            heat_size / height_px,
        ]

        cbar_pos = [
            (group_left + heat_size + gap) / width_px,
            heat_bottom / height_px,
            cbar_width / width_px,
            heat_size / height_px,
        ]

        return heat_pos, cbar_pos, heat_size

    def plot(
        self,
        matrix,
        cmap="turbo",
        center_zero=False,
        vmin=None,
        vmax=None,
        hover_callback=None,
        hover_sync_callback=None,
    ):
        self._matrix = matrix
        self._cmap = cmap
        self._center_zero = center_zero
        self._vmin = vmin
        self._vmax = vmax

        self.figure.clear()
        self.hover_rect = None
        self.hover_annotation = None
        self.cbar_marker = None
        self.hover_callback = hover_callback
        self.hover_sync_callback = hover_sync_callback

        colors = self.theme_colors()
        self.figure.patch.set_facecolor(colors["figure_bg"])
        self.setStyleSheet(
            f"background-color: {colors['figure_bg']}; border: none;"
        )

        heat_pos, cbar_pos, heat_size = self.responsive_positions()

        self.axes = self.figure.add_axes(heat_pos)
        self.cbar_ax = self.figure.add_axes(cbar_pos)

        self.axes.set_facecolor(colors["axes_bg"])
        self.cbar_ax.set_facecolor(colors["figure_bg"])

        self.data = np.array(matrix, dtype=float)
        data = self.data

        norm = None
        if center_zero:
            limit = float(np.max(np.abs(data)))
            if limit <= 0:
                limit = 1.0
            norm = TwoSlopeNorm(vmin=-limit, vcenter=0.0, vmax=limit)

        image = self.axes.imshow(
            data,
            origin="lower",
            cmap=cmap,
            norm=norm,
            vmin=vmin if norm is None else None,
            vmax=vmax if norm is None else None,
            aspect="equal",
        )

        rows, cols = data.shape
        max_dim = max(rows, cols)
        cell_font_size = max(8, min(13, int(heat_size / max_dim / 4.8)))
        tick_font_size = max(8, min(11, int(heat_size / max_dim / 6.0)))

        self.axes.set_xticks(range(cols))
        self.axes.set_yticks(range(rows))
        self.axes.set_xticklabels(
            [f"{self.coordinate_mm(i)} mm" for i in range(cols)],
            color=colors["text"],
            fontsize=tick_font_size,
        )
        self.axes.set_yticklabels(
            [f"{self.coordinate_mm(i)} mm" for i in range(rows)],
            color=colors["text"],
            fontsize=tick_font_size,
        )
        self.axes.tick_params(colors=colors["text"], length=0)

        for spine in self.axes.spines.values():
            spine.set_color(colors["grid"])

        for row in range(rows):
            for col in range(cols):
                self.axes.text(
                    col,
                    row,
                    f"{data[row, col]:.3f}",
                    ha="center",
                    va="center",
                    color="#FFFFFF",
                    fontsize=cell_font_size,
                    fontweight="bold",
                )

        self.cbar = self.figure.colorbar(
            image,
            cax=self.cbar_ax,
        )
        self.cbar.set_label("mm", color=colors["text"], fontsize=tick_font_size)
        self.cbar.ax.tick_params(colors=colors["text"], labelsize=tick_font_size)

        for spine in self.cbar.ax.spines.values():
            spine.set_color(colors["grid"])

        self.draw()

    def clear_hover(self):
        changed = False

        if self.hover_rect is not None:
            self.hover_rect.remove()
            self.hover_rect = None
            changed = True

        if self.hover_annotation is not None:
            self.hover_annotation.remove()
            self.hover_annotation = None
            changed = True

        if self.cbar_marker is not None:
            self.cbar_marker.remove()
            self.cbar_marker = None
            changed = True

        if changed:
            self.draw_idle()

    def update_colorbar_marker(self, value):
        """
        Hover edilen hücrenin değerini renk skalasında gösterir.

        Gösterim:
        - Renk skalası üzerinde içi boş yuvarlak işaretçi.
        - Ana grafik alanındaki hover rengiyle uyumludur.
        """
        if self.cbar is None or self.cbar_ax is None:
            return

        colors = self.theme_colors()

        if self.cbar_marker is not None:
            self.cbar_marker.remove()
            self.cbar_marker = None

        self.cbar_marker = Line2D(
            [0.5],
            [value],
            transform=self.cbar.ax.get_yaxis_transform(),
            linestyle="None",
            marker="o",
            markersize=9,
            markerfacecolor="none",
            markeredgecolor=colors["hover"],
            markeredgewidth=2.4,
            zorder=1000,
        )

        self.cbar.ax.add_line(self.cbar_marker)

    def highlight_cell(self, original_row, col, show_annotation=False):
        if self.axes is None or self.data is None:
            return

        rows, cols = self.data.shape
        visual_row = original_row

        if col < 0 or col >= cols or visual_row < 0 or visual_row >= rows:
            self.clear_hover()
            return

        value = float(self.data[visual_row, col])

        if self.hover_rect is not None:
            self.hover_rect.remove()

        colors = self.theme_colors()

        self.hover_rect = Rectangle(
            (col - 0.5, visual_row - 0.5),
            1,
            1,
            fill=False,
            edgecolor=colors["hover"],
            linewidth=3.0,
            zorder=900,
        )
        self.axes.add_patch(self.hover_rect)

        self.update_colorbar_marker(value)

        if self.hover_annotation is not None:
            self.hover_annotation.remove()
            self.hover_annotation = None

        if show_annotation:
            if self.hover_callback is not None:
                text = self.hover_callback(original_row, col, value)
            else:
                text = f"X{col + 1} Y{original_row + 1}\n{value:+.4f} mm"

            # Açılır bilgi kutusu renk ölçeğinin altında kalmasın diye
            # sağ kenara yakın hücrelerde kutuyu sola doğru açıyoruz.
            # Böylece tooltip her zaman heatmap alanının içinde ve üstte kalır.
            if col >= cols - 2:
                xytext = (-14, 14)
                ha = "right"
            else:
                xytext = (14, 14)
                ha = "left"

            self.hover_annotation = self.axes.annotate(
                text,
                xy=(col, visual_row),
                xytext=xytext,
                textcoords="offset points",
                fontsize=9,
                color="#FFFFFF",
                ha=ha,
                va="bottom",
                bbox={
                    "boxstyle": "round,pad=0.35",
                    "facecolor": "#111827",
                    "edgecolor": "#38BDF8",
                    "alpha": 0.98,
                },
                annotation_clip=False,
                zorder=1000,
            )

            self.hover_annotation.set_clip_on(False)

        self.draw_idle()

    def on_mouse_move(self, event):
        if self.axes is None or self.data is None or event.inaxes != self.axes:
            self.clear_hover()
            if self.hover_sync_callback is not None:
                self.hover_sync_callback(None, None, self)
            return

        if event.xdata is None or event.ydata is None:
            self.clear_hover()
            if self.hover_sync_callback is not None:
                self.hover_sync_callback(None, None, self)
            return

        col = int(round(event.xdata))
        visual_row = int(round(event.ydata))
        rows, cols = self.data.shape

        if col < 0 or col >= cols or visual_row < 0 or visual_row >= rows:
            self.clear_hover()
            if self.hover_sync_callback is not None:
                self.hover_sync_callback(None, None, self)
            return

        original_row = visual_row
        if self.hover_sync_callback is not None:
            self.hover_sync_callback(original_row, col, self)
        else:
            self.highlight_cell(original_row, col, show_annotation=True)

    def resizeEvent(self, event):
        super().resizeEvent(event)

        if self._matrix is not None:
            self.plot(
                self._matrix,
                cmap=self._cmap,
                center_zero=self._center_zero,
                vmin=self._vmin,
                vmax=self._vmax,
                hover_callback=self.hover_callback,
                hover_sync_callback=self.hover_sync_callback,
            )


class ComparePage(QWidget):

    def __init__(self):
        super().__init__()

        self.parser = MeshParser()
        self.db = Database()
        self.before_mesh = None
        self.after_mesh = None
        self.current_delta = None
        self.before_status = "not_selected"
        self.after_status = "not_selected"

        layout = QVBoxLayout(self)

        button_layout = QHBoxLayout()

        self.btn_before = QPushButton()
        self.btn_after = QPushButton()
        self.btn_compare = QPushButton()

        button_font = QFont()
        button_font.setPointSize(11)
        button_font.setBold(True)

        for button in [self.btn_before, self.btn_after, self.btn_compare]:
            button.setFont(button_font)

        button_layout.addWidget(self.btn_before)
        button_layout.addWidget(self.btn_after)
        button_layout.addWidget(self.btn_compare)

        self.lbl_before = QLabel()
        self.lbl_after = QLabel()

        label_font = QFont()
        label_font.setPointSize(10)
        label_font.setBold(True)

        self.lbl_before.setFont(label_font)
        self.lbl_after.setFont(label_font)

        self.before_heatmap = MiniCompareHeatmap()
        self.after_heatmap = MiniCompareHeatmap()
        self.delta_heatmap = MiniCompareHeatmap()

        self.old_title = QLabel()
        self.new_title = QLabel()
        self.delta_title = QLabel()
        self.result_title = QLabel()

        self.result = QTextEdit()
        self.result.setReadOnly(True)

        result_font = QFont()
        result_font.setPointSize(10)
        self.result.setFont(result_font)

        self.panel_grid = QGridLayout()
        self.panel_grid.setSpacing(14)
        self.panel_grid.addWidget(
            self.create_panel(self.old_title, self.before_heatmap),
            0,
            0,
        )
        self.panel_grid.addWidget(
            self.create_panel(self.new_title, self.after_heatmap),
            0,
            1,
        )
        self.panel_grid.addWidget(
            self.create_panel(self.result_title, self.result),
            1,
            0,
        )
        self.panel_grid.addWidget(
            self.create_panel(self.delta_title, self.delta_heatmap),
            1,
            1,
        )
        self.panel_grid.setColumnStretch(0, 1)
        self.panel_grid.setColumnStretch(1, 1)
        self.panel_grid.setRowStretch(0, 1)
        self.panel_grid.setRowStretch(1, 1)

        layout.addLayout(button_layout)
        layout.addWidget(self.lbl_before)
        layout.addWidget(self.lbl_after)
        layout.addLayout(self.panel_grid, 1)

        self.btn_before.clicked.connect(self.load_before)
        self.btn_after.clicked.connect(self.load_after)
        self.btn_compare.clicked.connect(self.compare)
        self.retranslate()
        self.refresh_theme()

    def create_panel(self, title, widget):
        panel = QFrame()
        panel.setObjectName("ComparePanel")
        panel.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        layout = QVBoxLayout(panel)
        layout.setContentsMargins(8, 8, 8, 8)
        layout.setSpacing(6)

        title.setObjectName("ComparePanelTitle")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        title.setFont(font)

        title_row = QWidget()
        title_row.setObjectName("CardTitleRow")

        title_layout = QHBoxLayout(title_row)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_layout.setSpacing(6)

        info_icon = InfoIcon("")
        title.infoIcon = info_icon

        title_layout.addStretch()
        title_layout.addWidget(title)
        title_layout.addWidget(info_icon)
        title_layout.addStretch()

        widget.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding,
        )

        layout.addWidget(title_row)
        layout.addWidget(widget, 1)
        return panel

    def update_mesh(self, mesh):
        self.after_mesh = mesh
        self.after_status = "loaded"
        self.current_delta = None
        self.update_labels()
        self.render_heatmaps()

        self.before_mesh = self.db.load_previous_mesh(mesh)

        if self.before_mesh is None:
            self.before_status = "missing_previous"
            self.current_delta = None
            self.before_heatmap.clear_plot()
            self.delta_heatmap.clear_plot()
            self.update_labels()
            self.result.setText(
                LanguageManager.text("compare_no_previous_history")
            )
            return

        self.before_status = "loaded"
        self.update_labels()
        self.render_heatmaps()
        self.auto_compare()

    def load_before(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            LanguageManager.text("compare_open_old_title"),
            "",
            LanguageManager.text("mesh_file_filter")
        )

        if not filename:
            return

        self.before_mesh = self.parser.load(filename)
        self.before_status = "loaded"
        self.current_delta = None
        self.update_labels()
        self.render_heatmaps()
        self.auto_compare()

    def load_after(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            LanguageManager.text("compare_open_new_title"),
            "",
            LanguageManager.text("mesh_file_filter")
        )

        if not filename:
            return

        self.after_mesh = self.parser.load(filename)
        self.after_status = "loaded"
        self.current_delta = None
        self.update_labels()
        self.render_heatmaps()
        self.auto_compare()

    def auto_compare(self):
        if self.before_mesh is not None and self.after_mesh is not None:
            self.compare()

    def render_heatmaps(self, delta=None):
        if delta is not None:
            self.current_delta = delta

        shared_vmin = None
        shared_vmax = None
        if self.before_mesh is not None and self.after_mesh is not None:
            shared_vmin = min(self.before_mesh.minimum, self.after_mesh.minimum)
            shared_vmax = max(self.before_mesh.maximum, self.after_mesh.maximum)

        if self.before_mesh is not None:
            self.before_heatmap.plot(
                self.before_mesh.matrix,
                cmap="turbo",
                vmin=shared_vmin,
                vmax=shared_vmax,
                hover_callback=self.hover_text,
                hover_sync_callback=self.sync_hover,
            )
        else:
            self.before_heatmap.clear_plot()

        if self.after_mesh is not None:
            self.after_heatmap.plot(
                self.after_mesh.matrix,
                cmap="turbo",
                vmin=shared_vmin,
                vmax=shared_vmax,
                hover_callback=self.hover_text,
                hover_sync_callback=self.sync_hover,
            )
        else:
            self.after_heatmap.clear_plot()

        if self.current_delta is not None:
            self.delta_heatmap.plot(
                self.current_delta,
                cmap="coolwarm",
                center_zero=True,
                hover_callback=self.hover_text,
                hover_sync_callback=self.sync_hover,
            )
        else:
            self.delta_heatmap.clear_plot()

    def sync_hover(self, row, col, source):
        heatmaps = (
            self.before_heatmap,
            self.after_heatmap,
            self.delta_heatmap,
        )

        if row is None or col is None:
            for heatmap in heatmaps:
                heatmap.clear_hover()
            return

        for heatmap in heatmaps:
            heatmap.highlight_cell(
                row,
                col,
                show_annotation=(heatmap is source),
            )

    def hover_text(self, row, col, value):
        lines = [
            f"{LanguageManager.text('compare_cell_value')}: {value:+.4f} mm",
        ]

        if self.current_delta is not None:
            delta = float(self.current_delta[row, col])
            lines.append(
                f"{LanguageManager.text('compare_cell_difference')}: "
                f"{delta:+.4f} mm"
            )

        return "\n".join(lines)

    def format_signed_percent(self, value):
        prefix = "+" if value > 0 else ""
        return f"{prefix}{value:.1f}%"

    def compare_summary_sentence(self, summary):
        total_change = float(summary.get("improvement", 0.0))
        rms_change = float(summary.get("rms_improvement", 0.0))

        if total_change > 1 and rms_change > 1:
            return LanguageManager.text("compare_summary_better")
        if total_change < -1 or rms_change < -1:
            return LanguageManager.text("compare_summary_worse")
        return LanguageManager.text("compare_summary_similar")

    def compare(self):
        if self.before_mesh is None or self.after_mesh is None:
            self.result.setText(LanguageManager.text("compare_select_two_mesh"))
            return

        try:
            comparison = MeshCompare(
                self.before_mesh,
                self.after_mesh
            )

            summary = comparison.summary()
            delta = comparison.delta()
            self.render_heatmaps(delta)

            self.result.clear()
            self.result.append(LanguageManager.text("compare_summary_section").upper())
            self.result.append("-" * 40)
            self.result.append(self.compare_summary_sentence(summary))
            self.result.append("")

            self.result.append(LanguageManager.text("compare_metric_changes").upper())
            self.result.append("-" * 40)
            self.result.append(
                f"{LanguageManager.text('compare_old_total_deviation')} : "
                f"{summary['before_range']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_new_total_deviation')} : "
                f"{summary['after_range']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_total_range_change')} : "
                f"{self.format_signed_percent(summary['improvement'])}"
            )
            self.result.append("")
            self.result.append(
                f"{LanguageManager.text('compare_old_rms')} : "
                f"{summary['before_rms']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_new_rms')} : "
                f"{summary['after_rms']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_rms_change')} : "
                f"{self.format_signed_percent(summary['rms_improvement'])}"
            )
            self.result.append("")

            self.result.append(LanguageManager.text("compare_regional_changes").upper())
            self.result.append("-" * 40)
            self.result.append(
                f"{LanguageManager.text('compare_most_improved_area')} : "
                f"{summary['best_location']} "
                f"({summary['best_value']:+.4f} mm)"
            )
            self.result.append(
                f"{LanguageManager.text('compare_most_worsened_area')} : "
                f"{summary['worst_location']} "
                f"({summary['worst_value']:+.4f} mm)"
            )
            self.result.append("")

            self.result.append(LanguageManager.text("compare_delta_statistics").upper())
            self.result.append("-" * 40)
            self.result.append(
                f"{LanguageManager.text('compare_delta_min')} : "
                f"{summary['delta_min']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_delta_max')} : "
                f"{summary['delta_max']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_delta_average')} : "
                f"{summary['delta_avg']:.4f} mm"
            )
            self.result.append(
                f"{LanguageManager.text('compare_delta_abs_max')} : "
                f"{summary['delta_abs_max']:.4f} mm"
            )
        except Exception as error:
            self.current_delta = None
            self.delta_heatmap.clear_plot()
            self.result.setText(str(error))

    def update_labels(self):
        if self.before_status == "loaded" and self.before_mesh is not None:
            self.lbl_before.setText(
                f"{LanguageManager.text('compare_old_label')}: "
                f"{self.before_mesh.name}"
            )
        elif self.before_status == "missing_previous":
            self.lbl_before.setText(
                f"{LanguageManager.text('compare_old_label')}: "
                f"{LanguageManager.text('compare_no_previous_short')}"
            )
        else:
            self.lbl_before.setText(
                LanguageManager.text("compare_old_not_selected")
            )

        if self.after_status == "loaded" and self.after_mesh is not None:
            self.lbl_after.setText(
                f"{LanguageManager.text('compare_new_label')}: "
                f"{self.after_mesh.name}"
            )
        else:
            self.lbl_after.setText(
                LanguageManager.text("compare_new_not_selected")
            )

    def retranslate(self):
        self.btn_before.setText(LanguageManager.text("compare_open_old"))
        self.btn_after.setText(LanguageManager.text("compare_open_new"))
        self.btn_compare.setText(LanguageManager.text("compare_action"))

        self.old_title.setText(LanguageManager.text("compare_old_mesh").upper())
        self.old_title.infoIcon.setToolTip(
            LanguageManager.text("tooltip_compare_old_mesh")
        )

        self.new_title.setText(LanguageManager.text("compare_new_mesh").upper())
        self.new_title.infoIcon.setToolTip(
            LanguageManager.text("tooltip_compare_new_mesh")
        )

        self.result_title.setText(
            LanguageManager.text("compare_report_title").upper()
        )
        self.result_title.infoIcon.setToolTip(
            LanguageManager.text("tooltip_compare_report")
        )

        self.delta_title.setText(
            LanguageManager.text("compare_delta_heatmap").upper()
        )
        self.delta_title.infoIcon.setToolTip(
            LanguageManager.text("tooltip_compare_delta_heatmap")
        )

        self.update_labels()

        if self.before_mesh is not None and self.after_mesh is not None:
            self.compare()
        elif self.before_status == "missing_previous":
            self.result.setText(
                LanguageManager.text("compare_no_previous_history")
            )
        else:
            self.result.setText(LanguageManager.text("compare_auto_hint"))

    def refresh_language(self):
        self.retranslate()

    def refresh_theme(self):
        theme = str(Config().get("theme"))

        if theme == "light":
            card_bg = "#FFFFFF"
            border = "#CBD5E1"
            text = "#0F172A"
            input_bg = "#F8FAFC"
        else:
            card_bg = "#1E293B"
            border = "#334155"
            text = "#F8FAFC"
            input_bg = "#111827"

        self.setStyleSheet(f"""
        QFrame#ComparePanel {{
            background: {card_bg};
            border: 1px solid {border};
            border-radius: 10px;
        }}

        QLabel#ComparePanelTitle {{
            color: {text};
            background: transparent;
            font-weight: 800;
        }}

        QTextEdit {{
            background: {input_bg};
            color: {text};
            border: 1px solid {border};
            border-radius: 8px;
            padding: 8px;
            font-family: Consolas, monospace;
            font-size: 10pt;
        }}
        """)

        self.render_heatmaps()
