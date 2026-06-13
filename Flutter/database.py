import sqlite3

DB_NAME = "traffic_reports.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS reports(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        violation TEXT,
        image_path TEXT,
        confidence REAL,
        location TEXT,
        timestamp TEXT
    )
    """)

    conn.commit()
    conn.close()

def add_report(
    violation,
    image_path,
    confidence,
    location,
    timestamp
):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO reports(
        violation,
        image_path,
        confidence,
        location,
        timestamp
    )
    VALUES(?,?,?,?,?)
    """,
    (
        violation,
        image_path,
        confidence,
        location,
        timestamp
    ))

    conn.commit()
    conn.close()

def get_reports():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM reports
    ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data