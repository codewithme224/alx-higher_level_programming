#!/usr/bin/python3
"""Module for stdin metrics"""
import sys


if __name__ == "__main__":
    size = 0
    status_codes = {"200": 0, "301": 0, "400": 0, "401": 0,
                    "403": 0, "404": 0, "405": 0, "500": 0}
    count = 0
    try:
        for line in sys.stdin:
            if count == 10:
                print("File size: {}".format(size))
                for k, v in sorted(status_codes.items()):
                    if v != 0:
                        print("{}: {}".format(k, v))
                count = 0
            count += 1
            try:
                size += int(line.split()[-1])
                status_codes[line.split()[-2]] += 1
            except ValueError:
                pass
    except KeyboardInterrupt:
        print("File size: {}".format(size))
        for k, v in sorted(status_codes.items()):
            if v != 0:
                print("{}: {}".format(k, v))
        raise
    print("File size: {}".format(size))
    for k, v in sorted(status_codes.items()):
        if v != 0:
            print("{}: {}".format(k, v))
