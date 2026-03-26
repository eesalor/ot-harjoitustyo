import sqlite3
from config import DATABASE

connection = sqlite3.connect(DATABASE)
connection.isolation_level = None
connection.row_factory = sqlite3.Row


def get_database_connection():
    return connection