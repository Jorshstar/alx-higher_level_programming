#!/usr/bin/python3
"""
Write a Python script that;
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].isalpha():
            q = sys.argv[1]
        else:
            print("No result")
            exit()
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    try:
        r = requests.post(url, data={"q": q})
        json_dict = r.json()

        if len(json_dict) == 0:
            print("No result")
        else:
            id = json_dict.get("id")
            name = json_dict.get("name")
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
