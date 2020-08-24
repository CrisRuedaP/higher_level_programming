#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the body of the response
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.URLError as e:
        print("Error code: {}".format(e.code))
