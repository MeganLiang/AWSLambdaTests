import multiprocessing
import requests
from timeit import default_timer as timer

url = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes128MBAPI"
# url = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes128MB"
headers = {
    'content-type': "application/json",
    'x-api-key': '9dkNN2ZSsoacVWr6Q5wok40dWWzVIg1I2NlYRAQ6'

# "X-Amz-Invocation-Type": "Event",
    # 'Invocation-Type': 'Event',
    # 'integration.request.header.X-Amz-Invocation-Type': 'Event',
    # 'integration.request.header.X-Amz-Invocation-Type': 'Event'
}

payload={
    "max": 1000000,
    "loops": 1
}

# pool = ThreadPoolExecutor(5)
#
# futs = []
# start = timer()
# print(multiprocessing.cpu_count()-1)
# p = multiprocessing.Pool(processes = multiprocessing.cpu_count()-1)
#
# for x in range(5):
#
#     p.map(requests.get(url, headers=headers, params=payload))
# #     result = requests.get(url, headers=headers, params=payload)
# #     future = pool.submit(result, ("hello"))
# #     futs.append(result)
#
# #     results = [fut.text for fut in futs]
# #
# # print(futs)
# print(timer() - start)

from multiprocessing import Process, Pool
import time
import numpy as np


def http_get(url):
    result = requests.get(url, headers=headers, params=payload)
    return result.text


urls = []
for x in range(2):
    urls.append(url)
pool = Pool(processes=2)


start = timer()
results = pool.map(http_get, urls)

print('timer')
print(timer() - start)
for result in results:
    print (result)

