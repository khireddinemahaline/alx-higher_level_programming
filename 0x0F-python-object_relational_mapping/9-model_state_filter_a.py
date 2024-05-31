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
    for instance in session.query(State).order_by(State.id):
        if 'a' in str(instance.name):
            print(instance.id, instance.name, sep=': ')
