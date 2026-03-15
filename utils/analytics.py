import sqlite3

def get_system_stats():

    conn = sqlite3.connect("transactions.db")
    cursor = conn.cursor()

    total = cursor.execute(
        "SELECT COUNT(*) FROM transactions"
    ).fetchone()[0]

    high = cursor.execute(
        "SELECT COUNT(*) FROM transactions WHERE risk_score > 0.7"
    ).fetchone()[0]

    medium = cursor.execute(
        "SELECT COUNT(*) FROM transactions WHERE risk_score BETWEEN 0.4 AND 0.7"
    ).fetchone()[0]

    low = cursor.execute(
        "SELECT COUNT(*) FROM transactions WHERE risk_score < 0.4"
    ).fetchone()[0]

    conn.close()

    return {
        "total": total,
        "high": high,
        "medium": medium,
        "low": low
    }