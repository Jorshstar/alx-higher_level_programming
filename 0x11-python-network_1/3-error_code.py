#!/usr/bin/python3
"""write a python script that;
Sends a request to the URL and displays the body of the response.

Handles urllib.error.HTTPError exceptions and prints the error code followed by
the HTTP status code.
"""

import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
