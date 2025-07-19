import sqlite3

DB_NAME = "f1.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS drivers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nama TEXT,
            tim TEXT,
            negara TEXT,
            point INTEGER,
            juara INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def insert_driver(nama, tim, negara, point, juara=0):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        INSERT INTO drivers (nama, tim, negara, point, juara)
        VALUES (?, ?, ?, ?, ?)
    ''', (nama, tim, negara, point, juara))
    conn.commit()
    conn.close()

def fetch_all_drivers():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('SELECT nama, tim, negara, point, juara FROM drivers')
    rows = c.fetchall()
    conn.close()
    return rows

def update_point(nama, tambah):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('UPDATE drivers SET point = point + ? WHERE nama = ?', (tambah, nama))
    conn.commit()
    conn.close()
