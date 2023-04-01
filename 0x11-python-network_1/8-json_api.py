#!/usr/bin/python3
"""
This script sends a POST request to http://0.0.0.0:5000/search_user with a given letter as a parameter.
If the response body is properly JSON formatted and not empty, it displays the id and name of the first user.
Otherwise, it displays a corresponding message.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) == 2:
        letter = sys.argv[1]
    else:
        letter = ""
    
    try:
        response = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
        if response.headers.get('content-type') != 'application/json':
            raise ValueError("Not a valid JSON")
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data['id'], data['name']))
    except ValueError as e:
        print(e)
