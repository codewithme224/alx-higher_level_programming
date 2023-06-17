#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
            port=3306,
            host="localhost",
            charset="utf8"
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = db.cursor()
    cur.execute(
            "SELECT * FROM `states` WHERE `name` LIKE %s ORDER BY id ASC",
            (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
