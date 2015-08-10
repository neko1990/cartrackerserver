import sqlite3

DB_NAME = "position-log.sqlite3"

conn = sqlite3.connect(DB_NAME)
conn.row_factory = sqlite3.Row
conn.text_factory = str


def setup_position_db_log():
    cur = conn.cursor()
    with open("schema.sql",'r') as f:
        create_table_command = f.read()
    cur.execute(create_table_command)
    conn.commit()


def get_db_connection():
    return conn


def db_write():
    conn.commit()


def insert_log(name,lng,lat):
    conn.execute("""INSERT INTO positionlogs (devicename,lng,lat) VALUES (?,?,?)""",(name,lng,lat))
