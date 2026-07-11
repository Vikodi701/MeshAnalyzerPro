"""
MeshAnalyzer Pro
Modern SVG Tool Bar
LanguageManager destekli
"""

from PySide6.QtWidgets import QToolBar
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt, QSize

from languages import LanguageManager
from utils.app_icon import resource_path


class ToolBar(QToolBar):

    def __init__(self):
        super().__init__(LanguageManager.text("app_name"))

        self.setObjectName("MainToolBar")
        self.setMovable(False)
        self.setFloatable(False)

        self.setIconSize(QSize(22, 22))
        self.setMinimumHeight(64)

        self.setToolButtonStyle(
            Qt.ToolButtonStyle.ToolButtonTextBesideIcon
        )

        self.actionOpen = QAction(self.icon("open.svg"), "", self)
        self.actionProjectOpen = QAction(self.icon("project_open.svg"), "", self)
        self.actionProjectSave = QAction(self.icon("project_save.svg"), "", self)

        self.actionHeatmapJPG = QAction(self.icon("heatmap.svg"), "", self)
        self.actionContourJPG = QAction(self.icon("topography.svg"), "", self)
        self.actionSurfaceJPG = QAction(self.icon("surface3d.svg"), "", self)

        self.actionPDF = QAction(self.icon("pdf.svg"), "", self)
        self.actionExportAll = QAction(self.icon("export.svg"), "", self)
        self.actionSettings = QAction(self.icon("settings.svg"), "", self)

        self.addAction(self.actionOpen)
        self.addAction(self.actionProjectOpen)
        self.addAction(self.actionProjectSave)

        self.addSeparator()

        self.addAction(self.actionHeatmapJPG)
        self.addAction(self.actionContourJPG)
        self.addAction(self.actionSurfaceJPG)

        self.addSeparator()

        self.addAction(self.actionPDF)
        self.addAction(self.actionExportAll)

        self.addSeparator()

        self.addAction(self.actionSettings)

        self.retranslate()

    def icon(self, filename):
        return QIcon(str(resource_path("assets", "icons", filename)))

    def retranslate(self):
        self.setWindowTitle(LanguageManager.text("app_name"))

        self.actionOpen.setText(LanguageManager.text("open_conf"))
        self.actionProjectOpen.setText(LanguageManager.text("project_open"))
        self.actionProjectSave.setText(LanguageManager.text("project_save"))

        self.actionHeatmapJPG.setText(LanguageManager.text("heatmap_jpg"))
        self.actionContourJPG.setText(LanguageManager.text("topography_jpg"))
        self.actionSurfaceJPG.setText(LanguageManager.text("surface_3d_jpg"))

        self.actionPDF.setText(LanguageManager.text("pdf"))
        self.actionExportAll.setText(LanguageManager.text("export_all"))
        self.actionSettings.setText(LanguageManager.text("settings"))

        self.actionOpen.setToolTip(LanguageManager.text("toolbar_tooltip_open_conf"))
        self.actionProjectOpen.setToolTip(LanguageManager.text("toolbar_tooltip_project_open"))
        self.actionProjectSave.setToolTip(LanguageManager.text("toolbar_tooltip_project_save"))

        self.actionHeatmapJPG.setToolTip(LanguageManager.text("toolbar_tooltip_heatmap_jpg"))
        self.actionContourJPG.setToolTip(LanguageManager.text("toolbar_tooltip_topography_jpg"))
        self.actionSurfaceJPG.setToolTip(LanguageManager.text("toolbar_tooltip_surface_3d_jpg"))

        self.actionPDF.setToolTip(LanguageManager.text("toolbar_tooltip_pdf"))
        self.actionExportAll.setToolTip(LanguageManager.text("toolbar_tooltip_export_all"))
        self.actionSettings.setToolTip(LanguageManager.text("toolbar_tooltip_settings"))

        self.actionOpen.setStatusTip(LanguageManager.text("toolbar_status_open_conf"))
        self.actionProjectOpen.setStatusTip(LanguageManager.text("toolbar_status_project_open"))
        self.actionProjectSave.setStatusTip(LanguageManager.text("toolbar_status_project_save"))

        self.actionHeatmapJPG.setStatusTip(LanguageManager.text("toolbar_status_heatmap_jpg"))
        self.actionContourJPG.setStatusTip(LanguageManager.text("toolbar_status_topography_jpg"))
        self.actionSurfaceJPG.setStatusTip(LanguageManager.text("toolbar_status_surface_3d_jpg"))

        self.actionPDF.setStatusTip(LanguageManager.text("toolbar_status_pdf"))
        self.actionExportAll.setStatusTip(LanguageManager.text("toolbar_status_export_all"))
        self.actionSettings.setStatusTip(LanguageManager.text("toolbar_status_settings"))