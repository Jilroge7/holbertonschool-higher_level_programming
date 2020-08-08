#!/usr/bin/python3
""" Script to list State id from a database object given """
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
    for \
        state in session.query(State).order_by(State.id). \
            all():
        if state.name == sys.argv[4]:
            print("{}".format(state.id))
            exit()
    print("Not found")
    session.close()
