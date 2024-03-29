#!/usr/bin/python3
"""Python script that takes 2 arguments in order to solve this challenge.
"""
import sys
import requests


def fetch_commits(repo_name, owner_name):
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    if response.status_code == 200:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit['sha']
            author = commit['commit']['author']['name']
            print(f"{sha}: {author}")
    else:
        print("Failed to retrieve commits.")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        repo_name = sys.argv[1]
        owner_name = sys.argv[2]
        fetch_commits(repo_name, owner_name)
    else:
        print("Usage: python script.py <repository_name> <owner_name>")
