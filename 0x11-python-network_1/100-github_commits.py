#!/usr/bin/python3
"""This script uses the GitHub API to list the 10 most recent commits of a repository by a user."""

import requests
import sys


def get_commits(repo_name, owner_name):
    """Function to get the 10 most recent commits of a repository by a user."""
    # Set the GitHub API endpoint and parameters
    api_endpoint = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {"per_page": 10}

    # Make a GET request to the API
    response = requests.get(api_endpoint, params=params)

    # Check if the request was successful
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.reason}")
        sys.exit()

    # Get the commits data from the API response
    commits = response.json()

    # Print the commits data
    for commit in commits:
        sha = commit["sha"]
        author_name = commit["commit"]["author"]["name"]
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    # Check if the correct number of command line arguments were provided
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py [repository name] [owner name]")
        sys.exit()

    # Get the repository name and owner name from the command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # Get the 10 most recent commits of the repository by the owner
    get_commits(repo_name, owner_name)
