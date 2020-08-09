#!/usr/bin/python3
""" Script to list all City and State objects from database given """
if __name__ == "__main__":
    import sqlalchemy
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from model_city import City
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for state, city in session.query(State, City).order_by(City.id).all():
        if (state.id == city.state_id):
            print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
