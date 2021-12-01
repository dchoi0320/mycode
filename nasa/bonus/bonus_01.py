#!//usr/bin/python3

# https://github.com/csfeeser/Python/blob/master/challenges/API%20CHALLENGE%20INTO-%20ISS.md
# bonus

import requests
#import json

ISS = "http://api.open-notify.org/iss-now.json"

def main():
    location = requests.get(ISS)

    current = location.json()

    #print(f"Current Location:\n{current}")
    print(f"CURRENT LOCATION OF THE ISS:")
    print(f"Lon: {current['iss_position']['longitude']}")
    print(f"Lat: {current['iss_position']['latitude']}\n")

if __name__ == "__main__":
    main()