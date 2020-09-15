#!/usr/bin/python3
""" Script to query for id and name in url """
if __name__ == "__main__":
    import requests
    import sys

    length = len(sys.argv)
    if length < 2:
        q = ""
    else:
        q = sys.argv[1]

    response = requests.post('http://0.0.0.0:5000/search_user',
                             data={'q': q})
    try:
        json_response = response.json()
        if json_response == {}:
            print("No result")
        else:
            json_id = json_response.get('id')
            json_name = json_response.get('name')
            print("[{}] {}".format(json_id, json_name))
    except:
        print("Not a valid JSON")
        exit()
