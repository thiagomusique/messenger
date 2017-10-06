import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QHBoxLayout, QVBoxLayout, QLineEdit, QLabel


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('Messenger')
        self.setStyleSheet('background-color: #1E1F29 ')
        self.resize(600, 400)

        # Layouts
        self.messange = QHBoxLayout()
        self.side_menu = QVBoxLayout()

        # Widgets
        self.search = QLineEdit()
        self.search.setStyleSheet('color: #fff')
        self.btn = QPushButton('ok')
        self.btn.setStyleSheet('background-color: #1E1F29')
        self.btn.clicked.connect(self.send)

        # Wrapping
        self.messange.addWidget(self.search)
        self.messange.addWidget(self.btn)
        self.side_menu.addLayout(self.messange)

        self.setLayout(self.side_menu)
        self.show()

    def send(self):
        text = self.search.text()
        new_text = QLabel()
        new_text.setText(text)
        new_text.setStyleSheet('color: #FF512F')
        if new_text.text() != '':
            self.side_menu.addWidget(new_text)
            self.search.clear()


app = QApplication(sys.argv)
win = MainWindow()
sys.exit(app.exec_())
