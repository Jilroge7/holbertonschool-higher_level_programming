#!/usr/bin/python3
""" script to display email param of url """
if __name__ == "__main__":
    import requests
    import sys
    response = requests.post(sys.argv[1], data={'email': sys.argv[2]})
    print(response.text)
