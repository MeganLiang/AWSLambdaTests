import requests
import json
from timeit import default_timer as timer

url = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB"
headers = {
    'content-type': "application/json"
}

params={
    "max": 1000000,
    "loops": 1
}
start = timer()
for x in range(100):
    response = requests.get(url, headers=headers, params=params)
    print(str(x) + ':' + str(response.text))
print(timer() - start)