#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE `name` LIKE 'N%'")
    [print(state) for state in cur.fetchall()]
