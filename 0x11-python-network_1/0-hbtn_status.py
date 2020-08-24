#!/usr/bin/python3
"""fetch from given URL"""
import urllib.request


if __name__ == "__main__":
    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        html = response.read()
    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
    print("\t- uft8 content:", html.decode("utf8"))
