"""
MeshAnalyzer Pro
gui/main_window.py
Project .meshproj + PDF + JPG Export + Export All + History Load
Sidebar sync destekli sürüm
"""

from datetime import datetime
import os

from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget,
    QStatusBar,
    QMessageBox,
    QFileDialog,
)

from gui.navigation import Navigation
from gui.menu_bar import MenuBar
from gui.tool_bar import ToolBar
from PySide6.QtCore import QTimer
from languages import LanguageManager

from gui.pages.dashboard_page import DashboardPage
from gui.pages.mesh_page import MeshPage
from gui.pages.heatmap_page import HeatmapPage
from gui.pages.contour_page import ContourPage
from gui.pages.surface_page import SurfacePage
from gui.pages.analysis_page import AnalysisPage
from gui.pages.diagnosis_page import DiagnosisPage
from gui.pages.compare_page import ComparePage
from gui.pages.history_page import HistoryPage
from gui.pages.settings_page import SettingsPage

from core.parser import MeshParser
from core.config import Config
from core.analysis import AnalysisCache
from controllers.mesh_controller import MeshController

from reports.pdf_report import PDFReport
from reports.export_all import ExportAll

from database.database import Database
from gui.dialogs.help_dialog import HelpDialog
from utils.app_icon import apply_app_icon

from core.project import (
    ProjectSaver,
    ProjectLoader,
    ProjectValidator,
)


