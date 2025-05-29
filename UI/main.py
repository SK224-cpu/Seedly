import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from login_ui import Ui_MainWindow as LoginUI
from second_ui import Ui_MainWindow as SecondUI
from Logic.User import *
from configparser import ConfigParser
import psycopg2

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
            # Load DB config
            config = ConfigParser()
            config.read("config/config.ini")
            host_var = config['DB']['host']
            database_var = config['DB']['database']
            user_var = config['DB']['user']
            password_var = config['DB']['password']
            self.conn = psycopg2.connect(host=host_var, database=database_var, user=user_var, password=password_var)

        def login(self):
            username = self.ui.usernameLineEdit.text()
            password = self.ui.passwordLineEdit.text()

            checkLogin = login(username, password, self.conn)
            if checkLogin:
                self.second_window = SecondWindow(username)
                self.second_window.show()
            else:
                self.second_window = SecondWindow(username)
                self.second_window.show()
                QMessageBox.warning(self, "Warning", "Invalid username or password")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())

