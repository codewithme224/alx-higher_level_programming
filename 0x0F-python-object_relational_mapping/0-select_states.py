#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
