#!/usr/bin/python3
""" Module to list all states from a database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    curse = conn.cursor()
    curse.execute("SELECT cities.id, cities.name, states.name FROM \
                  cities JOIN states ON cities.state_id=states.id")
    looky_rows = curse.fetchall()
    for row in looky_rows:
        print(row)
    curse.close()
    conn.close()
