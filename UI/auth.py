
import json
import os
from pymongo import MongoClient

# Đường dẫn JSON
JSON_PATH = os.path.join(os.path.dirname(__file__), "users.json")

# MongoDB connection (dùng localhost hoặc MongoDB Atlas đều được)
client = MongoClient("mongodb://localhost:27017/")
db = client["nhom4_app"]
users_col = db["users"]

# --- Lưu vào JSON ---
def save_user_to_json(username, password, ngay, thang, nam):
    data = {}
    if os.path.exists(JSON_PATH):
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)

    # Nếu tài khoản đã tồn tại, không ghi đè
    if username in data:
        return False

    data[username] = {
        "password": password,
        "ngay": ngay,
        "thang": thang,
        "nam": nam
    }

    with open(JSON_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    return True


def check_login_json(username, password):
    if not os.path.exists(JSON_PATH):
        return False
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get(username) == password

# --- Lưu vào MongoDB ---
def save_user_to_mongodb(username, password, ngay, thang, nam):
    if users_col.find_one({"username": username}):
        return False  # Người dùng đã tồn tại

    users_col.insert_one({
        "username": username,
        "password": password,
        "ngay": ngay,
        "thang": thang,
        "nam": nam
    })
    return True

def check_login_mongodb(username, password):
    user = users_col.find_one({"username": username})
    return user and user["password"] == password

def load_users_from_json():
    """Đọc dữ liệu người dùng từ file JSON."""
    if not os.path.exists(JSON_PATH):
        return {}

    with open(JSON_PATH, "r", encoding="utf-8") as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            return {}
