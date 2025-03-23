import sqlite3
import heapq
import json
from datetime import datetime


# Kết nối SQLite
def connect_db():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()
    return conn, cursor


# Tạo bảng
def create_tables():
    conn, cursor = connect_db()
    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,py
        name TEXT,
        birthdate TEXT
    );

    CREATE TABLE IF NOT EXISTS goals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        title TEXT,
        description TEXT,
        priority INTEGER,
        due_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS mood_entries (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        date TEXT,
        mood TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS reminders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        message TEXT,
        reminder_date TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id)
    );

    CREATE TABLE IF NOT EXISTS quotes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        numerology_number INTEGER,
        quote TEXT
    );
    ''')
    conn.commit()
    conn.close()


# Class OOP
class Goal:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date


class MoodEntry:
    def __init__(self, mood, date=datetime.now().strftime('%Y-%m-%d')):
        self.mood = mood
        self.date = date


class Reminder:
    def __init__(self, message, reminder_date):
        self.message = message
        self.reminder_date = reminder_date


class Numerology:
    @staticmethod
    def calculate_life_path_number(birthdate):
        numbers = [int(digit) for digit in birthdate.replace("-", "")]
        while len(numbers) > 1:
            numbers = [int(digit) for digit in str(sum(numbers))]
        return numbers[0]


# Quản lý công việc theo heapq
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, goal):
        heapq.heappush(self.tasks, (goal.priority, goal))

    def get_next_task(self):
        return heapq.heappop(self.tasks)[1] if self.tasks else None


# Backup dữ liệu
def backup_data():
    conn, cursor = connect_db()
    tables = ['users', 'goals', 'mood_entries', 'reminders', 'quotes']
    backup = {}
    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        backup[table] = cursor.fetchall()

    with open("backup.json", "w") as f:
        json.dump(backup, f, indent=4)

    conn.close()


# Chạy hệ thống
if __name__ == "__main__":
    create_tables()
    print("Database initialized and tables created.")

import json


def export_to_json():
    conn, cursor = connect_db()
    tables = ['users', 'goals', 'mood_entries', 'reminders', 'quotes']
    backup_data = {}

    for table in tables:
        cursor.execute(f"SELECT * FROM {table}")
        columns = [desc[0] for desc in cursor.description]  # Lấy tên cột
        rows = cursor.fetchall()

        # Chuyển dữ liệu thành dạng dictionary
        backup_data[table] = [dict(zip(columns, row)) for row in rows]

    # Ghi ra file JSON
    with open("backup_data.json", "w", encoding="utf-8") as f:
        json.dump(backup_data, f, indent=4, ensure_ascii=False)

    conn.close()
    print("Dữ liệu đã được lưu vào backup_data.json")


# Gọi hàm để lưu dữ liệu
export_to_json()


#import matplotlib.pyplot as plt
#plt.plot([1, 2, 3], [4, 5, 6])
#plt.show()

import sqlite3
import json

# Kết nối database
def connect_db():
    conn = sqlite3.connect("task_manager.db")
    cursor = conn.cursor()
    return conn, cursor

# Đọc dữ liệu từ JSON
with open("backup_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

goals = data["goals"]

# Kết nối SQLite
conn, cursor = connect_db()

# Câu lệnh INSERT hoặc UPDATE nếu ID đã tồn tại
for goal in goals:
    cursor.execute("SELECT id FROM goals WHERE id = ?", (goal["id"],))
    existing_id = cursor.fetchone()

    if existing_id is None:
        # Thêm dữ liệu mới
        cursor.execute("""
            INSERT INTO goals (id, user_id, title, description, priority, due_date) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            goal["id"],
            goal["user_id"],
            goal["title"],
            goal["description"],
            goal["priority"],
            goal["due_date"]
        ))
        print(f"Thêm mới ID {goal['id']} thành công.")
    else:
        # Cập nhật dữ liệu nếu ID đã tồn tại
        cursor.execute("""
            UPDATE goals 
            SET user_id = ?, title = ?, description = ?, priority = ?, due_date = ?
            WHERE id = ?
        """, (
            goal["user_id"],
            goal["title"],
            goal["description"],
            goal["priority"],
            goal["due_date"],
            goal["id"]
        ))
        print(f"Cập nhật ID {goal['id']} thành công.")

# Lưu thay đổi vào database
conn.commit()
print("Dữ liệu từ JSON đã được đồng bộ vào bảng goals!")

# Đóng kết nối
conn.close()



