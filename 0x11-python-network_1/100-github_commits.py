#!/usr/bin/python3
"""Write a python script that;
uses the GitHub API to list the 10 most recent commits of a repository by a user."""
import requests
import sys

if __name__ == "__main__":
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(url)
    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
