from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QMessageBox
from user_signup import Ui_MainWindow as UserSignupUI

class SignupWindow(QMainWindow):
    def __init__(self, login_window):
        super().__init__()
        self.ui = UserSignupUI()
        self.ui.setupUi(self)
        self.login_window = login_window
        self.setWindowTitle("Signup To Seedly")
        self.setWindowIcon(QIcon("icon.ico"))
        self.ui.signupButton.clicked.connect(self.signup_user)

    def signup_user(self):
        first_name = self.ui.firstNameLineEdit.text()
        last_name = self.ui.lastNameLineEdit.text()
        user_name = self.ui.userNameLineEdit.text()
        password = self.ui.passwordLineEdit.text()
        dob = self.ui.dobDateEdit.date().toString("yyyy-MM-dd")
        objective = self.ui.objectiveTextEdit.toPlainText()

        # Add your validation and DB logic here
        # e.g., insert into users table

        # For now just show a success message
        QMessageBox.information(self, "Success", "User created successfully!")
        self.login_window.show()
        self.close()

    def closeEvent(self, event):
        self.login_window.show()
        event.accept()