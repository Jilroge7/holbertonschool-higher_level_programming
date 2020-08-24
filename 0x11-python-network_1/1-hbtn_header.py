#!/usr/bin/python3
""" script to get url and display 'X-Request-Id' """
if __name__ == "__main__":
    import sys
    from urllib import request
    with request.urlopen(sys.argv[1]) as response:
        header = response.getheader("X-Request-Id")
        print(header)
