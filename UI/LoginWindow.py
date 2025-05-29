from Logic.User import *
# from login_ui import Ui_MainWindow as LoginUI
from configparser import ConfigParser
import psycopg2
from SecondWindow import *
from SignupWindow import *

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.signup_window = None
        # self.ui = LoginUI()
        self.ui.setupUi(self)
        self.setWindowTitle("Login To Seedly")
        self.ui.loginButton.clicked.connect(self.login)
        self.ui.signupButton.clicked.connect(self.open_signup)

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
            QMessageBox.warning(self, "Warning", "Invalid username or password")

    def open_signup(self):
        self.signup_window = SignupWindow(self)
        self.signup_window.show()
        self.hide()