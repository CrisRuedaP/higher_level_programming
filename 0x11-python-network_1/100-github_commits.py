#!/usr/bin/python3
"""list 10 commits from the most recent to oldest"""
import requests
from sys import argv


if __name__ == '__main__':
    repo = argv[1]
    owner = argv[2]
    params = {'per_page': 10}
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(owner, repo), params=params)
    r = r.json()
    for arg in r:
        print("{}: {}".format(arg.get('sha'),
                              arg.get('commit').get('author').get('name')))
