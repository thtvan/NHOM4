from PyQt6 import QtWidgets
from NHOM4.UI.App_UI import Ui_MainWindow

import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Đặt kích thước cửa sổ nhỏ hơn
        self.setFixedSize(906, 750)  # Kích thước cố định

        # Kết nối các nút với chức năng tương ứng
        self.ui.pushButton.clicked.connect(self.switch_to_askTK)  # Từ Logo -> AskTK
        self.ui.btnYes.clicked.connect(self.switch_to_signup)     # Từ AskTK -> SignUp
        self.ui.btnNo.clicked.connect(self.switch_to_login)       # Từ AskTK -> LogIn
        self.ui.btnLogIn.clicked.connect(self.switch_to_main)     # Từ LogIn -> Main
        self.ui.btnSignup.clicked.connect(self.switch_to_login)   # Từ SignUp -> LogIn

    def switch_to_askTK(self):
        """Chuyển từ logo sang màn hình askTK"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.askTK)

    def switch_to_signup(self):
        """Chuyển từ askTK sang màn hình SignUp"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.SignUp)

    def switch_to_login(self):
        """Chuyển từ askTK hoặc SignUp sang màn hình LogIn"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.LogIn)

    def switch_to_main(self):
        """Chuyển từ LogIn sang màn hình Main"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
