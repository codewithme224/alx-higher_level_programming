#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request to the passed URL"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('utf-8')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as res:
        print(res.read().decode('utf-8'))
