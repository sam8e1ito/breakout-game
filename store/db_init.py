import sqlite3
import os

_connection = None
DB_PATH = os.path.join(os.path.dirname(__file__), 'score.sqlite')

def init_db():
    global _connection
    _connection = sqlite3.connect(DB_PATH)
    _connection.row_factory = sqlite3.Row

def close_db():
    global _connection
    if _connection is not None:
        _connection.close()
        _connection = None

def execute_write(sql: str, params: tuple = ()):
    _connection.execute(sql, params)
    _connection.commit()

def execute_read(sql: str, params: tuple = ()):
    cursor = _connection.execute(sql, params)
    return cursor.fetchall()