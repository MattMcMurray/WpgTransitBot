__author__ = 'Mathieu'

import MySQLdb


def connect():
    conn = MySQLdb.connect(host='localhost',
                           user='root',
                           passwd='', #TODO
                           db='') #TODO

    c = conn.cursor()

    return c, conn

def close(cursor, conn):
    cursor.close()
    conn.close()
