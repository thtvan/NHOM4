import sys
import json
import sqlite3
import matplotlib.pyplot as plt
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel,
                             QLineEdit, QPushButton, QMessageBox, QTextEdit,
                             QListWidget, QHBoxLayout)


class DataEntryApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_tasks()

    def init_ui(self):
        self.setWindowTitle("Quản lý Công Việc & Cảm Xúc")
        self.setGeometry(100, 100, 500, 600)
        layout = QVBoxLayout()

        # Form nhập công việc
        self.label1 = QLabel("Tiêu đề công việc:")
        self.input_title = QLineEdit()
        layout.addWidget(self.label1)
        layout.addWidget(self.input_title)

        self.label2 = QLabel("Mô tả:")
        self.input_desc = QTextEdit()
        layout.addWidget(self.label2)
        layout.addWidget(self.input_desc)

        self.label3 = QLabel("Mức độ ưu tiên (1-5):")
        self.input_priority = QLineEdit()
        layout.addWidget(self.label3)
        layout.addWidget(self.input_priority)

        self.label4 = QLabel("Hạn chót (YYYY-MM-DD):")
        self.input_due = QLineEdit()
        layout.addWidget(self.label4)
        layout.addWidget(self.input_due)

        self.btn_submit = QPushButton("Lưu Công Việc")
        self.btn_submit.clicked.connect(self.save_data)
        layout.addWidget(self.btn_submit)

        # Form nhập tâm trạng
        self.label5 = QLabel("Ghi chú tâm trạng:")
        self.input_mood = QTextEdit()
        layout.addWidget(self.label5)
        layout.addWidget(self.input_mood)

        self.btn_mood = QPushButton("Lưu Tâm Trạng")
        self.btn_mood.clicked.connect(self.save_mood)
        layout.addWidget(self.btn_mood)

        # Form nhập nhắc nhở
        self.label6 = QLabel("Nhắc nhở:")
        self.input_reminder = QTextEdit()
        layout.addWidget(self.label6)
        layout.addWidget(self.input_reminder)

        self.btn_reminder = QPushButton("Lưu Nhắc Nhở")
        self.btn_reminder.clicked.connect(self.save_reminder)
        layout.addWidget(self.btn_reminder)

        # Form nhập câu quote
        self.label7 = QLabel("Câu Quote:")
        self.input_quote = QTextEdit()
        layout.addWidget(self.label7)
        layout.addWidget(self.input_quote)

        self.btn_quote = QPushButton("Lưu Quote")
        self.btn_quote.clicked.connect(self.save_quote)
        layout.addWidget(self.btn_quote)

        # Hiển thị danh sách công việc
        self.task_list = QListWidget()
        layout.addWidget(QLabel("Danh sách công việc:"))
        layout.addWidget(self.task_list)

        self.btn_show_chart = QPushButton("Xem Biểu Đồ Cảm Xúc")
        self.btn_show_chart.clicked.connect(self.show_mood_chart)
        layout.addWidget(self.btn_show_chart)

        self.setLayout(layout)

    def save_data(self):
        title = self.input_title.text()
        desc = self.input_desc.toPlainText()
        priority = self.input_priority.text()
        due_date = self.input_due.text()

        if not (title and priority.isdigit() and due_date):
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập đủ thông tin hợp lệ!")
            return

        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO goals (user_id, title, description, priority, due_date) VALUES (1, ?, ?, ?, ?)",
                       (title, desc, int(priority), due_date))
        conn.commit()
        conn.close()

        self.export_to_json()
        self.load_tasks()
        QMessageBox.information(self, "Thành công", "Dữ liệu đã được lưu!")

        self.input_title.clear()
        self.input_desc.clear()
        self.input_priority.clear()
        self.input_due.clear()

    def save_mood(self):
        mood_text = self.input_mood.toPlainText()
        if not mood_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập nội dung tâm trạng!")
            return

        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO mood_entries (user_id, mood_text) VALUES (1, ?)", (mood_text,))
        conn.commit()
        conn.close()

        self.export_to_json()
        QMessageBox.information(self, "Thành công", "Tâm trạng đã được lưu!")
        self.input_mood.clear()

    def save_reminder(self):
        reminder_text = self.input_reminder.toPlainText()
        if not reminder_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập nội dung nhắc nhở!")
            return

        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO reminders (user_id, reminder_text) VALUES (1, ?)", (reminder_text,))
        conn.commit()
        conn.close()

        self.export_to_json()
        QMessageBox.information(self, "Thành công", "Nhắc nhở đã được lưu!")
        self.input_reminder.clear()

    def save_quote(self):
        quote_text = self.input_quote.toPlainText()
        if not quote_text:
            QMessageBox.warning(self, "Lỗi", "Vui lòng nhập nội dung quote!")
            return

        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO quotes (user_id, quote_text) VALUES (1, ?)", (quote_text,))
        conn.commit()
        conn.close()

        self.export_to_json()
        QMessageBox.information(self, "Thành công", "Quote đã được lưu!")
        self.input_quote.clear()

    def load_tasks(self):
        self.task_list.clear()
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        cursor.execute("SELECT title, due_date FROM goals")
        tasks = cursor.fetchall()
        conn.close()

        for task in tasks:
            self.task_list.addItem(f"{task[0]} - Hạn chót: {task[1]}")

    def export_to_json(self):
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()

        tables = ['goals', 'mood_entries', 'reminders', 'quotes']
        backup_data = {}

        for table in tables:
            cursor.execute(f"SELECT * FROM {table}")
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchall()
            backup_data[table] = [dict(zip(columns, row)) for row in rows]

        with open("backup_data.json", "w", encoding="utf-8") as f:
            json.dump(backup_data, f, indent=4, ensure_ascii=False)

        conn.close()
        print("Dữ liệu đã được lưu vào backup_data.json")

    def show_mood_chart(self):
        conn = sqlite3.connect("task_manager.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, mood_text FROM mood_entries")
        data = cursor.fetchall()
        conn.close()

        if not data:
            QMessageBox.warning(self, "Lỗi", "Không có dữ liệu tâm trạng!")
            return

        mood_ids = [item[0] for item in data]
        mood_texts = [len(item[1]) for item in data]

        plt.figure(figsize=(6, 4))
        plt.plot(mood_ids, mood_texts, marker='o', linestyle='-', color='b')
        plt.xlabel("Lần ghi tâm trạng")
        plt.ylabel("Độ dài nội dung tâm trạng")
        plt.title("Thống kê cảm xúc theo thời gian")
        plt.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DataEntryApp()
    window.show()
    sys.exit(app.exec())
