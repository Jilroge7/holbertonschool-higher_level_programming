#!/usr/bin/python3
""" Script to list all State objects from a database given """
if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()
    try:
        state = session.query(State).order_by(State.id).first()
        print("{}: {}".format(state.id, state.name))
    except Exception:
        print("Nothing")
    session.close()
