#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 2:
        if sys.argv[1].isalpha():
            q = sys.argv[1]
        else:
            q = ""
    else:
        q = ""

    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
        json_dict = response.json()

        if len(json_dict) > 0:
            print("[{}] {}".format(json_dict.get("id"), json_dict.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
