#!/usr/bin/python3
""" Script to list all city objects related to state frm database """
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import State, Base
    from relationship_city import City
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    states = session.query(State).all()
    for single_state in states:
        print(" {}: {}".format(single_state.id, single_state.name))
        for city in single_state.cities:
            print("\t{}: {}".format(city.id, city.name))
    session.close()
