import MySQLdb
from secrets import DATABASE_USER, DATABASE_PASSWORD, DATABASE_NAME

def connect():
    conn = MySQLdb.connect(host='localhost',
                           user=DATABASE_USER,
                           passwd=DATABASE_PASSWORD,
                           db=DATABASE_NAME)

    c = conn.cursor()

    return c, conn


def close(cursor, conn):
    cursor.close()
    conn.close()
