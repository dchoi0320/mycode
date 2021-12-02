#!/usr/bin/env python3
"""how to use the requests module to send a POST"""
import requests

url = "http://192.168.98.132:2224/post"

chadfavs = {
        "name": "Chad",
        "ice cream": "coffee",
        "color": "red"
}

davidfavs = {
        "name": "David",
        "ice cream": "tea",
        "color": "blue"
}

requests.post(url, json=chadfavs)
