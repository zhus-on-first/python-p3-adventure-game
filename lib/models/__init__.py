import sqlite3

CONN = sqlite3.connect('game.db')
CURSOR = CONN.cursor()


def close_connection():
    CONN.close()
