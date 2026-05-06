import sqlite3

DB_NAME = "ruta_optima.db"

def conectar():
    return sqlite3.connect(DB_NAME)

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS envios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        peso REAL,
        destino TEXT,
        tipo TEXT,
        costo REAL,
        cliente_id INTEGER,
        FOREIGN KEY(cliente_id) REFERENCES clientes(id)
    )
    """)

    conn.commit()
    conn.close()