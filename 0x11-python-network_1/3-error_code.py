#!/usr/bin/python3
""" script to take a url and display response decoded in utf-8 """
if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib import parse
    from urllib import error
    try:
        with request.urlopen(sys.argv[1]) as response:
            data = response.read().decode('utf-8')
            print(data)
    except error.HTTPError as e:
            print("Error code: {}".format(e.code))
