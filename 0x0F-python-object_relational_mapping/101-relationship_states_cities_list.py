#!/usr/bin/python3
""" Script to list all sate and corresponding city objects frm database """
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.orm import relationship
    from relationship_state import State, Base
    from relationship_city import City
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    for \
        state, city in \
            session.query(State).order_by(states.id, State.cities.id).all():
        if (state.id == state.cities.id):
            tabulation = 1
            print("{}: {}".format(state.id, state.name))
            print("{}{}: {}".format(tabulation, city.id, city.name))
            tabulation += 1
    session.close()
