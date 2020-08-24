#!/usr/bin/python3
""" script to fetch url """
if __name__ == "__main__":
    from urllib import request
    with request.urlopen('https://intranet.hbtn.io/status') as response:
        https = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(https)))
        print("\t- content: {}".format(https))
