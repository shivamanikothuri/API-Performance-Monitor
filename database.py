import sqlite3
from datetime import datetime

DATABASE_NAME = "monitor.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS api_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT NOT NULL,
            status_code INTEGER,
            response_time REAL,
            status TEXT,
            timestamp TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def save_result(result):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO api_logs
        (url, status_code, response_time, status, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (
        result["url"],
        result["status_code"],
        result["response_time"],
        result["status"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    connection.commit()
    connection.close()


def get_results():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT url, status_code, response_time, status, timestamp
        FROM api_logs
        ORDER BY id DESC
    """)

    results = cursor.fetchall()
    connection.close()

    return results