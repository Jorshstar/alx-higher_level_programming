#!/usr/bin/python3
"""
Python script that uses the GitHub API to display the user ID of the
authenticated user.
"""

import requests
import sys

if __name__ == "__main__":
    # Check that the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: {} <username> <token>".format(sys.argv[0]))
        sys.exit(1)

    # Get the command line arguments
    username = sys.argv[1]
    token = sys.argv[2]

    # Construct the URL for the authenticated user's information
    url = "https://api.github.com/user"

    # Set the authentication header with the personal access token
    headers = {
        "Authorization": "Basic " + username + ":" + token
    }

    # Make the request to the GitHub API
    response = requests.get(url, headers=headers)

    # If the request was successful, print the user ID
    if response.status_code == 200:
        json_dict = response.json()
        print(json_dict["id"])
    # If the request failed, print an error message
    else:
        print("Error: Request failed with status code {}".format(response.status_code))
        sys.exit(1)
