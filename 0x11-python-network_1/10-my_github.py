#!/usr/bin/python3
"""
This module takes GitHub credentials (username and personal access token)
and uses the GitHub API to display the user's id.

Usage: ./10-my_github.py <username> <token>
"""

import sys
import requests


def display_user_id(username: str, token: str) -> None:
    """
    Displays the user's GitHub id by sending a GET request to the
    GitHub API using the provided credentials.

    Args:
        username (str): The GitHub username.
        token (str): The personal access token associated with the
            GitHub account.

    Returns:
        None
    """
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))

    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./10-my_github.py <username> <token>")
        sys.exit(1)

    username = sys.argv[1]
    token = sys.argv[2]
    display_user_id(username, token)
