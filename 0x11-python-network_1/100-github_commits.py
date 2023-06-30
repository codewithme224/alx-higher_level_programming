#!/usr/bin/python3
"""Takes 2 arguments in order to solve this challenge."""


if __name__ == "__main__":
    import requests
    import sys

    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1]))
    for commit in res.json()[0:10]:
        print("{}: {}".format(commit.get('sha'),
              commit.get('commit').get('author').get('name')))
