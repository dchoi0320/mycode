#!/usr/bin/python3
"""
Lab 19 - requests library - Open APIs

- House(s) is returned by the "allegiances" key.
- Books they appear in is BOTH the "books" and "povBooks"!
"""

import requests
import pprint

AOIF = "https://www.anapioficeandfire.com/api"
AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    ## Ask user for input
    got_charToLookup = input("Choose between 1 and 2000 to select a GoT character! " )

    ## Send HTTPS GET to the API of ICE and Fire character resource
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)

    ## Decode the response from JSON to Python
    got_dj = gotresp.json()

    houses = got_dj['allegiances']
    books = got_dj['books']

    for char in got_dj:
        print(f"CHARACTER: {char['name']}")
        print(f"ALLEGIANCES:\n {char['allegiances']}\n")

    #pprint.pprint(got_dj)

if __name__ == "__main__":
    main()
