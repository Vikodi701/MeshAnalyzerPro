"""
MeshAnalyzer Pro
3D Surface Page
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QComboBox,
    QCheckBox,
    QRadioButton,
    QButtonGroup,
    QSlider,
    QLabel,
    QPushButton,
    QFrame,
)

from PySide6.QtCore import Qt

from core.config import Config
from graphs.widgets.surface_widget import SurfaceWidget
from languages import LanguageManager
from gui.widgets.summary_card import SummaryCard
from gui.widgets.info_icon import InfoIcon
from utils.app_icon import resource_path


class SurfacePage(QWidget):

    VIEW_PRESETS = {
        "default": (32, -55),
        "front": (20, -90),
        "side": (20, 0),
        "top": (90, -90),
        "detail": (42, -35),
    }

    def __init__(self):
        super().__init__()

        self.current_mesh = None

        main_layout = QVBoxLayout(self)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(16)

        self.graph = SurfaceWidget()
        content_layout.addWidget(self.graph, stretch=4)

        self.summaryCard = SummaryCard(
            tooltip=""
        )

        self.summaryCard.setMinimumWidth(280)
        self.summaryCard.setMaximumWidth(340)

        self.paletteCombo = QComboBox()
        self.paletteCombo.addItem("Turbo", "turbo")
        self.paletteCombo.addItem("Viridis", "viridis")
        self.paletteCombo.addItem("Terrain", "terrain")
        self.paletteCombo.addItem("Coolwarm", "coolwarm")
        self.paletteCombo.addItem("Plasma", "plasma")

        self.apply_default_combo_value(
            self.paletteCombo,
            str(Config().get("default_surface_palette") or "turbo"),
            0
        )

        self.viewCombo = QComboBox()
        self.probedRadio = QRadioButton()
        self.meshRadio = QRadioButton()
        self.matrixGroup = QButtonGroup(self)
        self.matrixGroup.addButton(self.probedRadio)
        self.matrixGroup.addButton(self.meshRadio)
        self.probedRadio.setChecked(True)
        self.wireframeCheck = QCheckBox()
        self.wireframeCheck.setChecked(True)
        self.zeroPlaneCheck = QCheckBox()
        self.colorScaleSlider = QSlider(Qt.Orientation.Horizontal)
        self.colorScaleSlider.setRange(50, 200)
        self.colorScaleSlider.setValue(100)
        self.colorScaleValue = QLabel("1.00x")
        self.colorScaleResetButton = QPushButton("↻")
        self.colorScaleResetButton.setObjectName("SurfaceResetButton")
        self.colorScaleResetButton.setFixedSize(24, 22)
        self.boxScaleSlider = QSlider(Qt.Orientation.Horizontal)
        self.boxScaleSlider.setRange(50, 250)
        self.boxScaleSlider.setValue(50)
        self.boxScaleValue = QLabel("0.50x")
        self.boxScaleResetButton = QPushButton("↻")
        self.boxScaleResetButton.setObjectName("SurfaceResetButton")
        self.boxScaleResetButton.setFixedSize(24, 22)

        self.summaryCard.addRow("palette")
        self.summaryCard.addRow("view")
        self.summaryCard.addRow("matrix_mode")
        self.summaryCard.addRow("wireframe")
        self.summaryCard.addRow("zero_plane")
        self.summaryCard.addRow("color_scale")
        self.summaryCard.addRow("box_scale")

        palette_value = self.summaryCard.values.get("palette")
        if palette_value is not None:
            palette_value.hide()

        view_value = self.summaryCard.values.get("view")
        if view_value is not None:
            view_value.hide()

        zero_plane_value = self.summaryCard.values.get("zero_plane")
        if zero_plane_value is not None:
            zero_plane_value.hide()

        for key in (
            "matrix_mode",
            "wireframe",
            "color_scale",
            "box_scale",
        ):
            value = self.summaryCard.values.get(key)
            if value is not None:
                value.hide()

        self.summaryCard.grid.addWidget(
            self.paletteCombo,
            0,
            1
        )

        self.summaryCard.grid.addWidget(
            self.viewCombo,
            1,
            1
        )

        matrix_layout = QVBoxLayout()
        matrix_layout.setContentsMargins(0, 0, 0, 0)
        matrix_layout.setSpacing(4)
        matrix_layout.addWidget(self.probedRadio)
        matrix_layout.addWidget(self.meshRadio)

        self.matrixWidget = QWidget()
        self.matrixWidget.setObjectName("SurfaceTransparentControl")
        self.matrixWidget.setLayout(matrix_layout)

        self.summaryCard.grid.addWidget(
            self.matrixWidget,
            2,
            1
        )

        self.summaryCard.grid.addWidget(
            self.wireframeCheck,
            3,
            1
        )

        self.summaryCard.grid.addWidget(
            self.zeroPlaneCheck,
            4,
            1
        )

        color_scale_layout = QHBoxLayout()
        color_scale_layout.setContentsMargins(0, 0, 0, 0)
        color_scale_layout.setSpacing(6)
        color_scale_layout.addWidget(self.colorScaleSlider)
        color_scale_layout.addWidget(self.colorScaleValue)
        color_scale_layout.addWidget(self.colorScaleResetButton)

        self.colorScaleWidget = QWidget()
        self.colorScaleWidget.setObjectName("SurfaceTransparentControl")
        self.colorScaleWidget.setLayout(color_scale_layout)

        self.summaryCard.grid.addWidget(
            self.colorScaleWidget,
            5,
            1
        )

        box_scale_layout = QHBoxLayout()
        box_scale_layout.setContentsMargins(0, 0, 0, 0)
        box_scale_layout.setSpacing(6)
        box_scale_layout.addWidget(self.boxScaleSlider)
        box_scale_layout.addWidget(self.boxScaleValue)
        box_scale_layout.addWidget(self.boxScaleResetButton)

        self.boxScaleWidget = QWidget()
        self.boxScaleWidget.setObjectName("SurfaceTransparentControl")
        self.boxScaleWidget.setLayout(box_scale_layout)

        self.summaryCard.grid.addWidget(
            self.boxScaleWidget,
            6,
            1
        )

        self.summaryCard.addRow("metrics_separator")
        separator_label = self.summaryCard.labels.get("metrics_separator")
        separator_value = self.summaryCard.values.get("metrics_separator")
        if separator_label is not None:
            separator_label.hide()
        if separator_value is not None:
            separator_value.hide()

        self.metricsSeparator = QFrame()
        self.metricsSeparator.setObjectName("SurfaceSectionSeparator")
        self.metricsSeparator.setFrameShape(QFrame.Shape.HLine)
        self.summaryCard.grid.addWidget(
            self.metricsSeparator,
            7,
            0,
            1,
            2
        )

        self.summaryCard.addRow("minimum")
        self.summaryCard.addRow("maximum")
        self.summaryCard.addRow("average")
        self.summaryCard.addRow("rms")
        self.summaryCard.addRow("total_range")

        for key in (
            "minimum",
            "maximum",
            "average",
            "rms",
            "total_range",
        ):
            self.add_metric_info_icon(key)

        content_layout.addWidget(self.summaryCard, stretch=1)
        main_layout.addLayout(content_layout)

        self.paletteCombo.currentIndexChanged.connect(
            self.on_options_changed
        )
        self.viewCombo.currentIndexChanged.connect(
            self.on_options_changed
        )
        self.probedRadio.toggled.connect(
            self.on_options_changed
        )
        self.wireframeCheck.stateChanged.connect(
            self.on_options_changed
        )
        self.zeroPlaneCheck.stateChanged.connect(
            self.on_options_changed
        )
        self.colorScaleSlider.valueChanged.connect(
            self.on_options_changed
        )
        self.boxScaleSlider.valueChanged.connect(
            self.on_options_changed
        )
        self.colorScaleResetButton.clicked.connect(
            self.reset_color_scale
        )
        self.boxScaleResetButton.clicked.connect(
            self.reset_box_scale
        )

        self.retranslate()
        self.refresh_control_styles()

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
            "rms",
            f"{mesh.rms:.4f} mm"
        )

        self.summaryCard.setValue(
            "total_range",
            f"{mesh.total_range:.4f} mm"
        )

    def on_options_changed(self, *args):
        self.update_scale_labels()
        self.refresh()

    def update_scale_labels(self):
        self.colorScaleValue.setText(f"{self.color_scale():.2f}x")
        self.boxScaleValue.setText(f"{self.box_scale():.2f}x")

    def reset_color_scale(self):
        self.colorScaleSlider.setValue(100)
        self.refresh()

    def reset_box_scale(self):
        self.boxScaleSlider.setValue(50)

    def add_metric_info_icon(self, key):
        label = self.summaryCard.labels.get(key)
        if label is None:
            return

        row = list(self.summaryCard.labels).index(key)
        self.summaryCard.grid.removeWidget(label)

        wrapper = QWidget()
        wrapper.setObjectName("SurfaceMetricLabel")
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

    def refresh_control_styles(self):
        theme = str(Config().get("theme"))

        if theme == "light":
            text_color = "#0F172A"
            muted_color = "#334155"
            value_color = "#000000"
            panel_bg = "#FFFFFF"
            border_color = "#0F172A"
            fill_color = "#0F172A"
            groove_color = "#CBD5E1"
            groove_fill = "#94A3B8"
            handle_border = "#0F172A"
            separator_color = "#CBD5E1"
            check_icon = resource_path("assets", "icons", "check_black.svg")
        else:
            text_color = "#F8FAFC"
            muted_color = "#CBD5E1"
            value_color = "#FFFFFF"
            panel_bg = "#1E293B"
            border_color = "#F8FAFC"
            fill_color = "#F8FAFC"
            groove_color = "#334155"
            groove_fill = "#64748B"
            handle_border = "#F8FAFC"
            separator_color = "#334155"
            check_icon = resource_path("assets", "icons", "check_white.svg")

        check_icon_path = check_icon.as_posix()

        style = f"""
        QFrame#SummaryCard {{
            background-color: {panel_bg};
        }}

        QWidget#SurfaceTransparentControl {{
            background: transparent;
            border: none;
        }}

        QWidget#SurfaceMetricLabel {{
            background: transparent;
            border: none;
        }}

        QFrame#SurfaceSectionSeparator {{
            background: {separator_color};
            border: none;
            max-height: 1px;
            min-height: 1px;
        }}

        QLabel#SummaryLabel {{
            background: transparent;
            color: {muted_color};
        }}

        QLabel#SummaryValue {{
            background: transparent;
            color: {value_color};
        }}

        QRadioButton, QCheckBox {{
            background: transparent;
            color: {text_color};
            spacing: 8px;
        }}

        QLabel {{
            background: transparent;
            color: {text_color};
        }}

        QRadioButton::indicator, QCheckBox::indicator {{
            width: 15px;
            height: 15px;
            border: 1px solid {border_color};
            background-color: transparent;
        }}

        QRadioButton::indicator {{
            border-radius: 8px;
        }}

        QRadioButton::indicator:checked {{
            border: 1px solid {border_color};
            background: qradialgradient(
                cx: 0.5,
                cy: 0.5,
                radius: 0.5,
                fx: 0.5,
                fy: 0.5,
                stop: 0 {fill_color},
                stop: 0.34 {fill_color},
                stop: 0.38 transparent,
                stop: 1 transparent
            );
        }}

        QCheckBox::indicator:checked {{
            border: 1px solid {border_color};
            background-color: {fill_color};
            image: url("{check_icon_path}");
        }}

        QSlider::groove:horizontal {{
            height: 4px;
            background: {groove_color};
            border-radius: 2px;
        }}

        QSlider::sub-page:horizontal {{
            height: 4px;
            background: {groove_fill};
            border-radius: 2px;
        }}

        QSlider::handle:horizontal {{
            width: 12px;
            margin: -5px 0;
            border-radius: 6px;
            background: {fill_color};
            border: 1px solid {handle_border};
        }}

        QPushButton#SurfaceResetButton {{
            background: transparent;
            color: {text_color};
            border: 1px solid {border_color};
            border-radius: 5px;
            font-weight: 700;
            font-size: 15px;
            padding: 0;
        }}

        QPushButton#SurfaceResetButton:hover {{
            background: {groove_color};
        }}
        """

        for control in (
            self.summaryCard,
            self.matrixWidget,
            self.colorScaleWidget,
            self.boxScaleWidget,
            self.metricsSeparator,
            self.probedRadio,
            self.meshRadio,
            self.wireframeCheck,
            self.zeroPlaneCheck,
            self.colorScaleSlider,
            self.boxScaleSlider,
            self.colorScaleResetButton,
            self.boxScaleResetButton,
        ):
            control.setStyleSheet(style)

        value_style = f"color: {text_color};"
        self.colorScaleValue.setStyleSheet(value_style)
        self.boxScaleValue.setStyleSheet(value_style)

        for label in self.summaryCard.labels.values():
            label.setStyleSheet(
                f"""
                QLabel#SummaryLabel {{
                    background: transparent;
                    color: {muted_color};
                    font-weight: 600;
                }}
                """
            )

        for value in self.summaryCard.values.values():
            value.setStyleSheet(
                f"""
                QLabel#SummaryValue {{
                    background: transparent;
                    color: {value_color};
                    font-weight: 800;
                }}
                """
            )

        for label in (
            self.colorScaleValue,
            self.boxScaleValue,
        ):
            label.setStyleSheet(
                f"""
                QLabel {{
                    background: transparent;
                    color: {text_color};
                    font-weight: 600;
                }}
                """
            )

        for key in (
            "minimum",
            "maximum",
            "average",
            "rms",
            "total_range",
        ):
            wrapper = getattr(self, f"{key}MetricWidget", None)
            if wrapper is not None:
                wrapper.setStyleSheet(style)

    def color_scale(self):
        return self.colorScaleSlider.value() / 100.0

    def box_scale(self):
        return self.boxScaleSlider.value() / 100.0

    def refresh(self):
        if self.current_mesh is None:
            self.graph.show_empty_state()
            return

        elevation, azimuth = self.VIEW_PRESETS[
            self.viewCombo.currentData()
        ]

        self.graph.plot(
            self.current_mesh,
            cmap=self.paletteCombo.currentData(),
            elevation=elevation,
            azimuth=azimuth,
            display_mode=self.display_mode(),
            show_wireframe=self.wireframeCheck.isChecked(),
            show_zero_plane=self.zeroPlaneCheck.isChecked(),
            color_scale=self.color_scale(),
            box_scale=self.box_scale()
        )

    def display_mode(self):
        if self.probedRadio.isChecked():
            return "probed"

        return "mesh"

    def refresh_theme(self, theme_name=None):
        if hasattr(self.graph, "set_theme_name"):
            self.graph.set_theme_name(theme_name)

        self.refresh_control_styles()
        self.refresh()

    def refresh_language(self):
        self.retranslate()

    def refresh_page(self):
        self.refresh_language()
        self.refresh_theme()

    def refresh_view_options(self):
        current_key = (
            self.viewCombo.currentData()
            or str(Config().get("default_surface_view") or "default")
        )

        self.viewCombo.blockSignals(True)
        self.viewCombo.clear()
        self.viewCombo.addItem(
            LanguageManager.text("surface_view_default"),
            "default"
        )
        self.viewCombo.addItem(
            LanguageManager.text("surface_view_front"),
            "front"
        )
        self.viewCombo.addItem(
            LanguageManager.text("surface_view_side"),
            "side"
        )
        self.viewCombo.addItem(
            LanguageManager.text("surface_view_top"),
            "top"
        )
        self.viewCombo.addItem(
            LanguageManager.text("surface_view_detail"),
            "detail"
        )

        index = self.viewCombo.findData(current_key)
        if index < 0:
            index = 0

        self.viewCombo.setCurrentIndex(index)
        self.viewCombo.blockSignals(False)

    def retranslate(self):
        self.refresh_view_options()

        self.summaryCard.setTitle(
            LanguageManager.text("surface_summary")
        )

        self.summaryCard.setTooltip(
            LanguageManager.text("surface_summary_tooltip")
        )

        self.summaryCard.setLabel(
            "palette",
            LanguageManager.text("color_palette")
        )

        self.summaryCard.setLabel(
            "view",
            LanguageManager.text("surface_view_angle")
        )

        self.summaryCard.setLabel(
            "matrix_mode",
            LanguageManager.text("surface_matrix_mode")
        )

        self.probedRadio.setText(
            LanguageManager.text("surface_probed_matrix")
        )
        self.meshRadio.setText(
            LanguageManager.text("surface_mesh_matrix")
        )

        self.summaryCard.setLabel(
            "wireframe",
            LanguageManager.text("surface_wireframe")
        )

        self.summaryCard.setLabel(
            "zero_plane",
            LanguageManager.text("surface_zero_plane")
        )

        self.summaryCard.setLabel(
            "color_scale",
            LanguageManager.text("surface_color_scale")
        )

        self.summaryCard.setLabel(
            "box_scale",
            LanguageManager.text("surface_box_scale")
        )

        self.colorScaleResetButton.setToolTip(
            LanguageManager.text("surface_reset_color_scale")
        )
        self.boxScaleResetButton.setToolTip(
            LanguageManager.text("surface_reset_box_scale")
        )

        self.update_scale_labels()

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
            "rms",
            "RMS"
        )
        self.set_metric_tooltip(
            "rms",
            LanguageManager.text("surface_rms_tooltip")
        )

        self.summaryCard.setLabel(
            "total_range",
            LanguageManager.text("total_deviation")
        )
        self.set_metric_tooltip(
            "total_range",
            LanguageManager.text("surface_total_range_tooltip")
        )

        self.refresh_control_styles()
        self.refresh()
