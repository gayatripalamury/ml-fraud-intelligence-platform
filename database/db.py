import sqlite3

DATABASE = "transactions.db"

def get_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        location TEXT,
        device TEXT,
        hour INTEGER,
        risk_score REAL
    )
    """)

    conn.commit()
    conn.close()


def get_all_transactions():
    conn = get_connection()

    rows = conn.execute(
        "SELECT * FROM transactions ORDER BY id DESC"
    ).fetchall()

    conn.close()

    return rows