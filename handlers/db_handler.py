from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from aiogram import Router

from config import DB_URL

router = Router()

db_url = DB_URL
engine = create_engine(db_url, echo=True)


def create_table_user():
    try:
        query = '''CREATE TABLE IF NOT EXISTS users ( 
                                 id serial PRIMARY KEY, 
                                 user_id integer UNIQUE,
                                 username varchar UNIQUE, 
                                 first_name varchar, 
                                 last_name varchar)'''

        with engine.connect() as conn:
            conn.execute(text(query))
            conn.commit()
            print("user table created")

    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")


def insert_user(user_id, username, first_name, last_name):
    try:
        query = '''INSERT INTO users (user_id, username, first_name, last_name)
                VALUES (:user_id, :username, :first_name, :last_name)'''

        with engine.connect() as conn:
            conn.execute(text(query),
                         {"user_id": user_id, "username": username, "first_name": first_name, "last_name": last_name})
            conn.commit()
            print("user created successful")

    except SQLAlchemyError as e:
        print(f"Error inserting user: {e}")


def create_reminder():
    try:
        query = '''CREATE TABLE IF NOT EXISTS reminder (
                                id serial PRIMARY KEY,
                                description varchar,
                                noty_at timestamp,
                                is_done boolean,
                                user_pk integer,
                                FOREIGN KEY (user_pk) REFERENCES users(user_id))'''

        with engine.connect() as conn:
            conn.execute(text(query))
            conn.commit()
            print("reminder table create")

    except SQLAlchemyError as e:
        print(f"Error creating table: {e}")


def insert_reminder(description, noty_at, is_done, user_pk):
    try:
        query = '''INSERT INTO reminder (description, noty_at, is_done, user_pk)
                VALUES (:description, :noty_at, :is_done, :user_pk)'''

        with engine.connect() as conn:
            conn.execute(text(query),
                         {"description": description, "noty_at": noty_at, "is_done": is_done, "user_pk": user_pk})
            conn.commit()
            print("reminder created successful")

    except SQLAlchemyError as e:
        print(f"Error inserting reminder: {e}")


# def valid_pk(input_id):
#     try:
#         with sqlite3.connect('../users.sqlite') as conn:
#             cursor = conn.cursor()
#
#             cursor.execute("SELECT id FROM users WHERE user_id = ?", (input_id,))
#
#             result = cursor.fetchone()
#             print(result[0])
#             return result[0]
#     except sqlite3.Error as e:
#         return print(f"Error user don't found {e}")


def get_reminders_to_show(current_date):
    try:
        query = '''SELECT * FROM reminder WHERE noty_at <= :current_date AND is_done = FALSE'''

        with engine.connect() as conn:
            reminder = conn.execute(text(query), {"current_date": current_date}).fetchall()

        return reminder
    except SQLAlchemyError as e:
        print(f"Error alert list: {e}")


def get_reminder_list(current_date):
    try:
        query = '''SELECT * FROM reminder WHERE noty_at >= :current_date ORDER BY noty_at'''

        with engine.connect() as conn:
            reminder = conn.execute(text(query), {"current_date": current_date}).fetchall()

        return reminder
    except SQLAlchemyError as e:
        print(f"Error reminder list: {e}")


def edit_reminder_stat(reminder_id):
    try:
        query = '''UPDATE reminder SET is_done = :is_done WHERE id = :reminder_id'''

        with engine.connect() as conn:
            conn.execute(text(query), {"reminder_id": reminder_id, "is_done": True})
            conn.commit()
            print("Status changed")

    except SQLAlchemyError as e:
        print(f"Error updating: {e}")


def delete_reminder_from_db(reminder_id):
    try:
        query = '''DELETE FROM reminder WHERE id = :reminder_id'''

        with engine.connect() as conn:
            conn.execute(text(query), {"reminder_id": reminder_id})
            conn.commit()
            print("Reminder was delete")

    except SQLAlchemyError as e:
        print(f"Error deleting: {e}")

#
# insert_user(9809809, "sdjfhjk", "sgdf", "fwefg")
