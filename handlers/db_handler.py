import sqlite3

from aiogram import Router

router = Router()


def create_user():
    try:
        with sqlite3.connect('users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
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


def create_reminder():
    try:
        with sqlite3.connect('users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS reminder (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT,
                                noty_at DATETIME,
                                user_pk INTEGER,
                                FOREIGN KEY (user_pk) REFERENCES users(user_id)
                           )''')
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_reminder(description, noty_at, user_pk):
    try:
        with sqlite3.connect('users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO reminder (description, noty_at, user_pk) VALUES (?, ?, ?)",
                           (description, noty_at, user_pk))
            conn.commit()
    except sqlite3.Error as e:
        print(f"Error inserting reminder: {e}")


def valid_pk(input_id):
    try:
        with sqlite3.connect('users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM users WHERE user_id = ?", (input_id,))

            result = cursor.fetchone()
            print(result[0])
            return result[0]
    except sqlite3.Error as e:
        return print(f"Error user don't found {e}")
