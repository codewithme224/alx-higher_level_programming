#!/usr/bin/python3
"""Module to list all states from database hbtn_0e_0_usa"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    """Connect to MySQL database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    session = Session()

    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))

        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))

    session.close()
