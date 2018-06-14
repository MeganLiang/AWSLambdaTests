import requests
from timeit import default_timer as timer
from multiprocessing import Process, Pool
import json
import numpy as np
import matplotlib.pyplot as plt
import sys

url = "https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes1024MB"

urls = []
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/Eratosthenes")
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB")
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes512MB")
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes1024MB")

repeat_n = 100
if len(sys.argv) >= 2:
    repeat_n = int(sys.argv[1])
headers = {
    'content-type': "application/json"
}

payload={
    "max": 1000000,
    "loops": 1
}


def http_get_memory(url):
    result = requests.get(url, headers=headers, params=payload)
    return result.text


all_urls = []
for x in range(repeat_n):
    for u in urls:
        all_urls.append(u)
pool = Pool(processes=repeat_n)


start = timer()
results = pool.map(http_get_memory, all_urls)
print('total time')
print(timer() - start)
start_mem = 128
i = 1
memories = []
for result in results:
    print(str(start_mem) + 'MB : ' + str(result))
    j = json.loads(result)
    duration = j['durationSeconds']
    print(duration)
    memories.append(duration)
    if i % repeat_n == 0:
        start_mem = start_mem * 2
    i = i + 1
memories = np.array(memories)
memories_split = np.array_split(memories, 4)

averages = np.mean(memories_split, axis=1)
medians = np.median(memories_split, axis=1)
sd = np.std(memories_split, axis=1)
print('results for memory allocations')
print('averages: ')
print(averages)
print('medians: ')
print(medians)
print('standard deviation:')
print(sd)
# graph
x= np.linspace(128, 1024, 4)
y_avg = averages
y_med = medians
y_sd = sd

# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(3, 1, 1)
plt.plot(x, y_avg)
plt.title('Averages for 128MB, 256MB, 512MB, 1024MB')
plt.ylabel('Duration (Seconds)')
# Set the second subplot as active, and make the second plot.
plt.subplot(3, 1, 2)
plt.plot(x, y_med)
plt.title('Medians for 128MB, 256MB, 512MB, 1024MB')
plt.ylabel('Duration (Seconds)')

plt.subplot(3, 1, 3)
plt.plot(x, y_sd)
plt.title('Standard Deviations for 128MB, 256MB, 512MB, 1024MB')
plt.xlabel('Memory (MB)')
plt.ylabel('Duration (Seconds)')
plt.savefig('memory_concurrent.png', bbox_inches='tight')
plt.clf()

def http_get_loops(url_blob):
    j = json.loads(url_blob)
    params1 = {
        "max": 1000000,
        "loops": j['loops']
    }
    res = requests.get(j['url'], headers=headers, params=params1)
    return res.text

urls = []

loops=[2,3,4,5]
for l in loops:
    for x in range(repeat_n):
        urls.append('{"url": "' + url + '","loops":"' + str(l) + '"}')

pool = Pool(processes=repeat_n)


start = timer()
results = pool.map(http_get_loops, urls)

print('timer')
print(timer() - start)
start_mem = 128
i = 1
memories = []
for result in results:
    print(str(start_mem) + 'MB : ' + str(result))
    j = json.loads(result)
    duration = j['durationSeconds']
    print(duration)
    memories.append(duration)
    if i % repeat_n == 0:
        start_mem = start_mem * 2
    i = i + 1
memories = np.array(memories)
memories_split = np.array_split(memories, 4)

averages = np.mean(memories_split, axis=1)
medians = np.median(memories_split, axis=1)
sd = np.std(memories_split, axis=1)
print('results for loops')
print('averages: ')
print(averages)
print('medians: ')
print(medians)
print('standard deviation:')
print(sd)


x= np.array([2,3,4,5])
y_avg = averages
y_med = medians
y_sd = sd
# y_avg=np.array([1.05308474 ,1.59004421 ,2.13707865, 2.71845544])
# y_med = np.array([1.04524433 ,1.58326695 ,2.1259652  ,2.66435964])
# y_sd = np.array([0.02250633 ,0.02337177, 0.03232937 ,0.2386394 ])
# Set up a subplot grid that has height 2 and width 1,
# and set the first such subplot as active.
plt.subplot(3, 1, 1)
plt.plot(x, y_avg)
plt.title('Averages for 2,3,4,5 loops')
plt.ylabel('Duration (Seconds)')
# Set the second subplot as active, and make the second plot.
plt.subplot(3, 1, 2)
plt.plot(x, y_med)
plt.title('Medians for 2,3,4,5 loops')
plt.ylabel('Duration (Seconds)')

plt.subplot(3, 1, 3)
plt.plot(x, y_sd)
plt.title('Standard Deviation for 2,3,4,5 loops')
plt.xlabel('Number of loops')
plt.ylabel('Duration (Seconds)')
plt.savefig('loop_concurrent.png', bbox_inches='tight')
