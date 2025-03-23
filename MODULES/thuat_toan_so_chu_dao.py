from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QMessageBox
import sys

class NumerologyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui_numerology.ui", self)  # Load giao diện từ file .ui

        # Lấy các thành phần từ UI (đặt đúng tên trong Figma)
        self.input_day = self.findChild(QWidget, "inputDay")
        self.input_month = self.findChild(QWidget, "inputMonth")
        self.input_year = self.findChild(QWidget, "inputYear")
        self.btn_calculate = self.findChild(QWidget, "btnCalculate")
        self.label_result = self.findChild(QWidget, "labelResult")

        # Kết nối nút bấm với hàm tính toán
        self.btn_calculate.clicked.connect(self.calculate_life_path)

    def calculate_life_path(self):
        """Xử lý khi nhấn 'Tính Toán'"""
        try:
            # Lấy dữ liệu từ UI
            day = int(self.input_day.text())
            month = int(self.input_month.text())
            year = int(self.input_year.text())

            # Kiểm tra ngày hợp lệ
            if not (1 <= day <= 31 and 1 <= month <= 12 and 1000 <= year <= 9999):
                raise ValueError("Ngày tháng năm không hợp lệ!")

            # Tính con số chủ đạo
            life_path_number = self.get_life_path_number(day, month, year)

            # Hiển thị kết quả trên giao diện
            self.label_result.setText(f"Con số chủ đạo của bạn là: {life_path_number}")

        except ValueError:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập ngày sinh hợp lệ!")

    def get_life_path_number(self, day: int, month: int, year: int) -> int:
        """Hàm tính con số chủ đạo"""
        def sum_digits(n: int) -> int:
            return sum(int(digit) for digit in str(n))

        total = sum_digits(day) + sum_digits(month) + sum_digits(year)
        life_path = sum_digits(total)

        return life_path if life_path in {11, 22} or life_path < 10 else sum_digits(life_path)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NumerologyApp()
    window.show()
    sys.exit(app.exec())
