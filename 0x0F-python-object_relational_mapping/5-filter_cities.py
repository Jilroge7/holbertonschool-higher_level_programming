#!/usr/bin/python3
""" Module to list all states from a database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    curse = conn.cursor()
    curse.execute("SELECT cities.name FROM \
                  cities JOIN states ON cities.state_id=states.id WHERE \
                  states.name=%(name)s", {'name': sys.argv[4]})
    looky_rows = curse.fetchall()
    cityList = []
    for cities in looky_rows:
        city = str(cities).strip("()")
        city = city.replace("'", '')
        city = city.replace(",", "")
        cityList.append(city)
    print(', '.join(cityList))
    curse.close()
    conn.close()
