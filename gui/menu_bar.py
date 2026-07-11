"""
MeshAnalyzer Pro
Modern Menu Bar
"""

from PySide6.QtWidgets import (
    QMenuBar,
)
from PySide6.QtGui import QAction

from languages import LanguageManager


class MenuBar(QMenuBar):

    def __init__(self):
        super().__init__()

        self.build_menus()

    def build_menus(self):

        # ==========================
        # Dosya
        # ==========================

        self.fileMenu = self.addMenu("Dosya")

        self.actionOpen = QAction(
            LanguageManager.text("open_conf"),
            self,
        )

        self.actionProjectOpen = QAction(
            LanguageManager.text("project_open"),
            self,
        )

        self.actionProjectSave = QAction(
            LanguageManager.text("project_save"),
            self,
        )

        self.actionPDF = QAction(
            LanguageManager.text("pdf"),
            self,
        )

        self.actionExportAll = QAction(
            LanguageManager.text("export_all"),
            self,
        )

        self.actionExit = QAction(
            "Çıkış",
            self,
        )

        self.fileMenu.addAction(self.actionOpen)
        self.fileMenu.addAction(self.actionProjectOpen)
        self.fileMenu.addAction(self.actionProjectSave)

        self.fileMenu.addSeparator()

        self.fileMenu.addAction(self.actionPDF)
        self.fileMenu.addAction(self.actionExportAll)

        self.fileMenu.addSeparator()

        self.fileMenu.addAction(self.actionExit)

        # ==========================
        # Görünüm
        # ==========================

        self.viewMenu = self.addMenu("Görünüm")

        self.actionDashboard = QAction(
            LanguageManager.text("dashboard"),
            self,
        )

        self.actionMesh = QAction(
            LanguageManager.text("mesh_view"),
            self,
        )

        self.actionHeatmap = QAction(
            LanguageManager.text("heatmap"),
            self,
        )

        self.actionTopography = QAction(
            LanguageManager.text("topography"),
            self,
        )

        self.actionSurface = QAction(
            LanguageManager.text("surface_3d"),
            self,
        )

        self.actionAnalysis = QAction(
            LanguageManager.text("analysis"),
            self,
        )

        self.actionDiagnosis = QAction(
            LanguageManager.text("diagnosis_recommendations"),
            self,
        )

        self.actionCompare = QAction(
            LanguageManager.text("compare"),
            self,
        )

        self.actionHistory = QAction(
            LanguageManager.text("history"),
            self,
        )

        self.viewMenu.addActions([
            self.actionDashboard,
            self.actionMesh,
            self.actionHeatmap,
            self.actionTopography,
            self.actionSurface,
            self.actionAnalysis,
            self.actionDiagnosis,
            self.actionCompare,
            self.actionHistory,
        ])

        # ==========================
        # Araçlar
        # ==========================

        self.toolsMenu = self.addMenu("Araçlar")

        self.actionSettings = QAction(
            LanguageManager.text("settings"),
            self,
        )

        self.toolsMenu.addAction(self.actionSettings)

        # ==========================
        # Help
        # ==========================

        self.helpMenu = self.addMenu(LanguageManager.text("help"))

        self.modulesMenu = self.helpMenu.addMenu(
            LanguageManager.text("modules")
        )

        self.actionHelpDashboard = QAction(
            LanguageManager.text("dashboard"),
            self,
        )

        self.actionHelpMesh = QAction(
            LanguageManager.text("mesh_view"),
        self,
)

        self.actionHelpHeatmap = QAction(
            LanguageManager.text("heatmap"),
            self,
        )

        self.actionHelpTopography = QAction(
            LanguageManager.text("topography"),
            self,
        )

        self.actionHelpSurface = QAction(
            LanguageManager.text("surface_3d"),
            self,
        )

        self.actionHelpAnalysis = QAction(
            LanguageManager.text("analysis"),
            self,
        )

        self.actionHelpDiagnosis = QAction(
            LanguageManager.text("diagnosis_recommendations"),
            self,
        )

        self.actionHelpCompare = QAction(
            LanguageManager.text("compare"),
            self,
        )

        self.actionHelpHistory = QAction(
            LanguageManager.text("history"),
            self,
        )

        self.actionHelpSettings = QAction(
            LanguageManager.text("settings"),
            self,
        )

        self.modulesMenu.addActions([
            self.actionHelpDashboard,
            self.actionHelpMesh,
            self.actionHelpHeatmap,
            self.actionHelpTopography,
            self.actionHelpSurface,
            self.actionHelpAnalysis,
            self.actionHelpDiagnosis,
            self.actionHelpCompare,
            self.actionHelpHistory,
            self.actionHelpSettings,
        ])

        self.helpMenu.addSeparator()

        self.actionAbout = QAction(
            "Hakkında",
            self,
        )

        self.helpMenu.addAction(self.actionAbout)


    def retranslate(self):

        self.fileMenu.setTitle(LanguageManager.text("file"))
        self.viewMenu.setTitle(LanguageManager.text("view"))
        self.toolsMenu.setTitle(LanguageManager.text("tools"))
        self.helpMenu.setTitle(LanguageManager.text("help"))
        self.actionExit.setText(LanguageManager.text("exit"))

        self.modulesMenu.setTitle(LanguageManager.text("modules"))
        self.actionAbout.setText(LanguageManager.text("about"))

        self.actionOpen.setText(LanguageManager.text("open_conf"))
        self.actionProjectOpen.setText(LanguageManager.text("project_open"))
        self.actionProjectSave.setText(LanguageManager.text("project_save"))
        self.actionPDF.setText(LanguageManager.text("pdf"))
        self.actionExportAll.setText(LanguageManager.text("export_all"))

        self.actionDashboard.setText(LanguageManager.text("dashboard"))
        self.actionMesh.setText(LanguageManager.text("mesh_view"))
        self.actionHeatmap.setText(LanguageManager.text("heatmap"))
        self.actionTopography.setText(LanguageManager.text("topography"))
        self.actionSurface.setText(LanguageManager.text("surface_3d"))
        self.actionAnalysis.setText(LanguageManager.text("analysis"))
        self.actionDiagnosis.setText(
            LanguageManager.text("diagnosis_recommendations")
        )
        self.actionCompare.setText(LanguageManager.text("compare"))
        self.actionHistory.setText(LanguageManager.text("history"))

        self.actionSettings.setText(LanguageManager.text("settings"))

        self.actionHelpDashboard.setText(LanguageManager.text("dashboard"))
        self.actionHelpMesh.setText(LanguageManager.text("mesh_view"))
        self.actionHelpHeatmap.setText(LanguageManager.text("heatmap"))
        self.actionHelpTopography.setText(LanguageManager.text("topography"))
        self.actionHelpSurface.setText(LanguageManager.text("surface_3d"))
        self.actionHelpAnalysis.setText(LanguageManager.text("analysis"))
        self.actionHelpDiagnosis.setText(
            LanguageManager.text("diagnosis_recommendations")
        )
        self.actionHelpCompare.setText(LanguageManager.text("compare"))
        self.actionHelpHistory.setText(LanguageManager.text("history"))
        self.actionHelpSettings.setText(LanguageManager.text("settings"))
