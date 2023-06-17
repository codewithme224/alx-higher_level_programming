#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
            port=3306,
            host="localhost",
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = db.cursor()
    cur.execute(
            "SELECT * FROM `states` WHERE `name` = %s", (sys.argv[4],))
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]

    cur.close()
    db.close()
