from DB import config
import sqlite3


def create(data):
    try:
        if checkEmail(data["email"]):
            return False, "Email already exists!", 400
        else:
            connect, cursor = config.db_connection()
            insert_id = insert_data(cursor, data)
            config.db_connection_close(connect)

            return insert_id, "", 200
    except sqlite3.Error as e:
        return e.args[0], 400


def insert_data(cursor, data):
    cursor.execute("INSERT INTO contacts VALUES ("
                   ":first_name, :last_name, :address, :city, :state, "
                   ":zip_code, :phone, :email)", {
                       'first_name': data["firstName"],
                       'last_name': data["lastName"],
                       'address': data["address"],
                       'city': data["city"],
                       'state': data["state"],
                       'zip_code': data["zipCode"],
                       'phone': data["phone"],
                       'email': data["email"],
                   })
    return cursor.lastrowid


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


def checkEmail(email):
    connect, cursor = config.db_connection()
    cursor.execute(f"SELECT oid, email FROM contacts WHERE email='{email}'")
    record = cursor.fetchone()
    config.db_connection_close(connect)

    if record:
        return True
    else:
        return False
