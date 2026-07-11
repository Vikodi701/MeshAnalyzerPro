"""
MeshAnalyzer Pro
Settings Page
ThemeManager + LanguageManager destekli
"""

from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout, QHBoxLayout,
    QGridLayout,
    QLabel,
    QDoubleSpinBox,
    QAbstractSpinBox,
    QPushButton,
    QToolButton,
    QFormLayout,
    QComboBox,
    QCheckBox,
    QFrame,
    QApplication,
)
from PySide6.QtGui import QFont

from core.config import Config
from themes.theme_manager import ThemeManager
from languages import LanguageManager
from gui.widgets.info_icon import InfoIcon


class SettingsPage(QWidget):

    languageChanged = Signal()
    themeChanged = Signal(str)
    settingsChanged = Signal()

    def __init__(self):
        super().__init__()

        self.config = Config()

        self.default_total_range = 0.600
        self.default_rms = 0.250
        self.default_plane_deviation = 0.300
        self._loading = False

        layout = QVBoxLayout(self)
        layout.setSpacing(8)

        self.title = QLabel()
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.title.setFont(font)
        layout.addWidget(self.title)


        self.totalLabel = QLabel()
        self.rmsLabel = QLabel()
        self.planeLabel = QLabel()
        self.themeLabel = QLabel()
        self.languageLabel = QLabel()

        self.toleranceSettingsTitle = QLabel()
        self.toleranceSettingsTitle.setObjectName("SettingsSectionTitle")
        self.generalSettingsTitle = QLabel()
        self.generalSettingsTitle.setObjectName("SettingsSectionTitle")

        self.graphSettingsTitle = QLabel()
        self.graphSettingsTitle.setObjectName("SettingsSectionTitle")
        self.defaultHeatmapPaletteLabel = QLabel()
        self.defaultTopographyPaletteLabel = QLabel()
        self.defaultSurfacePaletteLabel = QLabel()
        self.defaultSurfaceViewLabel = QLabel()

        self.reportSettingsTitle = QLabel()
        self.reportSettingsTitle.setObjectName("SettingsSectionTitle")
        self.reportIncludeGraphsCheck = QCheckBox()
        self.reportIncludeDiagnosticsCheck = QCheckBox()
        self.reportIncludeMeshTableCheck = QCheckBox()
        self.exportJpgShowCellValuesCheck = QCheckBox()

        self.totalSpin = QDoubleSpinBox()
        self.totalSpin.setDecimals(3)
        self.totalSpin.setRange(0.000, 100.000)
        self.totalSpin.setSingleStep(0.01)
        self.prepare_limit_spinbox(self.totalSpin)

        self.rmsSpin = QDoubleSpinBox()
        self.rmsSpin.setDecimals(3)
        self.rmsSpin.setRange(0.000, 100.000)
        self.rmsSpin.setSingleStep(0.01)
        self.prepare_limit_spinbox(self.rmsSpin)

        self.planeSpin = QDoubleSpinBox()
        self.planeSpin.setDecimals(3)
        self.planeSpin.setRange(0.000, 100.000)
        self.planeSpin.setSingleStep(0.01)
        self.prepare_limit_spinbox(self.planeSpin)

        self.themeCombo = QComboBox()
        self.themeCombo.addItem("Dark", "dark")
        self.themeCombo.addItem("Light", "light")

        self.languageCombo = QComboBox()
        self.languageCombo.addItem("Türkçe", "tr")
        self.languageCombo.addItem("English", "en")

        self.defaultHeatmapPaletteCombo = QComboBox()
        self.defaultHeatmapPaletteCombo.addItem("Turbo", "turbo")
        self.defaultHeatmapPaletteCombo.addItem("Viridis", "viridis")
        self.defaultHeatmapPaletteCombo.addItem("Coolwarm", "coolwarm")
        self.defaultHeatmapPaletteCombo.addItem("Plasma", "plasma")
        self.defaultHeatmapPaletteCombo.addItem("Inferno", "inferno")
        self.defaultHeatmapPaletteCombo.addItem("Jet", "jet")

        self.defaultTopographyPaletteCombo = QComboBox()
        self.defaultTopographyPaletteCombo.addItem("Terrain", "terrain")
        self.defaultTopographyPaletteCombo.addItem("Turbo", "turbo")
        self.defaultTopographyPaletteCombo.addItem("Viridis", "viridis")
        self.defaultTopographyPaletteCombo.addItem("Coolwarm", "coolwarm")
        self.defaultTopographyPaletteCombo.addItem("Plasma", "plasma")

        self.defaultSurfacePaletteCombo = QComboBox()
        self.defaultSurfacePaletteCombo.addItem("Turbo", "turbo")
        self.defaultSurfacePaletteCombo.addItem("Viridis", "viridis")
        self.defaultSurfacePaletteCombo.addItem("Terrain", "terrain")
        self.defaultSurfacePaletteCombo.addItem("Coolwarm", "coolwarm")
        self.defaultSurfacePaletteCombo.addItem("Plasma", "plasma")

        self.defaultSurfaceViewCombo = QComboBox()

        self.totalResetButton = QPushButton()
        self.totalResetButton.setObjectName("SmallResetButton")
        self.totalResetButton.setFixedWidth(150)

        self.rmsResetButton = QPushButton()
        self.rmsResetButton.setObjectName("SmallResetButton")
        self.rmsResetButton.setFixedWidth(150)

        self.planeResetButton = QPushButton()
        self.planeResetButton.setObjectName("SmallResetButton")
        self.planeResetButton.setFixedWidth(150)

        self.totalRow = QWidget()
        self.totalRowLayout = QHBoxLayout(self.totalRow)
        self.totalRowLayout.setContentsMargins(0, 0, 0, 0)
        self.totalRowLayout.setSpacing(8)
        self.totalSpinButtons = self.create_spin_buttons(self.totalSpin)
        self.totalRowLayout.addWidget(self.totalSpin)
        self.totalRowLayout.addWidget(self.totalSpinButtons)
        self.totalRowLayout.addWidget(self.totalResetButton)

        self.rmsRow = QWidget()
        self.rmsRowLayout = QHBoxLayout(self.rmsRow)
        self.rmsRowLayout.setContentsMargins(0, 0, 0, 0)
        self.rmsRowLayout.setSpacing(8)
        self.rmsSpinButtons = self.create_spin_buttons(self.rmsSpin)
        self.rmsRowLayout.addWidget(self.rmsSpin)
        self.rmsRowLayout.addWidget(self.rmsSpinButtons)
        self.rmsRowLayout.addWidget(self.rmsResetButton)

        self.planeRow = QWidget()
        self.planeRowLayout = QHBoxLayout(self.planeRow)
        self.planeRowLayout.setContentsMargins(0, 0, 0, 0)
        self.planeRowLayout.setSpacing(8)
        self.planeSpinButtons = self.create_spin_buttons(self.planeSpin)
        self.planeRowLayout.addWidget(self.planeSpin)
        self.planeRowLayout.addWidget(self.planeSpinButtons)
        self.planeRowLayout.addWidget(self.planeResetButton)

        self.totalLabelWidget, self.totalInfoIcon, self.totalInfoKey = self.create_label_with_info(
            self.totalLabel,
            "settings_total_deviation_limit_tooltip"
        )
        self.rmsLabelWidget, self.rmsInfoIcon, self.rmsInfoKey = self.create_label_with_info(
            self.rmsLabel,
            "settings_rms_limit_tooltip"
        )
        self.planeLabelWidget, self.planeInfoIcon, self.planeInfoKey = self.create_label_with_info(
            self.planeLabel,
            "settings_plane_deviation_limit_tooltip"
        )

        self.settingsGrid = QGridLayout()
        self.settingsGrid.setContentsMargins(0, 0, 0, 0)
        self.settingsGrid.setHorizontalSpacing(12)
        self.settingsGrid.setVerticalSpacing(10)

        self.toleranceGroup, self.toleranceForm = self.create_settings_group(
            self.toleranceSettingsTitle
        )
        self.toleranceForm.addRow(self.totalLabelWidget, self.totalRow)
        self.toleranceForm.addRow(self.rmsLabelWidget, self.rmsRow)
        self.toleranceForm.addRow(self.planeLabelWidget, self.planeRow)

        self.generalGroup, self.generalForm = self.create_settings_group(
            self.generalSettingsTitle
        )
        self.generalForm.addRow(self.themeLabel, self.themeCombo)
        self.generalForm.addRow(self.languageLabel, self.languageCombo)

        self.graphGroup, self.graphForm = self.create_settings_group(
            self.graphSettingsTitle
        )
        self.graphForm.addRow(
            self.defaultHeatmapPaletteLabel,
            self.defaultHeatmapPaletteCombo
        )
        self.graphForm.addRow(
            self.defaultTopographyPaletteLabel,
            self.defaultTopographyPaletteCombo
        )
        self.graphForm.addRow(
            self.defaultSurfacePaletteLabel,
            self.defaultSurfacePaletteCombo
        )
        self.graphForm.addRow(
            self.defaultSurfaceViewLabel,
            self.defaultSurfaceViewCombo
        )

        self.reportGroup, self.reportForm = self.create_settings_group(
            self.reportSettingsTitle
        )
        self.reportForm.addRow(self.reportIncludeGraphsCheck)
        self.reportForm.addRow(self.reportIncludeDiagnosticsCheck)
        self.reportForm.addRow(self.reportIncludeMeshTableCheck)
        self.reportForm.addRow(self.exportJpgShowCellValuesCheck)

        self.settingsGrid.addWidget(self.toleranceGroup, 0, 0)
        self.settingsGrid.addWidget(self.generalGroup, 0, 1)
        self.settingsGrid.addWidget(self.graphGroup, 1, 0)
        self.settingsGrid.addWidget(self.reportGroup, 1, 1)

        self.settingsGrid.setColumnStretch(0, 1)
        self.settingsGrid.setColumnStretch(1, 1)
        layout.addLayout(self.settingsGrid)

        self.saveButton = QPushButton()
        self.saveButton.setMinimumHeight(42)

        layout.addWidget(self.saveButton)
        layout.addStretch()

        self.load_settings()
        self.retranslate()

        self.themeCombo.currentIndexChanged.connect(
            self.on_theme_changed
        )

        self.totalResetButton.clicked.connect(self.reset_total_range)
        self.rmsResetButton.clicked.connect(self.reset_rms)
        self.planeResetButton.clicked.connect(self.reset_plane_deviation)

        self.saveButton.clicked.connect(self.save_settings)

    def create_settings_group(self, title_label):
        frame = QFrame()
        frame.setObjectName("SettingsGroupFrame")

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(6)

        layout.addWidget(title_label)

        form = QFormLayout()
        form.setContentsMargins(0, 0, 0, 0)
        form.setHorizontalSpacing(12)
        form.setVerticalSpacing(6)

        layout.addLayout(form)

        return frame, form

    def create_label_with_info(self, label_widget, tooltip_key):
        container = QWidget()
        container.setObjectName("SettingsLabelInfoRow")

        layout = QHBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(6)

        icon = InfoIcon("")
        layout.addWidget(label_widget)
        layout.addWidget(icon)
        layout.addStretch()

        return container, icon, tooltip_key

    def create_spin_buttons(self, spinbox):
        container = QWidget()
        container.setObjectName("SpinStepContainer")

        layout = QVBoxLayout(container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        up_button = QToolButton()
        up_button.setObjectName("SpinStepButton")
        up_button.setText("▲")
        up_button.setAutoRepeat(True)
        up_button.setAutoRepeatDelay(250)
        up_button.setAutoRepeatInterval(80)
        up_button.clicked.connect(spinbox.stepUp)

        down_button = QToolButton()
        down_button.setObjectName("SpinStepButton")
        down_button.setText("▼")
        down_button.setAutoRepeat(True)
        down_button.setAutoRepeatDelay(250)
        down_button.setAutoRepeatInterval(80)
        down_button.clicked.connect(spinbox.stepDown)

        layout.addWidget(up_button)
        layout.addWidget(down_button)

        return container

    def reset_total_range(self):
        self.totalSpin.setValue(
            getattr(self, "DEFAULT_TOTAL_RANGE", self.default_total_range)
        )

    def reset_rms(self):
        self.rmsSpin.setValue(
            getattr(self, "DEFAULT_RMS", self.default_rms)
        )

    def reset_plane_deviation(self):
        self.planeSpin.setValue(
            getattr(self, "DEFAULT_PLANE_DEVIATION", self.default_plane_deviation)
        )

    def reset_all_limits(self):
        self.reset_total_range()
        self.reset_rms()
        self.reset_plane_deviation()

    def prepare_limit_spinbox(self, spinbox):
        """
        Native QDoubleSpinBox okları bazı Windows temalarında tek ok gibi
        görünebildiği için kapatılır. Arttırma/azaltma işlemi özel üçgen
        butonlarla yapılır.
        """
        spinbox.setButtonSymbols(
            QAbstractSpinBox.ButtonSymbols.NoButtons
        )
        spinbox.setAccelerated(True)
        spinbox.setKeyboardTracking(False)
        spinbox.setMinimumHeight(36)


    def set_combo_value(self, combo, value, fallback_index=0):
        index = combo.findData(value)
        if index < 0:
            index = fallback_index
        combo.setCurrentIndex(index)

    def refresh_surface_view_options(self):
        current = self.defaultSurfaceViewCombo.currentData()

        if current is None:
            current = str(self.config.get("default_surface_view") or "default")

        self.defaultSurfaceViewCombo.blockSignals(True)
        self.defaultSurfaceViewCombo.clear()
        self.defaultSurfaceViewCombo.addItem(
            LanguageManager.text("surface_view_default"),
            "default"
        )
        self.defaultSurfaceViewCombo.addItem(
            LanguageManager.text("surface_view_front"),
            "front"
        )
        self.defaultSurfaceViewCombo.addItem(
            LanguageManager.text("surface_view_side"),
            "side"
        )
        self.defaultSurfaceViewCombo.addItem(
            LanguageManager.text("surface_view_top"),
            "top"
        )
        self.defaultSurfaceViewCombo.addItem(
            LanguageManager.text("surface_view_detail"),
            "detail"
        )

        self.set_combo_value(
            self.defaultSurfaceViewCombo,
            current,
            0
        )
        self.defaultSurfaceViewCombo.blockSignals(False)

    def load_settings(self):
        self._loading = True

        self.totalSpin.setValue(float(self.config.get("max_total_range")))
        self.rmsSpin.setValue(float(self.config.get("max_rms")))
        self.planeSpin.setValue(float(self.config.get("max_plane_deviation")))

        current_theme = str(self.config.get("theme"))
        theme_index = self.themeCombo.findData(current_theme)

        if theme_index < 0:
            theme_index = self.themeCombo.findData("dark")

        self.themeCombo.setCurrentIndex(theme_index)

        current_language = str(self.config.get("language"))
        language_index = self.languageCombo.findData(current_language)

        if language_index < 0:
            language_index = self.languageCombo.findData("tr")

        self.languageCombo.setCurrentIndex(language_index)

        self.set_combo_value(
            self.defaultHeatmapPaletteCombo,
            str(self.config.get("default_heatmap_palette") or "turbo"),
            0
        )
        self.set_combo_value(
            self.defaultTopographyPaletteCombo,
            str(self.config.get("default_topography_palette") or "terrain"),
            0
        )
        self.set_combo_value(
            self.defaultSurfacePaletteCombo,
            str(self.config.get("default_surface_palette") or "turbo"),
            0
        )
        self.refresh_surface_view_options()

        self.reportIncludeGraphsCheck.setChecked(
            bool(self.config.get("report_include_graphs"))
        )
        self.reportIncludeDiagnosticsCheck.setChecked(
            bool(self.config.get("report_include_diagnostics"))
        )
        self.reportIncludeMeshTableCheck.setChecked(
            bool(self.config.get("report_include_mesh_table"))
        )
        self.exportJpgShowCellValuesCheck.setChecked(
            bool(self.config.get("export_jpg_show_cell_values"))
        )

        self._loading = False

    def on_theme_changed(self, *args):
        """
        Tema combobox'ta değiştiği anda uygulanır.
        Böylece Heatmap, Topography ve 3B görünüm sayfaları
        kaydet butonuna basmadan yeni temaya göre yenilenir.
        """
        if self._loading:
            return

        selected_theme = self.themeCombo.currentData()

        if not selected_theme:
            return

        self.config.set("theme", selected_theme)

        app = QApplication.instance()
        ThemeManager.apply(
            app,
            selected_theme
        )

        if app is not None:
            app.processEvents()

        self.themeChanged.emit(str(selected_theme))


    def save_settings(self):
        old_language = LanguageManager.current_language()
        old_theme = str(self.config.get("theme"))

        selected_theme = self.themeCombo.currentData()
        selected_language = self.languageCombo.currentData()

        self.config.set("max_total_range", self.totalSpin.value())
        self.config.set("max_rms", self.rmsSpin.value())
        self.config.set("max_plane_deviation", self.planeSpin.value())
        self.config.set("theme", selected_theme)
        self.config.set(
            "default_heatmap_palette",
            self.defaultHeatmapPaletteCombo.currentData()
        )
        self.config.set(
            "default_topography_palette",
            self.defaultTopographyPaletteCombo.currentData()
        )
        self.config.set(
            "default_surface_palette",
            self.defaultSurfacePaletteCombo.currentData()
        )
        self.config.set(
            "default_surface_view",
            self.defaultSurfaceViewCombo.currentData()
        )
        self.config.set(
            "report_include_graphs",
            self.reportIncludeGraphsCheck.isChecked()
        )
        self.config.set(
            "report_include_diagnostics",
            self.reportIncludeDiagnosticsCheck.isChecked()
        )
        self.config.set(
            "report_include_mesh_table",
            self.reportIncludeMeshTableCheck.isChecked()
        )
        self.config.set(
            "export_jpg_show_cell_values",
            self.exportJpgShowCellValuesCheck.isChecked()
        )
        LanguageManager.set_language(selected_language)

        app = QApplication.instance()
        ThemeManager.apply(
            app,
            selected_theme
        )

        if app is not None:
            app.processEvents()

        if selected_language != old_language:
            self.languageChanged.emit()

        if selected_theme != old_theme:
            self.themeChanged.emit(str(selected_theme))

        self.settingsChanged.emit()

    def retranslate(self):
        self.title.setText(LanguageManager.text("settings_title"))

        self.totalLabel.setText(LanguageManager.text("max_total_range"))
        self.rmsLabel.setText(LanguageManager.text("max_rms"))
        self.planeLabel.setText(LanguageManager.text("max_plane_deviation"))
        self.themeLabel.setText(LanguageManager.text("theme"))
        self.languageLabel.setText(LanguageManager.text("language"))

        self.toleranceSettingsTitle.setText(
            LanguageManager.text("settings_tolerance_settings")
        )
        self.generalSettingsTitle.setText(
            LanguageManager.text("settings_general_settings")
        )

        self.graphSettingsTitle.setText(
            LanguageManager.text("settings_graph_defaults")
        )
        self.defaultHeatmapPaletteLabel.setText(
            LanguageManager.text("settings_default_heatmap_palette")
        )
        self.defaultTopographyPaletteLabel.setText(
            LanguageManager.text("settings_default_topography_palette")
        )
        self.defaultSurfacePaletteLabel.setText(
            LanguageManager.text("settings_default_surface_palette")
        )
        self.defaultSurfaceViewLabel.setText(
            LanguageManager.text("settings_default_surface_view")
        )
        self.refresh_surface_view_options()

        self.reportSettingsTitle.setText(
            LanguageManager.text("settings_report_settings")
        )
        self.reportIncludeGraphsCheck.setText(
            LanguageManager.text("settings_report_include_graphs")
        )
        self.reportIncludeDiagnosticsCheck.setText(
            LanguageManager.text("settings_report_include_diagnostics")
        )
        self.reportIncludeMeshTableCheck.setText(
            LanguageManager.text("settings_report_include_mesh_table")
        )
        self.exportJpgShowCellValuesCheck.setText(
            LanguageManager.text("settings_export_jpg_show_cell_values")
        )

        self.totalInfoIcon.setToolTip(
            LanguageManager.text("settings_total_deviation_limit_tooltip")
        )
        self.rmsInfoIcon.setToolTip(
            LanguageManager.text("settings_rms_limit_tooltip")
        )
        self.planeInfoIcon.setToolTip(
            LanguageManager.text("settings_plane_deviation_limit_tooltip")
        )

        self.totalResetButton.setText(LanguageManager.text("reset_to_default"))
        self.rmsResetButton.setText(LanguageManager.text("reset_to_default"))
        self.planeResetButton.setText(LanguageManager.text("reset_to_default"))
        self.saveButton.setText(LanguageManager.text("save_settings"))
