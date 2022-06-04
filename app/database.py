import sqlite3

def db_connect():
    conn = sqlite3.connect('../vgames.db')
    conn.row_factory = sqlite3.Row
    print("Database opened!")
    return conn

def create_table():
    try:
        conn = db_connect()
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS vgames(
                game_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                publisher TEXT NOT NULL, 
                rating INTEGER NOT NULL,
                price REAL NOT NULL,
                year INTEGER NOT NULL
            );
        ''')
        print("Video game table created!")
        conn.commit()
    except:
        print("Table creation failed")
    finally:
        print("closed")
        conn.close()