class MainWindow(QMainWindow):

    def apply_startup_window_state(self):
        self.showMaximized()

    def apply_current_appearance_settings(self):
        # Pencere durumu ayarlar kaydedildiğinde değiştirilmez.
        # Uygulama varsayılan olarak açılışta tam ekran/maximized başlar.
        return

    def iter_pages(self):
        return [
            getattr(self, "dashboard_page", None),
            getattr(self, "mesh_page", None),
            getattr(self, "heatmap_page", None),
            getattr(self, "contour_page", None),
            getattr(self, "surface_page", None),
            getattr(self, "analysis_page", None),
            getattr(self, "diagnosis_page", None),
            getattr(self, "compare_page", None),
            getattr(self, "history_page", None),
            getattr(self, "settings_page", None),
        ]

    def refresh_all_pages_theme(self, *args):
        """
        Tema değiştiğinde tüm sayfaları anında ve güvenli şekilde yeniler.
        Ayarlar sayfası seçilen tema adını sinyal ile gönderir; böylece
        grafikler Config dosyasını tekrar okumayı beklemeden doğru temaya geçer.
        """
        theme_name = None

        if args and args[0]:
            theme_name = str(args[0])
        else:
            theme_name = str(Config().get("theme"))

        self._refresh_all_pages_theme_now(theme_name)
        QTimer.singleShot(0, lambda: self._refresh_all_pages_theme_now(theme_name))
        QTimer.singleShot(80, lambda: self._refresh_all_pages_theme_now(theme_name))

    def _refresh_all_pages_theme_now(self, theme_name=None):
        if not theme_name:
            theme_name = str(Config().get("theme"))

        self.setProperty("theme", theme_name)
        self.style().unpolish(self)
        self.style().polish(self)
        self.update()

        for page in self.iter_pages():
            if page is None:
                continue

            page.setProperty("theme", theme_name)
            page.style().unpolish(page)
            page.style().polish(page)
            page.update()

            if hasattr(page, "refresh_theme"):
                try:
                    page.refresh_theme(theme_name)
                except TypeError:
                    page.refresh_theme()
            elif hasattr(page, "retranslate"):
                page.retranslate()

    def refresh_all_pages_language(self):
        for page in self.iter_pages():
            if page is None:
                continue

            if hasattr(page, "refresh_language"):
                page.refresh_language()
            elif hasattr(page, "retranslate"):
                page.retranslate()

    def refresh_current_mesh_after_settings(self):
        """
        Ayarlar kaydedildiğinde veya görünüm ayarları değiştiğinde
        tüm sayfaları anında yeniler. Mesh varsa analiz cache temizlenir
        ve mesh bağımlı sayfalar tekrar beslenir.
        """
        self.apply_current_appearance_settings()

        try:
            AnalysisCache.instance().clear()
        except Exception:
            pass

        if self.current_mesh is not None:
            self.mesh_controller.set_mesh(self.current_mesh)

        self.refresh_all_pages_theme(str(Config().get("theme")))

        for page in self.iter_pages():
            if page is None:
                continue

            if self.current_mesh is not None and hasattr(page, "update_mesh"):
                try:
                    page.update_mesh(self.current_mesh)
                except TypeError:
                    pass
                except Exception:
                    pass

            if hasattr(page, "refresh_page"):
                try:
                    page.refresh_page()
                except TypeError:
                    pass
                except Exception:
                    pass

        if self.statusBar() is not None:
            self.statusBar().showMessage(
                LanguageManager.text("settings_applied")
            )


    def show_about(self):

        QMessageBox.about(
            self,
            "MeshAnalyzer Pro",

            """
        <h2>MeshAnalyzer Pro</h2>

        <p><b>Version:</b> 1.0.0</p>

        <p>
        Precision Surface Analysis Software
        </p>

        <hr>

        <p>
        © 2026 Vikodi 
        </p>
        """
    )
    
    def show_help(self, topic):
        if getattr(self, "_active_help_dialog", None) is not None:
            try:
                self._active_help_dialog.close()
            except Exception:
                pass

        dialog = HelpDialog(topic, self)
        self._active_help_dialog = dialog
        dialog.finished.connect(lambda _result: setattr(self, "_active_help_dialog", None))
        dialog.open_non_modal()

    def __init__(self):
        super().__init__()

        self.parser = MeshParser()
        self.mesh_controller = MeshController()

        self.database = Database()

        self.projectSaver = ProjectSaver()
        self.projectLoader = ProjectLoader()
        self.projectValidator = ProjectValidator()

        self.current_mesh = None

        self.setWindowTitle("MeshAnalyzer Pro")
        apply_app_icon(window=self)
        self.resize(1500, 900)

        self.build_ui()

    def build_ui(self):
        self.menu = MenuBar()
        self.setMenuBar(self.menu)

        self.toolbar = ToolBar()
        self.addToolBar(self.toolbar)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)

        self.navigation = Navigation()
        self.pages = QStackedWidget()

        self.dashboard_page = DashboardPage()
        self.mesh_page = MeshPage()
        self.heatmap_page = HeatmapPage()
        self.contour_page = ContourPage()
        self.surface_page = SurfacePage()
        self.analysis_page = AnalysisPage()
        self.diagnosis_page = DiagnosisPage()
        self.compare_page = ComparePage()
        self.history_page = HistoryPage()
        self.settings_page = SettingsPage()

        self.pages.addWidget(self.dashboard_page)
        self.pages.addWidget(self.mesh_page)
        self.pages.addWidget(self.heatmap_page)
        self.pages.addWidget(self.contour_page)
        self.pages.addWidget(self.surface_page)
        self.pages.addWidget(self.analysis_page)
        self.pages.addWidget(self.diagnosis_page)
        self.pages.addWidget(self.compare_page)
        self.pages.addWidget(self.history_page)
        self.pages.addWidget(self.settings_page)

        self.mesh_controller.meshLoaded.connect(self.dashboard_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.mesh_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.heatmap_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.contour_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.surface_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.analysis_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.diagnosis_page.update_mesh)
        self.mesh_controller.meshLoaded.connect(self.compare_page.update_mesh)

        self.navigation.pageChanged.connect(self.change_page)
        self.history_page.meshSelected.connect(self.load_history_mesh)

        self.settings_page.languageChanged.connect(
            self.retranslate_ui
        )

        self.settings_page.themeChanged.connect(
            self.refresh_all_pages_theme
        )

        self.settings_page.settingsChanged.connect(
            self.refresh_current_mesh_after_settings
        )

        layout.addWidget(self.navigation)
        layout.addWidget(self.pages)

        self.setStatusBar(QStatusBar())
        self.statusBar().showMessage("Hazır")

        self.connect_actions()

        self.menu.actionHelpDashboard.triggered.connect(
            lambda: self.show_help("dashboard")
        )

        self.menu.actionHelpMesh.triggered.connect(
            lambda: self.show_help("mesh")
        )

        self.menu.actionHelpHeatmap.triggered.connect(
            lambda: self.show_help("heatmap")
        )

        self.menu.actionHelpTopography.triggered.connect(
            lambda: self.show_help("topography")
        )

        self.menu.actionHelpSurface.triggered.connect(
            lambda: self.show_help("surface3d")
        )

        self.menu.actionHelpAnalysis.triggered.connect(
            lambda: self.show_help("analysis")
        )

        self.menu.actionHelpDiagnosis.triggered.connect(
            lambda: self.show_help("diagnosis")
        )

        self.menu.actionHelpCompare.triggered.connect(
            lambda: self.show_help("compare")
        )

        self.menu.actionHelpHistory.triggered.connect(
            lambda: self.show_help("history")
        )

        self.menu.actionHelpSettings.triggered.connect(
            lambda: self.show_help("settings")
        )

    def retranslate_ui(self):

        self.refresh_all_pages_language()

        self.setWindowTitle("MeshAnalyzer Pro")

        if hasattr(self.menu, "retranslate"):
            self.menu.retranslate()

        if hasattr(self.navigation, "retranslate"):
            self.navigation.retranslate()

        if hasattr(self.toolbar, "retranslate"):
            self.toolbar.retranslate()

        self.statusBar().showMessage(
            LanguageManager.text("ready")
         )

    def connect_actions(self):
        self.toolbar.actionOpen.triggered.connect(self.open_file)
        self.toolbar.actionProjectOpen.triggered.connect(self.open_project)
        self.toolbar.actionProjectSave.triggered.connect(self.save_project)

        self.toolbar.actionHeatmapJPG.triggered.connect(
            self.export_heatmap_jpeg
        )

        self.toolbar.actionContourJPG.triggered.connect(
            self.export_contour_jpeg
        )

        self.toolbar.actionSurfaceJPG.triggered.connect(
            self.export_surface_jpeg
        )

        self.toolbar.actionPDF.triggered.connect(self.export_pdf)
        self.toolbar.actionExportAll.triggered.connect(self.export_all)

        self.toolbar.actionSettings.triggered.connect(
            lambda: self.change_page(9)
        )

        # ==========================
        # Menu Bar
        # ==========================

        self.menu.actionOpen.triggered.connect(self.open_file)

        self.menu.actionProjectOpen.triggered.connect(
            self.open_project
        )

        self.menu.actionProjectSave.triggered.connect(
            self.save_project
        )

        self.menu.actionPDF.triggered.connect(
            self.export_pdf
        )

        self.menu.actionExportAll.triggered.connect(
            self.export_all
        )

        self.menu.actionExit.triggered.connect(
            self.close
        )

        # ==========================
        # View Menu
        # ==========================

        self.menu.actionDashboard.triggered.connect(
            lambda: self.change_page(0)
        )

        self.menu.actionMesh.triggered.connect(
            lambda: self.change_page(1)
        )

        self.menu.actionHeatmap.triggered.connect(
            lambda: self.change_page(2)
        )

        self.menu.actionTopography.triggered.connect(
            lambda: self.change_page(3)
        )

        self.menu.actionSurface.triggered.connect(
            lambda: self.change_page(4)
        )

        self.menu.actionAnalysis.triggered.connect(
            lambda: self.change_page(5)
        )

        self.menu.actionDiagnosis.triggered.connect(
            lambda: self.change_page(6)
        )

        # ==========================
        # Tools
        # ==========================

        self.menu.actionSettings.triggered.connect(
            lambda: self.change_page(9)
        )

        self.menu.actionCompare.triggered.connect(
            lambda: self.change_page(7)
        )

        self.menu.actionHistory.triggered.connect(
            lambda: self.change_page(8)
        )

        # ==========================
        # Help
        # ==========================

        self.menu.actionAbout.triggered.connect(
          self.show_about
        )

    def change_page(self, index):
        """
        Sidebar ve QStackedWidget sayfa geçişini senkronize eder.
        """

        self.pages.setCurrentIndex(index)

        if hasattr(self.navigation, "setCurrentPage"):
            self.navigation.setCurrentPage(index)

        page = self.pages.widget(index)
        if page is getattr(self, "diagnosis_page", None):
            page.refresh_language()

    def open_file(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Mesh veya Pack Aç",
            "",
            "Mesh Dosyaları (*.pack *.csv *.txt *.json);;Tüm Dosyalar (*)"
        )

        if not filename:
            return

        try:
            mesh = self.parser.load(filename)

            self.current_mesh = mesh

            self.database.save_mesh(mesh)
            self.history_page.load_history()

            self.mesh_controller.set_mesh(mesh)

            self.statusBar().showMessage(
                f"Mesh yüklendi ve geçmişe kaydedildi: {mesh.name}"
            )

            self.change_page(0)

        except Exception as error:
            QMessageBox.critical(
                self,
                "Dosya okunamadı",
                str(error)
            )

            self.statusBar().showMessage("Hata")

    def load_history_mesh(self, mesh):
        self.current_mesh = mesh

        self.mesh_controller.set_mesh(mesh)

        self.statusBar().showMessage(
            f"History'den yüklendi: {mesh.name}"
        )

        self.change_page(0)

    def save_project(self):
        if self.current_mesh is None:
            QMessageBox.warning(
                self,
                "Proje Kaydedilemedi",
                "Önce bir mesh açın."
            )
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        mesh_name = os.path.splitext(
            os.path.basename(self.current_mesh.name)
        )[0]

        default_name = f"MeshAnalyzer_{mesh_name}_{timestamp}.meshproj"

        filename, _ = QFileDialog.getSaveFileName(
            self,
            "Proje Kaydet",
            default_name,
            "Mesh Project (*.meshproj)"
        )

        if not filename:
            return

        try:
            saved_file = self.projectSaver.save(
                self.current_mesh,
                filename
            )

            self.statusBar().showMessage(
                f"Proje kaydedildi: {os.path.basename(saved_file)}"
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Proje Kaydetme Hatası",
                str(error)
            )

            self.statusBar().showMessage("Proje kaydedilemedi.")

    def open_project(self):
        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Proje Aç",
            "",
            "Mesh Project (*.meshproj)"
        )

        if not filename:
            return

        valid, message = self.projectValidator.validate(filename)

        if not valid:
            QMessageBox.warning(
                self,
                "Geçersiz Proje",
                message
            )
            return

        try:
            mesh = self.projectLoader.load(filename)

            self.current_mesh = mesh
            self.mesh_controller.set_mesh(mesh)

            self.statusBar().showMessage(
                f"Proje açıldı: {mesh.name}"
            )

            self.change_page(0)

        except Exception as error:
            QMessageBox.critical(
                self,
                "Proje Açma Hatası",
                str(error)
            )

            self.statusBar().showMessage("Proje açılamadı.")

    def export_pdf(self):
        if self.current_mesh is None:
            QMessageBox.warning(
                self,
                LanguageManager.text("export_pdf_failed_title"),
                LanguageManager.text("export_mesh_required_message")
            )
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        mesh_name = os.path.splitext(
            os.path.basename(self.current_mesh.name)
        )[0]

        default_name = f"MeshAnalyzer_{mesh_name}_{timestamp}.pdf"

        filename, _ = QFileDialog.getSaveFileName(
            self,
            LanguageManager.text("export_pdf_save_title"),
            default_name,
            "PDF Files (*.pdf)"
        )

        if not filename:
            return

        try:
            report = PDFReport(self.current_mesh)
            report.save(filename)

            self.statusBar().showMessage(
                LanguageManager.text("export_pdf_created_status").format(
                    filename=os.path.basename(filename)
                )
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                LanguageManager.text("export_pdf_error_title"),
                str(error)
            )

            self.statusBar().showMessage(
                LanguageManager.text("export_pdf_failed_status")
            )

    def export_heatmap_jpeg(self):
        self.export_single_jpeg(
            title=LanguageManager.text("export_heatmap_jpeg_save_title"),
            default_prefix="Heatmap",
            save_function_name="save_heatmap_jpeg"
        )

    def export_contour_jpeg(self):
        self.export_single_jpeg(
            title=LanguageManager.text("export_topography_jpg_save_title"),
            default_prefix="Topographic",
            save_function_name="save_contour_jpeg"
        )

    def export_surface_jpeg(self):
        self.export_single_jpeg(
            title=LanguageManager.text("export_surface_jpg_save_title"),
            default_prefix="Surface3D",
            save_function_name="save_surface_jpeg"
        )

    def export_single_jpeg(self, title, default_prefix, save_function_name):
        if self.current_mesh is None:
            QMessageBox.warning(
                self,
                LanguageManager.text("export_jpeg_failed_title"),
                LanguageManager.text("export_mesh_required_message")
            )
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        mesh_name = os.path.splitext(
            os.path.basename(self.current_mesh.name)
        )[0]

        default_name = f"{default_prefix}_{mesh_name}_{timestamp}.jpg"

        filename, _ = QFileDialog.getSaveFileName(
            self,
            title,
            default_name,
            "JPEG Files (*.jpg)"
        )

        if not filename:
            return

        try:
            report = PDFReport(self.current_mesh)
            save_func = getattr(report, save_function_name)
            save_func(filename)

            self.statusBar().showMessage(
                LanguageManager.text("export_jpeg_created_status").format(
                    filename=os.path.basename(filename)
                )
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                LanguageManager.text("export_jpeg_error_title"),
                str(error)
            )

            self.statusBar().showMessage(
                LanguageManager.text("export_jpeg_failed_status")
            )

    def export_all(self):
        if self.current_mesh is None:
            QMessageBox.warning(
                self,
                "Dışa Aktarma Yapılamadı",
                "Önce bir mesh dosyası açmalısın."
            )
            return

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        mesh_name = os.path.splitext(
            os.path.basename(self.current_mesh.name)
        )[0]

        default_folder = f"MeshAnalyzer_{mesh_name}_{timestamp}"

        folder = QFileDialog.getExistingDirectory(
            self,
            "Tümünü Dışa Aktar Klasörü Seç"
        )

        if not folder:
            return

        export_path = os.path.join(folder, default_folder)

        try:
            exporter = ExportAll(self.current_mesh)
            exporter.save(export_path)

            self.statusBar().showMessage(
                f"Dışa aktarma tamamlandı: {default_folder}"
            )

        except Exception as error:
            QMessageBox.critical(
                self,
                "Dışa Aktarma Hatası",
                str(error)
            )

            self.statusBar().showMessage("Dışa aktarma başarısız.")
