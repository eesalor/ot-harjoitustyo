import sqlite3

connection = sqlite3.connect("database.db")
connection.isolation_level = None
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection