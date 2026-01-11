import sqlite3

DB_NAME = "allowed_vehicles.db"

def connect_db():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS allowed_vehicles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            plate_number TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def add_vehicle(plate_number):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO allowed_vehicles (plate_number) VALUES (?)",
            (plate_number,)
        )
        conn.commit()
        print("✅ Vehicle added to allow list")
    except sqlite3.IntegrityError:
        print("⚠️ Vehicle already exists")
    conn.close()

def is_vehicle_allowed(plate_number):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT 1 FROM allowed_vehicles WHERE plate_number = ?",
        (plate_number,)
    )
    result = cursor.fetchone()
    conn.close()
    return result is not None
