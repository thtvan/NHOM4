from PyQt6 import QtWidgets
from App_UI import Ui_MainWindow
from Random_quotes import get_quote_from_ui
import sys
from UI.auth import save_user_to_json, save_user_to_mongodb, check_login_json, check_login_mongodb
from auth import check_login_json, check_login_mongodb, load_users_from_json
class MainApp(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Đặt kích thước cửa sổ cố định
        self.setFixedSize(906, 750)

        # Kết nối các nút chuyển các màn
        self.ui.pushButton.clicked.connect(self.switch_to_askTK)  # Từ Logo -> AskTK
        self.ui.btnYes.clicked.connect(self.switch_to_login)     # Từ AskTK -> SignUp
        self.ui.btnNo.clicked.connect(self.switch_to_signup)       # Từ AskTK -> LogIn

        self.ui.btnSignup.clicked.connect(self.switch_to_gthieu1)   # Từ SignUp -> Gthieu1
        self.ui.btnNext.clicked.connect(self.switch_to_gthieu2)   # Từ Gthieu1 -> Gthieu2
        self.ui.btnNext_2.clicked.connect(self.switch_to_gthieu3)   # Từ Gthieu2 -> Gthieu3
        self.ui.btnNext_11.clicked.connect(self.switch_to_birthday)   # Từ Gthieu3 -> birthday

        self.ui.btnQuay.clicked.connect(self.switch_to_Logo)
        self.ui.btnQuay_2.clicked.connect(self.switch_to_askTK)
        self.ui.btnQuay_3.clicked.connect(self.switch_to_askTK)
        self.ui.btnQuay_4.clicked.connect(self.switch_to_signup)
        self.ui.btnQuay_5.clicked.connect(self.switch_to_gthieu1)
        self.ui.btnQuay_6.clicked.connect(self.switch_to_gthieu2)
        self.ui.btnQuay_7.clicked.connect(self.switch_to_gthieu3)


        self.ui.btnChooseDiary.clicked.connect(self.switch_to_EmoOkay)
        self.ui.btnChooseToDoList.clicked.connect(self.switch_to_list1)

        self.ui.btnPre_2.clicked.connect(self.switch_to_list1)
        self.ui.btnPre_3.clicked.connect(self.switch_to_list2)
        self.ui.btnPre.clicked.connect(self.switch_to_list3)

        self.ui.btnAdd.clicked.connect(self.switch_to_list2)
        self.ui.btnAdd_2.clicked.connect(self.switch_to_list3)
        self.ui.btnAdd_3.clicked.connect(self.switch_to_list4)

        # Kết nối sự kiện khi nhấn Enter trong các ô nhập
        self.ui.day.returnPressed.connect(lambda: self.ui.month.setFocus())
        self.ui.month.returnPressed.connect(lambda: self.ui.year.setFocus())
        self.ui.year.returnPressed.connect(self.hien_thi_quote)

        # Kết nối nút Done để hiển thị quote
        self.ui.btnDone.clicked.connect(self.hien_thi_quote)

        self.switch_to_Logo()

        self.ui.btnSignOut.clicked.connect(self.logout)

        # các nút để chuyển về main
        main_buttons = [self.ui.btnLogIn, self.ui.btnDone, self.ui.btnNext_8, self.ui.btnPre, self.ui.btnPre_4,
                        self.ui.btnPre_5, self.ui.btnPre_6, self.ui.btnPre_7, self.ui.btnPre_8, self.ui.btnPre_9,
                        self.ui.btnPre_10, self.ui.btn_Pre, self.ui.btnNext_12]
        for btn in main_buttons:
            btn.clicked.connect(self.switch_to_main)

        #các nút để chuyển về diary
        diary_buttons = [self.ui.btnNext_4, self.ui.btnNext_5, self.ui.btnNext_6,
                         self.ui.btnNext_7, self.ui.btnNext_8, self.ui.btnNext_9, self.ui.btnNext_10]
        for btn in diary_buttons:
            btn.clicked.connect(self.switch_to_Diary)

        # Lấy danh sách tất cả các nút có tên bắt đầu bằng "btnOkay"
        self.okay_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnOkay")]
        # Kết nối tất cả các nút với một hàm xử lý chung
        for btn in self.okay_btn:
            btn.clicked.connect(self.switch_to_EmoOkay)

        self.ui.btnSignup.clicked.connect(self.handle_signup)
        self.ui.btnLogIn.clicked.connect(self.handle_login)

        self.happy_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnHappy")]
        for btn in self.happy_btn:
            btn.clicked.connect(self.switch_to_EmoHappy)


        self.excited_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnExcited")]
        for btn in self.excited_btn:
            btn.clicked.connect(self.switch_to_EmoExcited)


        self.love_btn = [btn for btn in self.findChildren(QtWidgets.QPushButton) if btn.objectName().startswith("btnLove")]
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


    def switch_to_Logo(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.logo)

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

    def switch_to_Diary(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Diary)

    def handle_signup(self):
        username = self.ui.lineUserName.text().strip()
        password = self.ui.linePassword.text().strip()
        confirm = self.ui.lineConfirm.text().strip()
        ngay = self.ui.day.text().strip()
        thang = self.ui.month.text().strip()
        nam = self.ui.year.text().strip()

        # Kiểm tra nếu có bất kỳ ô nào trống
        if not all([username, password, confirm]):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đầy đủ thông tin.")
            return  # Thoát khỏi hàm, không tiếp tục đăng ký

        if password != confirm:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Mật khẩu không khớp.")
            return

        # Kiểm tra nếu tài khoản đã tồn tại
        if check_login_json(username, password):
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Tài khoản đã tồn tại. Chuyển về trang đăng nhập.")
            self.ui.stackedWidget.setCurrentWidget(self.ui.LogIn)
            return

        # Lưu tài khoản vào JSON và MongoDB
        save_user_to_json(username, password, ngay, thang, nam)
        save_user_to_mongodb(username, password, ngay, thang, nam)

        QtWidgets.QMessageBox.information(self, "Thành công", "Đăng ký thành công!")
        self.switch_to_gthieu1()

    def handle_login(self):
        username = self.ui.lineUserName_2.text().strip()
        password = self.ui.linePass.text().strip()

        users = load_users_from_json()

        if username in users and users[username]["password"] == password:
            QtWidgets.QMessageBox.information(self, "Thành công", "Đăng nhập thành công!")

            # Lấy ngày sinh từ JSON
            ngay = users[username].get("ngay", "")
            thang = users[username].get("thang", "")
            nam = users[username].get("nam", "")

            # Nếu đã có ngày sinh, hiển thị ngay câu quote
            if ngay and thang and nam:
                quote = get_quote_from_ui(ngay, thang, nam)
                self.ui.lineQuote.setText(quote)

            self.switch_to_main()  # Chỉ chuyển trang nếu đăng nhập đúng
        else:
            QtWidgets.QMessageBox.warning(self, "Lỗi", "Sai tài khoản hoặc mật khẩu. Vui lòng nhập lại!")
            self.ui.lineUserName_2.clear()
            self.ui.linePass.clear()
            self.ui.lineUserName_2.setFocus()
            self.ui.stackedWidget.setCurrentWidget(self.ui.LogIn)

    def hien_thi_quote(self):
        # Lấy dữ liệu từ giao diện
        ngay = self.ui.day.text().strip()
        thang = self.ui.month.text().strip()
        nam = self.ui.year.text().strip()

        # Gọi hàm xử lý từ `Random_quotes.py`
        quote = get_quote_from_ui(ngay, thang, nam)

        # Hiển thị câu quote lên `lineQuote`
        self.ui.lineQuote.setText(quote)

    def logout(self):
        """Hàm xử lý đăng xuất, quay lại trang đăng nhập"""
        self.ui.stackedWidget.setCurrentWidget(self.ui.LogIn)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec())