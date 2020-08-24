#!/usr/bin/python3
""" Script to fetch webpage information """
from urllib import request
with request.urlopen('https://intranet.hbtn.io/status') as response:
    data = response.read()
    data2 = data.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(data)))
    print("\t- content: {}".format(data))
    print("\t- utf8 content: {}".format(data2))
