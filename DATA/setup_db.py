import sqlite3

conn = sqlite3.connect("management.db")  # Tạo database mới
cursor = conn.cursor()

# Định nghĩa các bảng
sql_commands = [
    """CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        role TEXT CHECK(role IN ('admin', 'manager', 'user')) DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );""",

    """CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT,
        start_date DATE,
        end_date DATE,
        owner_id INTEGER,
        FOREIGN KEY (owner_id) REFERENCES users(id) ON DELETE SET NULL
    );""",

    """CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        status TEXT CHECK(status IN ('pending', 'in_progress', 'completed')) DEFAULT 'pending',
        priority INTEGER CHECK(priority BETWEEN 1 AND 5) DEFAULT 3,
        due_date DATE,
        project_id INTEGER,
        assigned_to INTEGER,
        FOREIGN KEY (project_id) REFERENCES projects(id) ON DELETE CASCADE,
        FOREIGN KEY (assigned_to) REFERENCES users(id) ON DELETE SET NULL
    );""",

    """CREATE TABLE IF NOT EXISTS logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        action TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE SET NULL
    );"""
]

# Thực thi các câu lệnh SQL
for command in sql_commands:
    cursor.execute(command)

conn.commit()
conn.close()

print("Database và các bảng đã được tạo thành công!")
