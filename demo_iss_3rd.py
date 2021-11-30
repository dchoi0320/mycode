#!/usr/bin/env python3
"""
    Accessing APIs, Standard-Style
"""

# standard library
#import urllib.request
#import json

# 3rd party library
import requests

URL = "http://api.open-notify.org/iss-now.json"

def main():
    # resp = urllib.request.urlopen(URL)
    resp = requests.get(URL)
    # got the content of the responde in bytes.  need to change it to a str.  this is due to urllib
    
    final = resp.json()

    print(type(resp))
    print(resp.status_code)
    print(final["iss_position"]["latitude"])

main()