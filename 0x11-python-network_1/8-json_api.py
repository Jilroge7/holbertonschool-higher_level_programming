#!/usr/bin/python3
""" Script to query for id and name in url """
if __name__ == "__main__":
    import requests
    import sys
    try:
        response = requests.get('http://0.0.0.0:5000/search_user',
                                params={'q': sys.argv[0]})
        json_response = response.json()
        if json_response.status_code == 204 or \
           json_response.raise_for_status():
            print("Not a valid JSON")
        # repository = json_response['items'][0]
        # print("[{}] {}".format(***something***)
    except IndexError:
        print("No result")
