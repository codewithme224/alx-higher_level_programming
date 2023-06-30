#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays the value"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
