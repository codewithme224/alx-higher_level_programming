#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    """Connect to MySQL database"""
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=sys.argv[1],
            password=sys.argv[2],
            database=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states\
            INNER JOIN cities ON states.id = cities.state_id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC", (sys.argv[4],))
    rows = cursor.fetchall()
    print(", ".join([city[0] for city in rows]))

    cur.close()
    db.close()
