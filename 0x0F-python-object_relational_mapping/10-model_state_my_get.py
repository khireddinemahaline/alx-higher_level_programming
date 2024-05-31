#!/usr/bin/python3
""" lists all State objects from the database """
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engin = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engin)
    session = sessionmaker(bind=engin)
    session = session()
    match = sys.argv[4]
    instance = session.query(State).filter((match,) == State.name)
    try:
        print(instance[0].id)
    except IndexError:
        print("Not found")
