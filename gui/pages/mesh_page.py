"""
MeshAnalyzer Pro
Mesh Page
Professional Table View
Shared Widgets + LanguageManager + Mini Heatmap
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView,
    QAbstractItemView,
    QLabel,
    QFrame,
    QStackedWidget,
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QColor

from languages import LanguageManager
from core.config import Config
from gui.tooltips import ToolTips
from gui.widgets.summary_card import SummaryCard
from gui.widgets.info_icon import InfoIcon


class MeshPage(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName("MeshPage")

        self.current_mesh = None
        self.selected_row = None
        self.selected_col = None

        main_layout = QVBoxLayout(self)

        content_layout = QHBoxLayout()
        content_layout.setSpacing(16)

        self.table = QTableWidget()
        self.table.setObjectName("MeshTable")
        self.table.setAlternatingRowColors(False)
        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectItems
        )
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )

        font = QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.table.setFont(font)

        header_font = QFont()
        header_font.setPointSize(11)
        header_font.setBold(True)

        self.table.horizontalHeader().setFont(header_font)
        self.table.verticalHeader().setFont(header_font)

        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch
        )

        self.table.verticalHeader().setDefaultSectionSize(52)
        self.table.horizontalHeader().setDefaultSectionSize(120)

        self.meshStack = QStackedWidget()
        self.meshStack.setObjectName("MeshStack")

        self.emptyStateLabel = QLabel()
        self.emptyStateLabel.setObjectName("EmptyStateLabel")
        self.emptyStateLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.emptyStateLabel.setWordWrap(True)
        self.emptyStateLabel.setTextFormat(Qt.TextFormat.RichText)

        self.meshStack.addWidget(self.emptyStateLabel)
        self.meshStack.addWidget(self.table)
        self.meshStack.setCurrentWidget(self.emptyStateLabel)

        content_layout.addWidget(self.meshStack, stretch=4)

        self.summaryCard = SummaryCard(
            icon="📊",
            tooltip=ToolTips.mesh_summary()
        )

        self.summaryCard.setMinimumWidth(280)
        self.summaryCard.setMaximumWidth(340)

        self.summaryCard.addRow("size")
        self.add_metrics_separator()
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

        self.coordinateStandardLabel = QLabel()
        self.coordinateStandardLabel.setObjectName("CoordinateStandardInfo")
        self.coordinateStandardLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coordinateStandardLabel.setWordWrap(True)
        self.coordinateStandardLabel.setTextFormat(Qt.TextFormat.RichText)
        self.coordinateStandardLabel.setMinimumHeight(38)
        main_layout.addWidget(self.coordinateStandardLabel)

        self.infoLabel = QLabel()
        self.infoLabel.setObjectName("SectionTitle")
        self.infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.infoLabel.setMinimumHeight(42)

        main_layout.addWidget(self.infoLabel)

        self.table.cellClicked.connect(self.show_cell_info)

        self.retranslate()

    def show_empty_state(self):
        self.meshStack.setCurrentWidget(self.emptyStateLabel)
        self.emptyStateLabel.setText(
            "<div style='font-size:18pt; font-weight:700;'>"
            + LanguageManager.text("empty_conf_waiting_title")
            + "</div>"
            + "<div style='height:26px;'>&nbsp;</div>"
            + "<div style='font-size:11pt; font-weight:400; color:#94A3B8;'>"
            + LanguageManager.text("empty_conf_waiting_message")
            + "</div>"
        )

        self.coordinateStandardLabel.hide()
        self.infoLabel.clear()
        self.infoLabel.hide()

    def coordinate_mm(self, index):
        return 5 + (index - 1) * 60

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

    def heat_color(self, value, min_value, max_value):
        if max_value == min_value:
            return QColor("#334155")

        ratio = (value - min_value) / (max_value - min_value)

        if ratio < 0.5:
            t = ratio / 0.5
            r = int(30 + t * (34 - 30))
            g = int(64 + t * (197 - 64))
            b = int(175 + t * (94 - 175))
            return QColor(r, g, b)

        t = (ratio - 0.5) / 0.5
        r = int(34 + t * (220 - 34))
        g = int(197 + t * (38 - 197))
        b = int(94 + t * (38 - 94))
        return QColor(r, g, b)

    def text_color_for_background(self, color):
        brightness = (
            color.red() * 0.299 +
            color.green() * 0.587 +
            color.blue() * 0.114
        )

        if brightness > 145:
            return QColor("#0F172A")

        return QColor("#FFFFFF")

    def point_status(self, value, min_value, max_value):
        if value == min_value:
            return LanguageManager.text("minimum_point")

        if value == max_value:
            return LanguageManager.text("maximum_point")

        return LanguageManager.text("normal_point")

    def update_mesh(self, mesh):
        self.coordinateStandardLabel.show()
        self.coordinateStandardLabel.setText(
            LanguageManager.text("coordinate_standard_info")
        )
        self.infoLabel.show()
        self.current_mesh = mesh
        self.selected_row = None
        self.selected_col = None

        self.meshStack.setCurrentWidget(self.table)

        rows = mesh.rows
        cols = mesh.cols

        min_value = mesh.minimum
        max_value = mesh.maximum

        self.table.clear()
        self.table.setRowCount(rows)
        self.table.setColumnCount(cols)

        self.table.setHorizontalHeaderLabels(
            [
                f"X{i + 1} - {self.coordinate_mm(i + 1)} mm"
                for i in range(cols)
            ]
        )

        self.table.setVerticalHeaderLabels(
            [
                f"Y{rows - i} - {self.coordinate_mm(rows - i)} mm"
                for i in range(rows)
            ]
        )

        show_table_values = bool(
            Config().get("appearance_show_table_values")
        )

        for r in range(rows):
            for c in range(cols):
                source_row = rows - 1 - r
                value = mesh.values[source_row][c]
                marker = ""
                if value == max_value:
                    marker = "  ↑"
                elif value == min_value:
                    marker = "  ↓"

                display_text = f"{value:.4f}{marker}" if show_table_values else ""
                item = QTableWidgetItem(display_text)
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)

                bg = self.heat_color(value, min_value, max_value)
                fg = self.text_color_for_background(bg)

                item.setBackground(bg)
                item.setForeground(fg)
                item.setToolTip(
                    self.point_status(value, min_value, max_value)
                )

                self.table.setItem(r, c, item)

        for r in range(rows):
            self.table.setRowHeight(r, 52)

        self.summaryCard.setValue(
            "size",
            f"{mesh.rows} × {mesh.cols}"
        )
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

        self.infoLabel.setText(
            LanguageManager.text("selected_point_none")
        )

    def show_cell_info(self, row, col):
        if self.current_mesh is None:
            return

        self.selected_row = row
        self.selected_col = col

        min_value = self.current_mesh.minimum
        max_value = self.current_mesh.maximum

        value = self.current_mesh.values[row][col]

        x_index = col + 1
        y_index = self.current_mesh.rows - row

        x_mm = self.coordinate_mm(x_index)
        y_mm = self.coordinate_mm(y_index)

        status = self.point_status(
            value,
            min_value,
            max_value
        )

        self.infoLabel.setText(
            f"{LanguageManager.text('selected_point')}: "
            f"X{x_index} = {x_mm} mm / "
            f"Y{y_index} = {y_mm} mm | "
            f"Z = {value:.4f} mm | "
            f"{LanguageManager.text('point_status')}: {status}"
        )

    def retranslate(self):
        self.summaryCard.setTitle(
            LanguageManager.text("mesh_summary")
        )

        self.summaryCard.setTooltip(
            ToolTips.mesh_summary()
        )

        self.summaryCard.setLabel(
            "size",
            LanguageManager.text("mesh_size")
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
        self.summaryCard.setLabel("rms", "RMS")
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

        if self.current_mesh is None:
            self.show_empty_state()

        else:
            self.coordinateStandardLabel.setText(
                LanguageManager.text("coordinate_standard_info")
            )

        if self.current_mesh is not None and self.selected_row is not None and self.selected_col is not None:
            self.show_cell_info(
                self.selected_row,
                self.selected_col
            )
