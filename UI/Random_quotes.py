import json
import random
from datetime import datetime


def tong_chu_so(n: int) -> int:
    """Hàm tính tổng các chữ số của một số."""
    return sum(int(chu_so) for chu_so in str(n))


def tinh_so_chu_dao(ngay: int, thang: int, nam: int) -> int:
    """Hàm tính con số chủ đạo từ ngày, tháng, năm sinh."""
    tong = tong_chu_so(ngay) + tong_chu_so(thang) + tong_chu_so(nam)

    while tong >= 10 and tong not in {11, 22}:  # Giữ nguyên số 11 và 22, chỉ tiếp tục cộng nếu khác
        tong = tong_chu_so(tong)

    return tong


def lay_cau_quote(so_chu_dao: int) -> str:
    """Lấy câu quote phù hợp với số chủ đạo."""
    try:
        with open("Cac_cau_quotes.json", "r", encoding="utf-8") as file:
            quotes = json.load(file)

        # Lấy danh sách quote cho số chủ đạo
        danh_sach_quote = quotes.get(str(so_chu_dao), ["Không tìm thấy câu quote phù hợp."])

        # Dùng seed để đảm bảo mỗi ngày có quote mới
        random.seed(datetime.now().strftime("%Y-%m-%d"))
        return random.choice(danh_sach_quote)
    except FileNotFoundError:
        return "Không tìm thấy file quotes.json."
    except json.JSONDecodeError:
        return "Lỗi đọc dữ liệu từ file quotes.json."

def get_quote_from_ui(ngay: str, thang: str, nam: str) -> str:
    """Lấy số chủ đạo và câu quote từ ngày sinh nhập trên giao diện."""
    try:
        # Chuyển đổi sang số nguyên
        ngay, thang, nam = int(ngay), int(thang), int(nam)

        # Kiểm tra tính hợp lệ
        nam_hien_tai = datetime.now().year
        if not (1 <= ngay <= 31 and 1 <= thang <= 12 and 1000 <= nam <= nam_hien_tai):
            return "Ngày tháng năm không hợp lệ!"

        # Tính số chủ đạo
        so_chu_dao = tinh_so_chu_dao(ngay, thang, nam)

        # Lấy câu quote
        return lay_cau_quote(so_chu_dao)
    except ValueError:
        return "Vui lòng nhập số hợp lệ!"