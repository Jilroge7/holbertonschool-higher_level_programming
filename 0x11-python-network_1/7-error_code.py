#!/usr/bin/python3
""" Script to display error code of url path """
if __name__ == "__main__":
    import requests
    import sys
    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        response.encoding = 'utf-8'
        print(response.text)
    except:
        print("Error code: {}".format(response.status_code))
