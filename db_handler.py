import sqlite3


def connection():
    try:
        with sqlite3.connect('users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY,
                                user_id TEXT UNIQUE,
                                username TEXT UNIQUE,
                                first_name TEXT,
                                last_name TEXT
                           )''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_user(user_id, username, first_name, last_name):
    try:
        with sqlite3.connect('users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)",
                           (user_id, username, first_name, last_name))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting user: {e}")
