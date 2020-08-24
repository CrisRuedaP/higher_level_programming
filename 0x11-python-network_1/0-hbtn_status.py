#!/usr/bin/python3
""" fetch from given URL """
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        the_page = response.read()
        print("Body response:")
        print("\t- type:", type(the_page))
        print("\t- content:", the_page)
        print("\t- uft8 content:", the_page.decode("utf-8"))
