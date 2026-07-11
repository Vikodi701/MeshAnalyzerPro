"""
MeshAnalyzer Pro
Dashboard Page
LanguageManager + ToolTips destekli sürüm
"""

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QGridLayout,
    QVBoxLayout,
)

from PySide6.QtCore import Qt

from gui.widgets.info_card import InfoCard
from gui.widgets.health_card import HealthCard
from gui.tooltips import ToolTips
from languages import LanguageManager
from core.analysis import AnalysisEngine


class DashboardPage(QWidget):

    def __init__(self):
        super().__init__()
        self.current_mesh = None
        self.current_analysis = None
        self.build_ui()

    def build_ui(self):
        main_layout = QVBoxLayout(self)

        # Panel başlığı kaldırıldı; üst alana sorumluluk reddi eklendi.
        self.titleLabel = QLabel()
        self.titleLabel.hide()

        self.disclaimerLabel = QLabel()
        self.disclaimerLabel.setObjectName("DashboardDisclaimer")
        self.disclaimerLabel.setWordWrap(True)
        self.disclaimerLabel.setAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )
        main_layout.addWidget(self.disclaimerLabel)

        grid = QGridLayout()
        grid.setHorizontalSpacing(16)
        grid.setVerticalSpacing(16)

        self.statusCard = InfoCard(
            "",
            "--",
            "",
            "#95A5A6",
            tooltip=ToolTips.quality_status()
        )

        self.healthCard = HealthCard(0, "")
        self.healthCard.setTooltip(ToolTips.machine_health())
        self.healthCard.setMinimumSize(320, 420)

        self.rangeCard = InfoCard(
            "",
            "--",
            "",
            "#3498DB",
            tooltip=ToolTips.total_range()
        )

        self.rmsCard = InfoCard(
            "",
            "--",
            "",
            "#9B59B6",
            tooltip=ToolTips.rms()
        )

        self.planeCard = InfoCard(
            "",
            "--",
            "",
            "#E67E22",
            tooltip=ToolTips.plane_deviation()
        )

        self.sizeCard = InfoCard(
            "",
            "--",
            "",
            "#27AE60",
            tooltip=ToolTips.mesh_size()
        )

        self.minCard = InfoCard(
            "",
            "--",
            "",
            "#2980B9",
            tooltip=ToolTips.minimum()
        )

        self.maxCard = InfoCard(
            "",
            "--",
            "",
            "#C0392B",
            tooltip=ToolTips.maximum()
        )

        self.avgCard = InfoCard(
            "",
            "--",
            "",
            "#16A085",
            tooltip=ToolTips.average()
        )

        self.fileCard = InfoCard(
            "",
            "--",
            "",
            "#7F8C8D",
            tooltip=ToolTips.file_info()
        )

        self.analysisCard = InfoCard(
            "",
            "--",
            "",
            "#34495E",
            tooltip=ToolTips.analysis_result()
        )

        grid.addWidget(self.healthCard, 0, 0, 3, 1)
        grid.addWidget(self.statusCard, 0, 1)
        grid.addWidget(self.rangeCard, 0, 2)

        grid.addWidget(self.rmsCard, 1, 1)
        grid.addWidget(self.planeCard, 1, 2)

        grid.addWidget(self.minCard, 2, 1)
        grid.addWidget(self.maxCard, 2, 2)

        grid.addWidget(self.avgCard, 3, 0)
        grid.addWidget(self.sizeCard, 3, 1)
        grid.addWidget(self.fileCard, 3, 2)

        grid.addWidget(self.analysisCard, 4, 0, 1, 3)

        main_layout.addLayout(grid)
        main_layout.addStretch()

        self.retranslate()

    def status_text(self, status):
        text = str(status).strip().upper()
        keys = {
            "PASS": "status_pass",
            "OK": "status_ok",
            "EXCELLENT": "status_excellent",
            "GOOD": "status_good",
            "WARNING": "status_warning",
            "WARN": "status_warning",
            "ACCEPTABLE": "status_acceptable",
            "FAIL": "status_fail",
            "ERROR": "status_error",
            "BAD": "status_bad",
            "CRITICAL": "status_critical",
        }

        key = keys.get(text)
        if not key:
            return str(status)

        translated = LanguageManager.text(key)
        return translated if translated != key else str(status)

    def update_mesh(self, mesh):
        self.current_mesh = mesh

        analysis = AnalysisEngine(mesh).run()
        self.current_analysis = analysis

        tolerance_result = analysis.tolerance
        geometry = analysis.geometry
        health = analysis.health

        status = tolerance_result["status"]

        if status == "PASS":
            self.statusCard.setValue(f"🟢 {self.status_text(status)}")
            self.statusCard.setFooter(
                LanguageManager.text("tolerance_ok")
            )
            self.statusCard.setColor("#2ECC71")

            self.analysisCard.setValue(
                LanguageManager.text("analysis_ok")
            )
            self.analysisCard.setFooter(
                LanguageManager.text("mesh_quality_passed")
            )
            self.analysisCard.setColor("#2ECC71")

        elif status == "ACCEPTABLE":
            self.statusCard.setValue(f"🟡 {self.status_text(status)}")
            self.statusCard.setFooter(
                LanguageManager.text("acceptable_range")
            )
            self.statusCard.setColor("#F1C40F")

            self.analysisCard.setValue(
                LanguageManager.text("acceptable")
            )
            self.analysisCard.setFooter(
                LanguageManager.text("mesh_quality_acceptable")
            )
            self.analysisCard.setColor("#F1C40F")

        elif status == "WARNING":
            self.statusCard.setValue(f"🟠 {self.status_text(status)}")
            self.statusCard.setFooter(
                LanguageManager.text("check_recommended")
            )
            self.statusCard.setColor("#F97316")

            self.analysisCard.setValue(
                LanguageManager.text("attention")
            )
            self.analysisCard.setFooter(
                LanguageManager.text("mesh_check_recommended")
            )
            self.analysisCard.setColor("#F97316")

        else:
            self.statusCard.setValue(f"🔴 {self.status_text(status)}")
            self.statusCard.setFooter(
                LanguageManager.text("out_of_tolerance")
            )
            self.statusCard.setColor("#E74C3C")

            self.analysisCard.setValue(
                LanguageManager.text("inspection_required")
            )
            self.analysisCard.setFooter(
                LanguageManager.text("mesh_out_of_limits")
            )
            self.analysisCard.setColor("#E74C3C")

        self.healthCard.setHealth(
            health.score,
            self.translate_health_label(health.label)
        )

        self.rangeCard.setValue(f"{mesh.total_range:.4f} mm")
        self.rangeCard.setFooter(
            f"{self.status_text(tolerance_result['range_status'])} / "
            f"{LanguageManager.text('limit')}: "
            f"{tolerance_result['max_total_range']:.2f} mm"
        )

        self.rmsCard.setValue(f"{mesh.rms:.4f} mm")
        self.rmsCard.setFooter(
            f"{self.status_text(tolerance_result['rms_status'])} / "
            f"{LanguageManager.text('limit')}: "
            f"{tolerance_result['max_rms']:.2f} mm"
        )

        self.planeCard.setValue(f"{geometry.max_deviation:.4f} mm")
        self.planeCard.setFooter(
            f"{self.status_text(tolerance_result['plane_status'])} / "
            f"{LanguageManager.text('limit')}: "
            f"{tolerance_result['max_plane_deviation']:.2f} mm"
        )

        self.sizeCard.setValue(f"{mesh.rows} × {mesh.cols}")
        self.sizeCard.setFooter(
            LanguageManager.text("rows_columns")
        )

        self.minCard.setValue(f"{mesh.minimum:.4f} mm")
        self.minCard.setFooter(
            LanguageManager.text("lowest_measurement")
        )

        self.maxCard.setValue(f"{mesh.maximum:.4f} mm")
        self.maxCard.setFooter(
            LanguageManager.text("highest_measurement")
        )

        self.avgCard.setValue(f"{mesh.average:.4f} mm")
        self.avgCard.setFooter(
            LanguageManager.text("average_height")
        )

        self.fileCard.setValue(mesh.name)
        self.fileCard.setFooter(
            f"{LanguageManager.text('last_opened_mesh')} | "
            f"{LanguageManager.text('analysis_time')}: "
            f"{analysis.elapsed_ms:.1f} ms"
        )

    def retranslate(self):
        self.titleLabel.clear()
        self.disclaimerLabel.setText(
            LanguageManager.text("dashboard_disclaimer")
        )

        self.healthCard.setTitle(
            "🩺 " + LanguageManager.text("machine_health")
        )

        self.statusCard.setTitle(
            "✅ " + LanguageManager.text("quality_status")
        )

        self.rangeCard.setTitle(
            "📏 " + LanguageManager.text("total_deviation")
        )

        self.rmsCard.setTitle("📐 RMS")

        self.planeCard.setTitle(
            "📊 " + LanguageManager.text("plane_deviation")
        )

        self.sizeCard.setTitle(
            "📂 " + LanguageManager.text("mesh_size")
        )

        self.minCard.setTitle(
            "⬇ " + LanguageManager.text("minimum")
        )

        self.maxCard.setTitle(
            "⬆ " + LanguageManager.text("maximum")
        )

        self.avgCard.setTitle(
            "➗ " + LanguageManager.text("average")
        )

        self.fileCard.setTitle(
            "📄 " + LanguageManager.text("file")
        )

        self.analysisCard.setTitle(
            "🧠 " + LanguageManager.text("analysis")
        )

        self.healthCard.setTooltip(ToolTips.machine_health())
        self.statusCard.setTooltip(ToolTips.quality_status())
        self.rangeCard.setTooltip(ToolTips.total_range())
        self.rmsCard.setTooltip(ToolTips.rms())
        self.planeCard.setTooltip(ToolTips.plane_deviation())
        self.sizeCard.setTooltip(ToolTips.mesh_size())
        self.minCard.setTooltip(ToolTips.minimum())
        self.maxCard.setTooltip(ToolTips.maximum())
        self.avgCard.setTooltip(ToolTips.average())
        self.fileCard.setTooltip(ToolTips.file_info())
        self.analysisCard.setTooltip(ToolTips.analysis_result())

        if self.current_mesh is None:
            waiting = LanguageManager.text("waiting_mesh")

            self.healthCard.setHealth(0, waiting)

            self.statusCard.setValue("--")
            self.statusCard.setFooter(waiting)
            self.statusCard.setColor("#95A5A6")

            self.rangeCard.setValue("--")
            self.rangeCard.setFooter(waiting)

            self.rmsCard.setValue("--")
            self.rmsCard.setFooter(waiting)

            self.planeCard.setValue("--")
            self.planeCard.setFooter(waiting)

            self.sizeCard.setValue("--")
            self.sizeCard.setFooter(
                LanguageManager.text("rows_columns")
            )

            self.minCard.setValue("--")
            self.minCard.setFooter(
                LanguageManager.text("lowest_point")
            )

            self.maxCard.setValue("--")
            self.maxCard.setFooter(
                LanguageManager.text("highest_point")
            )

            self.avgCard.setValue("--")
            self.avgCard.setFooter(
                LanguageManager.text("mesh_average")
            )

            self.fileCard.setValue("--")
            self.fileCard.setFooter(
                LanguageManager.text("no_file")
            )

            self.analysisCard.setValue("--")
            self.analysisCard.setFooter(
                LanguageManager.text("waiting_result")
            )

        else:
            self.update_mesh(self.current_mesh)

    def translate_health_label(self, label):
        mapping = {
            "Kritik": LanguageManager.text("critical"),
            "Kabul Edilebilir": LanguageManager.text("acceptable"),
            "İyi": LanguageManager.text("good"),
            "Mükemmel": LanguageManager.text("excellent"),
            "Çok İyi": LanguageManager.text("excellent"),
            "Kontrol Edilmeli": LanguageManager.text("needs_attention"),
        }

        return mapping.get(label, label)
