from PyQt6 import QtWidgets
from NHOM4.UI.App_UI import Ui_MainWindow

import sys

class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Đặt kích thước cửa sổ cố định
        self.setFixedSize(906, 750)

        # Kết nối các nút chuyển các màn
        self.ui.pushButton.clicked.connect(self.switch_to_askTK)  # Từ Logo -> AskTK
        self.ui.btnYes.clicked.connect(self.switch_to_signup)     # Từ AskTK -> SignUp
        self.ui.btnNo.clicked.connect(self.switch_to_login)       # Từ AskTK -> LogIn

        self.ui.btnSignup.clicked.connect(self.switch_to_gthieu1)   # Từ SignUp -> Gthieu1
        self.ui.btnNext.clicked.connect(self.switch_to_gthieu2)   # Từ Gthieu1 -> Gthieu2
        self.ui.btnNext_2.clicked.connect(self.switch_to_gthieu3)   # Từ Gthieu2 -> Gthieu3
        self.ui.btnNext_11.clicked.connect(self.switch_to_birthday)   # Từ Gthieu3 -> birthday


        self.ui.btnChooseToDoList.clicked.connect(self.switch_to_list1)

        self.ui.btnPre_2.clicked.connect(self.switch_to_list1)
        self.ui.btnPre_3.clicked.connect(self.switch_to_list2)
        self.ui.btnPre.clicked.connect(self.switch_to_list3)

        self.ui.btnAdd.clicked.connect(self.switch_to_list2)
        self.ui.btnAdd_2.clicked.connect(self.switch_to_list3)
        self.ui.btnAdd_3.clicked.connect(self.switch_to_list4)

        #các nút để chuyển về main
        main_buttons = [self.btnLogIn, self.btnDone, self.btnNext_8, self.btnPre, self.btnPre_4, self.btnPre_5, self.btnPre_5, self.btnPre_6, self.btnPre_7, self.btnPre_8, self.btnPre_9, self.btnPre_10]
        # Kết nối các button trong danh sách với cùng một hành động
        for btn in main_buttons:
            btn.clicked.connect(self.stackedWidget.switch_to_main)

        # các nút để chuyển về diary
        main_buttons = [self.btnChooseDiary, self.btnNext_4, self.btnNext_5, self.btnNext_6, self.btnNext_7, self.btnNext_8, self.btnNext_9, self.btnNext_10]
        for btn in main_buttons:
            btn.clicked.connect(self.stackedWidget.switch_to_diary)

        # Lấy danh sách tất cả các nút có tên bắt đầu bằng "btnOkay"
        self.okay_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnOkay")]
        # Kết nối tất cả các nút với một hàm xử lý chung
        for btn in self.okay_btn:
            btn.clicked.connect(self.switch_to_EmoOkay)


        self.happy_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnHappy")]
        for btn in self.happy_btn:
            btn.clicked.connect(self.switch_to_EmoHappy)


        self.ui.btnExcited.clicked.connect(self.switch_to_EmoExcited)
        self.excited_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnExcited")]
        for btn in self.excited_btn:
            btn.clicked.connect(self.switch_to_EmoExcited)


        self.love_btn= [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnLove")]
        for btn in self.love_btn:
            btn.clicked.connect(self.switch_to_EmoLove)


        self.angry_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnAngry")]
        for btn in self.angry_btn:
            btn.clicked.connect(self.switch_to_EmoAngry)


        self.sad_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnSad")]
        for btn in self.sad_btn:
            btn.clicked.connect(self.switch_to_EmoSad)


        self.depresseed_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnDepressed")]
        for btn in self.depresseed_btn:
            btn.clicked.connect(self.switch_to_EmoDepressed)



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

    def switch_to_gthieu1(self):
        #Chuyển từ màn sign up qua màn giới thiệu
        self.ui.stackedWidget.setCurrentWidget(self.ui.GThieu1)

    def switch_to_gthieu2(self):
        #Chuyển từ màn sign up qua màn giới thiệu
        self.ui.stackedWidget.setCurrentWidget(self.ui.GThieu2)

    def switch_to_gthieu3(self):
        #Chuyển từ màn sign up qua màn giới thiệu
        self.ui.stackedWidget.setCurrentWidget(self.ui.GThieu3)

    def switch_to_birthday(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Birthday)

    def switch_to_list1(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ToDoList)

    def switch_to_list2(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ToDoList_2)

    def switch_to_list3(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ToDoList_3)

    def switch_to_list4(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.ToDoList_4)

    def switch_to_EmoOkay(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoOkay)

    def switch_to_EmoHappy(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoHappy)

    def switch_to_EmoExcited(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoExcited)

    def switch_to_EmoSad(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoSad)

    def switch_to_EmoAngry(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoAngry)

    def switch_to_EmoDepressed(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoDepressed)

    def switch_to_EmoLove(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.EmoLove)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())
