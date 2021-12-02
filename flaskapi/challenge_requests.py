# CH-31 - lab31
 
import requests

counter = 1

for num in range(51):
    x= requests.get("http://0.0.0.0:2224/fast").text
    print(f"Request {counter}: {x}")
    counter += 1