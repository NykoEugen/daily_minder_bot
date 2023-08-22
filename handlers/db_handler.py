import sqlite3
from datetime import datetime

from aiogram import Router

router = Router()


def create_user():
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id TEXT UNIQUE,
                                username TEXT UNIQUE,
                                first_name TEXT,
                                last_name TEXT
                           )''')
            conn.commit()
            print("user table created")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_user(user_id, username, first_name, last_name):
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (user_id, username, first_name, last_name) VALUES (?, ?, ?, ?)",
                           (user_id, username, first_name, last_name))
            conn.commit()
            print("user created successful")
    except sqlite3.Error as e:
        print(f"Error inserting user: {e}")


def create_reminder():
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute('''CREATE TABLE IF NOT EXISTS reminder (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                description TEXT,
                                noty_at DATETIME,
                                is_done INTEGER,
                                user_pk INTEGER,
                                FOREIGN KEY (user_pk) REFERENCES users(user_id)
                           )''')
            conn.commit()
            print("reminder table create")
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")


def insert_reminder(description, noty_at, is_done, user_pk):
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("INSERT INTO reminder (description, noty_at, is_done, user_pk) "
                           "VALUES (?, ?, ?, ?)", (description, noty_at, is_done, user_pk))
            conn.commit()
            print("reminder created successful")
    except sqlite3.Error as e:
        print(f"Error inserting reminder: {e}")


def valid_pk(input_id):
    try:
        with sqlite3.connect('../users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT id FROM users WHERE user_id = ?", (input_id,))

            result = cursor.fetchone()
            print(result[0])
            return result[0]
    except sqlite3.Error as e:
        return print(f"Error user don't found {e}")


def get_reminders_to_show(current_date):
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM reminder WHERE noty_at <= ? AND is_done = 0", (current_date,))

            reminder = cursor.fetchall()
        return reminder
    except Exception as e:
        print(f"Error alert list: {e}")


def get_reminder_list(current_date):
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM reminder WHERE noty_at >= ? ORDER BY noty_at",
                           (current_date,))

            reminder = cursor.fetchall()
        return reminder
    except Exception as e:
        print(f"Error reminder list: {e}")


def edit_reminder_stat(reminder_id):
    try:
        with sqlite3.connect('./users.sqlite') as conn:
            cursor = conn.cursor()

            cursor.execute("UPDATE reminder SET is_done = ? WHERE id = ?",
                           (1, reminder_id,))
            conn.commit()
        print("Status changed")
    except Exception as e:
        print(f"Error updating: {e}")
