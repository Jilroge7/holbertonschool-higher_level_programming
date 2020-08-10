#!/usr/bin/python3
""" Module to list all states from a database """
if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=sys.argv[1], passwd=sys.argv[2],
                           db=sys.argv[3])
    curse = conn.cursor()
    curse.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
                  .format(sys.argv[4]))
    looky_rows = curse.fetchall()
    for row in looky_rows.split():
        if row[0].isupper():
            print(row)
    curse.close()
    conn.close()
