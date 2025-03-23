import sys
from PyQt6 import QtWidgets
from App_UI import Ui_MainWindow

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # nối chức năng
        self.ui.pushButton.clicked.connect(self.switch_choose)
        self.ui.btnLogIn.clicked.connect(self.switch_main)
        self.ui.btnYes.clicked.connect(self.switch_signup)
        self.ui.btnNo.clicked.connect(self.switch_login)

    def switch_choose(self):
        #hỏi có tài khoản
        self.ui.stackedWidget.setCurrentWidget(self.ui.askTK)
    def switch_login(self):
        #đăng nhập
        self.ui.stackedWidget.setCurrentWidget(self.ui.LogIn)

    def switch_main(self):
        #vào màn chính
        self.ui.stackedWidget.setCurrentWidget(self.ui.Main)

    def switch_signup(self):
        #đăng kí
        self.ui.stackedWidget.setCurrentWidget(self.ui.SignUp)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
