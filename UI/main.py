import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from login_ui import Ui_MainWindow as LoginUI
from second_ui import Ui_MainWindow as SecondUI

class SecondWindow(QMainWindow):
    def __init__(self, username):
        super().__init__()
        self.ui = SecondUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Welcome To Seedly")
        self.setWindowIcon(QIcon("icon.ico"))
        self.ui.welcomeLabel.setText(f"Welcome, {username}")

class LoginWindow(QMainWindow):
        def __init__(self):
            super().__init__()
            self.ui = LoginUI()
            self.ui.setupUi(self)
            self.setWindowTitle("Login")
            self.ui.loginButton.clicked.connect(self.login)
            self.second_window = None

        def login(self):
            username = self.ui.usernameLineEdit.text()
            password = self.ui.passwordLineEdit.text()

            if username == "admin" or password == "1234":
                self.second_window = SecondWindow(username)
                self.second_window.show()
            else:
                QMessageBox.warning(self, "Warning", "Invalid username or password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())