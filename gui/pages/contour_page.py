"""
MeshAnalyzer Pro
Topography Page
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QFrame,
)

from core.config import Config
from graphs.widgets.contour_widget import ContourWidget
from languages import LanguageManager
from gui.widgets.summary_card import SummaryCard
from gui.widgets.info_icon import InfoIcon


class ContourPage(QWidget):

    def __init__(self):
        super().__init__()

        self.current_mesh = None

        main_layout = QVBoxLayout(self)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(16)

        self.graph = ContourWidget()
        content_layout.addWidget(self.graph, stretch=4)

        self.summaryCard = SummaryCard(
            tooltip=""
        )

        self.summaryCard.setMinimumWidth(280)
        self.summaryCard.setMaximumWidth(340)

        self.paletteCombo = QComboBox()
        self.paletteCombo.addItem("Terrain", "terrain")
        self.paletteCombo.addItem("Turbo", "turbo")
        self.paletteCombo.addItem("Viridis", "viridis")
        self.paletteCombo.addItem("Coolwarm", "coolwarm")
        self.paletteCombo.addItem("Plasma", "plasma")

        self.levelCombo = QComboBox()
        self.levelCombo.addItem("10", 10)
        self.levelCombo.addItem("15", 15)
        self.levelCombo.addItem("20", 20)
        self.levelCombo.addItem("30", 30)
        self.levelCombo.setCurrentIndex(2)

        self.apply_default_combo_value(
            self.paletteCombo,
            str(Config().get("default_topography_palette") or "terrain"),
            0
        )

        self.summaryCard.addRow("palette")
        self.summaryCard.addRow("levels")

        palette_value = self.summaryCard.values.get("palette")
        if palette_value is not None:
            palette_value.hide()

        level_value = self.summaryCard.values.get("levels")
        if level_value is not None:
            level_value.hide()

        self.summaryCard.grid.addWidget(
            self.paletteCombo,
            0,
            1
        )

        self.summaryCard.grid.addWidget(
            self.levelCombo,
            1,
            1
        )

        self.add_metrics_separator()
        self.summaryCard.addRow("minimum")
        self.summaryCard.addRow("maximum")
        self.summaryCard.addRow("average")
        self.summaryCard.addRow("total_range")

        for key in (
            "minimum",
            "maximum",
            "average",
            "total_range",
        ):
            self.add_metric_info_icon(key)

        content_layout.addWidget(self.summaryCard, stretch=1)
        main_layout.addLayout(content_layout)

        self.paletteCombo.currentIndexChanged.connect(
            self.on_options_changed
        )
        self.levelCombo.currentIndexChanged.connect(
            self.on_options_changed
        )

        self.retranslate()

    def apply_default_combo_value(self, combo, value, fallback_index=0):
        index = combo.findData(value)
        if index < 0:
            index = fallback_index
        combo.setCurrentIndex(index)

    def showEvent(self, event):
        super().showEvent(event)
        self.refresh_theme()

    def update_mesh(self, mesh):
        self.current_mesh = mesh

        self.refresh()

        self.summaryCard.setValue(
            "minimum",
            f"{mesh.minimum:.4f} mm"
        )

        self.summaryCard.setValue(
            "maximum",
            f"{mesh.maximum:.4f} mm"
        )

        self.summaryCard.setValue(
            "average",
            f"{mesh.average:.4f} mm"
        )

        self.summaryCard.setValue(
            "total_range",
            f"{mesh.total_range:.4f} mm"
        )

    def on_options_changed(self, *args):
        self.refresh()

    def add_metrics_separator(self):
        self.summaryCard.addRow("metrics_separator")

        separator_label = self.summaryCard.labels.get("metrics_separator")
        separator_value = self.summaryCard.values.get("metrics_separator")
        if separator_label is not None:
            separator_label.hide()
        if separator_value is not None:
            separator_value.hide()

        row = list(self.summaryCard.labels).index("metrics_separator")
        self.metricsSeparator = QFrame()
        self.metricsSeparator.setObjectName("SummarySeparator")
        self.metricsSeparator.setFrameShape(QFrame.Shape.HLine)
        self.metricsSeparator.setStyleSheet(
            "color: palette(mid); background: transparent; "
            "border: none; min-height: 1px; max-height: 1px;"
        )
        self.summaryCard.grid.addWidget(
            self.metricsSeparator,
            row,
            0,
            1,
            2
        )

    def add_metric_info_icon(self, key):
        label = self.summaryCard.labels.get(key)
        if label is None:
            return

        row = list(self.summaryCard.labels).index(key)
        self.summaryCard.grid.removeWidget(label)

        wrapper = QWidget()
        wrapper.setObjectName("SummaryMetricLabel")
        layout = QHBoxLayout(wrapper)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(4)
        layout.addWidget(label)

        info_icon = InfoIcon()
        layout.addWidget(info_icon)
        layout.addStretch()

        self.summaryCard.grid.addWidget(wrapper, row, 0)
        setattr(self, f"{key}MetricWidget", wrapper)
        setattr(self, f"{key}InfoIcon", info_icon)

    def set_metric_tooltip(self, key, text):
        info_icon = getattr(self, f"{key}InfoIcon", None)
        if info_icon is not None:
            info_icon.setToolTip(text)

    def refresh(self):
        if self.current_mesh is None:
            self.graph.show_empty_state()
            return

        levels = int(self.levelCombo.currentData())

        self.graph.plot(
            self.current_mesh,
            cmap=self.paletteCombo.currentData(),
            filled_levels=levels,
            line_levels=max(5, levels // 2)
        )

    def refresh_theme(self, theme_name=None):
        if hasattr(self.graph, "set_theme_name"):
            self.graph.set_theme_name(theme_name)

        self.refresh()

    def refresh_language(self):
        self.retranslate()

    def refresh_page(self):
        self.refresh_language()
        self.refresh_theme()

    def retranslate(self):
        self.summaryCard.setTitle(
            LanguageManager.text("topography_summary")
        )

        self.summaryCard.setTooltip(
            LanguageManager.text("topography_summary_tooltip")
        )

        self.summaryCard.setLabel(
            "palette",
            LanguageManager.text("color_palette")
        )

        self.summaryCard.setLabel(
            "levels",
            LanguageManager.text("contour_levels")
        )

        self.summaryCard.setLabel(
            "minimum",
            LanguageManager.text("minimum")
        )
        self.set_metric_tooltip(
            "minimum",
            LanguageManager.text("surface_minimum_tooltip")
        )

        self.summaryCard.setLabel(
            "maximum",
            LanguageManager.text("maximum")
        )
        self.set_metric_tooltip(
            "maximum",
            LanguageManager.text("surface_maximum_tooltip")
        )

        self.summaryCard.setLabel(
            "average",
            LanguageManager.text("average")
        )
        self.set_metric_tooltip(
            "average",
            LanguageManager.text("surface_average_tooltip")
        )

        self.summaryCard.setLabel(
            "total_range",
            LanguageManager.text("total_deviation")
        )
        self.set_metric_tooltip(
            "total_range",
            LanguageManager.text("surface_total_range_tooltip")
        )

        self.refresh()
