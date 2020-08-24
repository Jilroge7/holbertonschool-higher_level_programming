#!/usr/bin/python3
""" script to send post req to url with email as param """
if __name__ == "__main__":
    import sys
    from urllib import request
    from urllib import parse
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('utf-8')
    with request.urlopen(sys.argv[1], data) as response:
            data = response.read().decode('utf-8')
            print(data)
