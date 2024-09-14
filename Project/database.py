# database.py
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
    except Error as e:
        print(e)
    return conn


def create_table(conn):
    sql_create_users_table = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        age INTEGER,
        address TEXT
    );"""
    try:
        cursor = conn.cursor()
        cursor.execute(sql_create_users_table)
    except Error as e:
        print(e)


def add_user(conn, user):
    sql = '''INSERT INTO users(name, email, age, address)
             VALUES(?, ?, ?, ?)'''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (user.name, user.email, user.age, user.address))
        conn.commit()
        return cursor.lastrowid
    except Error as e:
        print(f"An error occurred: {e}")
        return None