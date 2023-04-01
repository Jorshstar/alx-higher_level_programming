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
            print("No result")
            exit()
    else:
        q = ""

    url = "http://0.0.0.0:5000/search_user"
    try:
        r = requests.post(url, data={"q": q})
        r.raise_for_status()  # Check if the request was successful

        json_dict = r.json()
        if len(json_dict) == 0:
            print("No result")
        else:
            user_id = json_dict.get("id")
            name = json_dict.get("name")
            print("[{}] {}".format(user_id, name))
    except requests.exceptions.HTTPError as e:
        print("HTTP error: {}".format(e))
    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")
    except Exception as e:
        print("An error occurred: {}".format(e))
