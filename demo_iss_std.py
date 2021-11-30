#!/usr/bin/env python3
"""
    Accessing APIs, Standard-Style
"""

# standard library
import urllib.request
import json

URL = "http://api.open-notify.org/iss-now.json"

def main():
    resp = urllib.request.urlopen(URL)

    # got the content of the responde in bytes.  need to change it to a str.  this is due to urllib
    resp = resp.read()
    
    #print(type(resp))

    print(resp.decode("utf-8"))

    jsonstr = resp.decode("utf-8")
    final = json.loads(jsonstr)

    #print(final)
    print(final["iss_position"]["latitude"])
    print(type(final))

main()