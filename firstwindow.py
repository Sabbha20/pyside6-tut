import sys
from PySide6.QtWidgets import QWidget, QApplication


class MWidget(QWidget):
    def __init__(self):
        super().__init__()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mwidget = MWidget()

    mwidget.show()
    sys.exit(app.exec())
