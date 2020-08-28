#!/usr/bin/python3
""" Script takes yr Github credentials uses Gh API 2 display yr id """
if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    import sys

    username = sys.argv[1]
    password = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(username, password))
    response = response.json()
    print(response.get('id'))
