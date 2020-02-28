from DB import config
import sqlite3


def list():
    try:
        connect, cursor = config.db_connection()
        cursor.execute("SELECT oid, * FROM contacts")
        records = cursor.fetchall()
        config.db_connection_close(connect)

        return records, 200
    except sqlite3.Error as e:
        return e.args[0], 400


def detail(id):
    try:
        connect, cursor = config.db_connection()
        cursor.execute(f"SELECT oid, * FROM contacts WHERE oid={id}")
        records = cursor.fetchall()
        config.db_connection_close(connect)

        return records, 200
    except sqlite3.Error as e:
        return e.args[0], 400
