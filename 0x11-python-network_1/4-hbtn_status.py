#!/usr/bin/python3
""" script to fetch url """
if __name__ == "__main__":
    import requests
    response = requests.get('https://intranet.hbtn.io/status')
    response.encoding = 'utf-8'
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
