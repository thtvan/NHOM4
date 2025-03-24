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


# Nhập ngày sinh từ người dùng
try:
    nam_hien_tai = datetime.now().year
    ngay = int(input("Nhập ngày sinh (1-31): "))
    thang = int(input("Nhập tháng sinh (1-12): "))
    nam = int(input(f"Nhập năm sinh (1000-{nam_hien_tai}): "))

    if not (1 <= ngay <= 31 and 1 <= thang <= 12 and 1000 <= nam <= nam_hien_tai):
        raise ValueError("Ngày tháng năm không hợp lệ!")

    so_chu_dao = tinh_so_chu_dao(ngay, thang, nam)
    cau_quote = lay_cau_quote(so_chu_dao)

    print(f"Con số chủ đạo của {ngay}/{thang}/{nam} là: {so_chu_dao}")
    print(f"Quote hôm nay: {cau_quote}")
except ValueError:
    print("Vui lòng nhập ngày tháng năm hợp lệ!")