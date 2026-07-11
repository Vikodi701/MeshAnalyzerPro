from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PySide6.QtCore import Qt


class BasePage(QWidget):
    TITLE = "Page"

    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout(self)

        self.titleLabel = QLabel(self.TITLE)
        self.titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setStyleSheet("""
            font-size: 28px;
            font-weight: bold;
            padding: 30px;
        """)

        self.layout.addWidget(self.titleLabel)
        self.layout.addStretch()

    def refresh_language(self):
        """
        Dil değiştiğinde çağrılır.
        Sayfada retranslate() varsa onu çalıştırır.
        """
        if hasattr(self, "retranslate"):
            self.retranslate()

    def refresh_theme(self):
        """
        Tema değiştiğinde çağrılır.
        Grafik/canvas gibi özel çizim yapan sayfalar bunu override eder.
        """
        pass

    def refresh_page(self):
        """
        Hem dil hem tema yenilemesi gerekiyorsa kullanılır.
        """
        self.refresh_language()
        self.refresh_theme()