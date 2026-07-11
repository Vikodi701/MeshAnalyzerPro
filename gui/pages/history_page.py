"""
MeshAnalyzer Pro
History Page
"""

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
    QInputDialog,
    QHeaderView,
    QAbstractItemView,
)

from PySide6.QtCore import Qt, Signal

from database.database import Database
from core.compare import MeshCompare
from languages import LanguageManager
from gui.widgets.section_title import SectionTitle


class HistoryTableItem(QTableWidgetItem):

    def __lt__(self, other):
        """
        QTableWidget sorting karşılaştırması.

        Not:
        super().__lt__(other) bazı durumlarda Python override zincirine
        tekrar girip RecursionError oluşturabiliyor. Bu yüzden karşılaştırmayı
        tamamen burada yapıyoruz.
        """
        left = self.data(Qt.ItemDataRole.UserRole)
        right = other.data(Qt.ItemDataRole.UserRole)

        if left is None:
            left = self.text()

        if right is None:
            right = other.text()

        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            return left < right

        return str(left).lower() < str(right).lower()


class HistoryPage(QWidget):

    meshSelected = Signal(object)

    def __init__(self):
        super().__init__()

        self.db = Database()
        self.rows = []

        layout = QVBoxLayout(self)
        layout.setSpacing(14)

        self.title = SectionTitle()
        layout.addWidget(self.title)

        self.info_label = QLabel()
        self.info_label.setObjectName("SectionTitle")
        self.info_label.setWordWrap(True)
        self.info_label.setMinimumHeight(44)
        layout.addWidget(self.info_label)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        self.btn_refresh = QPushButton()
        self.btn_open = QPushButton()
        self.btn_favorite = QPushButton()
        self.btn_label = QPushButton()
        self.btn_note = QPushButton()
        self.btn_compare_previous = QPushButton()
        self.btn_delete = QPushButton()
        self.btn_clear = QPushButton()

        for button in (
            self.btn_refresh,
            self.btn_open,
            self.btn_favorite,
            self.btn_label,
            self.btn_note,
            self.btn_compare_previous,
            self.btn_delete,
            self.btn_clear,
        ):
            button.setMinimumHeight(38)
            button_layout.addWidget(button)

        button_layout.addStretch()
        layout.addLayout(button_layout)

        self.table = QTableWidget()
        self.table.setAlternatingRowColors(False)
        self.table.setEditTriggers(
            QAbstractItemView.EditTrigger.NoEditTriggers
        )
        self.table.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table.setSelectionMode(
            QAbstractItemView.SelectionMode.SingleSelection
        )
        self.table.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.table.setSortingEnabled(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents
        )

        layout.addWidget(self.table)

        self.status_label = QLabel()
        self.status_label.setObjectName("SectionTitle")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setMinimumHeight(34)
        layout.addWidget(self.status_label)

        self.btn_refresh.clicked.connect(self.load_history)
        self.btn_open.clicked.connect(self.open_selected_mesh)
        self.btn_favorite.clicked.connect(self.toggle_selected_favorite)
        self.btn_label.clicked.connect(self.edit_selected_label)
        self.btn_note.clicked.connect(self.edit_selected_note)
        self.btn_compare_previous.clicked.connect(self.compare_with_previous)
        self.btn_delete.clicked.connect(self.delete_selected_mesh)
        self.btn_clear.clicked.connect(self.clear_history)
        self.table.cellDoubleClicked.connect(self.open_selected_mesh)
        self.table.itemSelectionChanged.connect(self.update_button_state)

        self.retranslate()

    def selected_mesh_id(self):
        selected = self.table.selectedItems()

        if not selected:
            return None

        row = selected[0].row()
        id_item = self.table.item(row, 0)

        if id_item is None:
            return None

        return int(id_item.text())

    def load_history(self):
        self.rows = self.db.get_history()

        headers = [
            LanguageManager.text("history_id"),
            LanguageManager.text("history_date"),
            LanguageManager.text("history_file"),
            LanguageManager.text("history_rows"),
            LanguageManager.text("history_cols"),
            LanguageManager.text("minimum"),
            LanguageManager.text("maximum"),
            LanguageManager.text("total_deviation"),
            "RMS",
            LanguageManager.text("history_favorite"),
            LanguageManager.text("history_label"),
            LanguageManager.text("history_note"),
        ]

        self.table.setSortingEnabled(False)
        self.table.clear()
        self.table.setRowCount(len(self.rows))
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(headers)

        for row_index, row in enumerate(self.rows):
            for column_index, value in enumerate(row):
                item = HistoryTableItem(self.format_value(column_index, value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                item.setData(Qt.ItemDataRole.UserRole, value)
                self.table.setItem(row_index, column_index, item)

        self.table.resizeColumnsToContents()
        self.table.setSortingEnabled(True)
        self.update_button_state()

    def format_value(self, column_index, value):
        if column_index in (5, 6, 7, 8):
            return f"{float(value):.4f}"

        if column_index == 9:
            return "★" if bool(value) else ""

        return str(value or "")

    def open_selected_mesh(self, row=None, column=None):
        mesh_id = None

        if isinstance(row, int):
            id_item = self.table.item(row, 0)
            if id_item is not None:
                mesh_id = int(id_item.text())

        if mesh_id is None:
            mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return

        mesh = self.db.load_mesh_by_id(mesh_id)

        if mesh is None:
            QMessageBox.warning(
                self,
                LanguageManager.text("history_load_failed_title"),
                LanguageManager.text("history_load_failed_message")
            )
            return

        self.meshSelected.emit(mesh)

    def selected_row_metadata(self):
        mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return None

        return self.db.get_history_item_metadata(mesh_id)

    def toggle_selected_favorite(self):
        mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return

        metadata = self.db.get_history_item_metadata(mesh_id)
        self.db.update_history_metadata(
            mesh_id,
            favorite=not metadata["favorite"]
        )
        self.load_history()

    def edit_selected_label(self):
        mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return

        metadata = self.db.get_history_item_metadata(mesh_id)

        label, ok = QInputDialog.getText(
            self,
            LanguageManager.text("history_edit_label_title"),
            LanguageManager.text("history_edit_label_message"),
            text=metadata["label"]
        )

        if not ok:
            return

        self.db.update_history_metadata(
            mesh_id,
            label=label.strip()
        )
        self.load_history()

    def edit_selected_note(self):
        mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return

        metadata = self.db.get_history_item_metadata(mesh_id)

        note, ok = QInputDialog.getMultiLineText(
            self,
            LanguageManager.text("history_edit_note_title"),
            LanguageManager.text("history_edit_note_message"),
            metadata["note"]
        )

        if not ok:
            return

        self.db.update_history_metadata(
            mesh_id,
            note=note.strip()
        )
        self.load_history()

    def compare_with_previous(self):
        mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return

        current_mesh = self.db.load_mesh_by_id(mesh_id)

        if current_mesh is None:
            return

        previous_mesh = self.db.load_previous_mesh(current_mesh)

        if previous_mesh is None:
            QMessageBox.information(
                self,
                LanguageManager.text("history_compare_previous"),
                LanguageManager.text("history_no_previous_for_compare")
            )
            return

        try:
            comparison = MeshCompare(previous_mesh, current_mesh)
            summary = comparison.summary()
        except Exception as error:
            QMessageBox.warning(
                self,
                LanguageManager.text("history_compare_previous"),
                str(error)
            )
            return

        message = (
            f"{LanguageManager.text('compare_old_label')}: {previous_mesh.name}\n"
            f"{LanguageManager.text('compare_new_label')}: {current_mesh.name}\n\n"
            f"{LanguageManager.text('compare_old_total_deviation')}: "
            f"{summary['before_range']:.4f} mm\n"
            f"{LanguageManager.text('compare_new_total_deviation')}: "
            f"{summary['after_range']:.4f} mm\n"
            f"{LanguageManager.text('compare_total_range_change')}: "
            f"{summary['improvement']:+.1f}%\n"
            f"{LanguageManager.text('compare_rms_change')}: "
            f"{summary['rms_improvement']:+.1f}%\n"
            f"{LanguageManager.text('compare_most_improved_area')}: "
            f"{summary['best_location']} ({summary['best_value']:+.4f} mm)\n"
            f"{LanguageManager.text('compare_most_worsened_area')}: "
            f"{summary['worst_location']} ({summary['worst_value']:+.4f} mm)"
        )

        QMessageBox.information(
            self,
            LanguageManager.text("history_compare_previous"),
            message
        )

    def delete_selected_mesh(self):
        mesh_id = self.selected_mesh_id()

        if mesh_id is None:
            return

        reply = QMessageBox.question(
            self,
            LanguageManager.text("history_delete_title"),
            LanguageManager.text("history_delete_message"),
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        self.db.delete_history_item(mesh_id)
        self.load_history()

    def clear_history(self):
        if not self.rows:
            return

        reply = QMessageBox.question(
            self,
            LanguageManager.text("history_clear_title"),
            LanguageManager.text("history_clear_message"),
            QMessageBox.StandardButton.Yes |
            QMessageBox.StandardButton.No
        )

        if reply != QMessageBox.StandardButton.Yes:
            return

        self.db.clear_history()
        self.load_history()

    def update_button_state(self):
        has_rows = bool(self.rows)
        has_selection = self.selected_mesh_id() is not None

        self.btn_open.setEnabled(has_selection)
        self.btn_favorite.setEnabled(has_selection)
        self.btn_label.setEnabled(has_selection)
        self.btn_note.setEnabled(has_selection)
        self.btn_compare_previous.setEnabled(has_selection)
        self.btn_delete.setEnabled(has_selection)
        self.btn_clear.setEnabled(has_rows)

        count = len(self.rows)
        if count == 0:
            self.status_label.setText(LanguageManager.text("history_empty"))
        else:
            self.status_label.setText(
                LanguageManager.text("history_record_count").format(count=count)
            )

    def refresh_language(self):
        self.retranslate()

    def refresh_theme(self):
        self.table.viewport().update()

    def refresh_page(self):
        self.refresh_language()
        self.refresh_theme()

    def retranslate(self):
        self.title.setTitle(LanguageManager.text("history_title"))
        self.title.setTooltip(LanguageManager.text("history_tooltip"))

        self.info_label.setText(LanguageManager.text("history_info"))

        self.btn_refresh.setText(LanguageManager.text("history_refresh"))
        self.btn_open.setText(LanguageManager.text("history_open_selected"))
        self.btn_favorite.setText(LanguageManager.text("history_toggle_favorite"))
        self.btn_label.setText(LanguageManager.text("history_edit_label_button"))
        self.btn_note.setText(LanguageManager.text("history_edit_note_button"))
        self.btn_compare_previous.setText(LanguageManager.text("history_compare_previous"))
        self.btn_delete.setText(LanguageManager.text("history_delete_selected"))
        self.btn_clear.setText(LanguageManager.text("history_clear"))

        self.load_history()
