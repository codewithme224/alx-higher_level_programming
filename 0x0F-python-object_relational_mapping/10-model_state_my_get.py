#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """Connect to MySQL database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        print("{}".format(session.query(State).filter(
            State.name == sys.argv[4]).first().id))
    except ValueError:
        print("Not found")

    session.close()
