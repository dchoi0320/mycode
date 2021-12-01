import requests

r = requests.get("http://192.168.98.132:2224/")
r_01= requests.get("http://192.168.98.132:2224/").json
r_02= requests.get("http://192.168.98.132:2224/").text

print(r)
print(r_01)
print(r_02)

"""
import requests
r= requests.get("http://10.11.206.98:2224/slappy").text
print(r)
"""