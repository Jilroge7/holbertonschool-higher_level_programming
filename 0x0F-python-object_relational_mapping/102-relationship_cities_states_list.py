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
    res = session.query(City).all()
    for city in res:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))
    session.close()
