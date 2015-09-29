import sqlite3
import settings
import datetime

conn = sqlite3.connect(settings.DB_NAME)

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

def get_cars():
    cars = {}
    now = datetime.datetime.utcnow()
    results = conn.execute("""SELECT devicename,lng,lat,ctime \
    FROM positionlogs GROUP BY devicename ORDER BY logid DESC LIMIT 1;""").fetchall()
    for car in results:
        if now - datetime.datetime.fromtimestamp(car[3]) < settings.TIMEOUT_INTERVAL:
            cars[car[0]] = (car[1],car[2])
    return cars

if __name__ == "__main__":
    get_cars()
