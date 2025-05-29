from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow
from second_ui import Ui_MainWindow as SecondUI

class SecondWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.ui = SecondUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Welcome To Seedly")
        self.setWindowIcon(QIcon("icon.ico"))
        self.ui.welcomeLabel.setText(f"Welcome, {username}")