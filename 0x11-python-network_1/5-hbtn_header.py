#!/usr/bin/python3
""" script to fetch url """
if __name__ == "__main__":
    import requests
    import sys
    response = requests.get(sys.argv[1])
    header = response.headers['X-Request-Id']
    print(header)
