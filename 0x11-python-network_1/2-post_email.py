#!/usr/bin/python3
""" script to send post req to url with email as param """
if __name__ == "__main__":
    import sys
    import urllib
    values = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    with request.Request(sys.argv[1], data) as reques:
        with urllip.request.urlopen(reques) as response:
            print(response.read())
