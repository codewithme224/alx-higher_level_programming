#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


def main():
    """main function"""

    import MySQLdb
    from sys import argv

    """ Open database connection """
    db = MySQLdb.connect(host="localhost", port=3306,
            user=argv[1], passwd=argv[2], db=argv[3], charset="utf8")

    """prepare a cursor object using cursor() method"""
    cur = db.cursor()

    """execute SQL query using execute() method."""
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    """Fetch a single row using fetchone() method."""
    for row in cur.fetchall():
        print(row)

    """disconnect from server"""
    cur.close()
    db.close()

    if __name__ == "__main__":
        main()
