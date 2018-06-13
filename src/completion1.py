import requests
import json
from timeit import default_timer as timer
import numpy as np
import matplotlib.pyplot as plt

urls = []
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/Eratosthenes")
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes256MB")
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes512MB")
urls.append("https://vtwnqgwbdg.execute-api.us-west-2.amazonaws.com/prod/eratosthenes1024MB")
costperrequest = 0.0000002
costperGB = 0.00001667
repeat_n = 100
headers = {
    'content-type': "application/json"
}
loops = [2,3,4,5]
params={
    "max": 1000000,
    "loops": 1
}

# start = timer()
# memories = []
# for url in urls:
#     one_mem_array = []
#     for x in range(repeat_n):
#         response = requests.get(url, headers=headers, params=params)
#         text_resp = response.text
#         print(str(x) + ':' + str(text_resp))
#         j = json.loads(text_resp)
#         duration = j['durationSeconds']
#         one_mem_array.append(duration)
#     memories.append(one_mem_array)
#     # for x in one_mem_array:
#     #     print(x)
#
# print('total time')
# print(timer() - start)
# memories = np.array(memories)
# averages = np.mean(memories, axis=1)
# medians = np.median(memories, axis=1)
# sd = np.std(memories, axis=1)
# print('averages: ')
# print(averages)
# print('medians: ')
# print(medians)
# print('standard deviation:')
# print(sd)
#
# # cost calc
# start_mem = 128
# for avg in averages:
#     cost = costperrequest + (start_mem/1024 * avg * costperGB)
#     print('cost per call for ' + str(start_mem) + 'MB using average duration '+ str(avg) + ' is $ ' + str(cost))
#     start_mem = start_mem * 2
#
# # graph
# x= np.linspace(128, 1024, 4)
# y_avg = averages
# y_med = medians
# y_sd = sd
#
# # Set up a subplot grid that has height 2 and width 1,
# # and set the first such subplot as active.
# plt.subplot(3, 1, 1)
# plt.plot(x, y_avg)
# plt.title('Averages for 128MB, 256MB, 512MB, 1024MB')
# plt.ylabel('Duration (Seconds)')
# # Set the second subplot as active, and make the second plot.
# plt.subplot(3, 1, 2)
# plt.plot(x, y_med)
# plt.title('Medians for 128MB, 256MB, 512MB, 1024MB')
# plt.ylabel('Duration (Seconds)')
#
# plt.subplot(3, 1, 3)
# plt.plot(x, y_sd)
# plt.title('Standard Deviations for 128MB, 256MB, 512MB, 1024MB')
# plt.xlabel('Memory (MB)')
# plt.ylabel('Duration (Seconds)')
# plt.savefig('memory_rerun.png', bbox_inches='tight')
# plt.show()



start = timer()
memories = []
loops = [2,3,4,5]
for loop in loops:
    one_mem_array = []
    print('loop: ' + str(loop))
    for x in range(repeat_n):
        params={
            "max": 1000000,
            "loops": loop
        }
        response = requests.get(urls[3], headers=headers, params=params)
        text_resp = response.text
        print(str(x) + ':' + str(text_resp))
        j = json.loads(text_resp)
        duration = j['durationSeconds']
        one_mem_array.append(duration)
    memories.append(one_mem_array)
    for x in one_mem_array:
        print(x)

print(timer() - start)
memories = np.array(memories)
# averages = np.array([1.05308474, 1.59004421, 2.13707865, 2.71845544])
# medians = np.array([1.05308474, 1.59004421, 2.13707865,2.71845544])
# sd = np.array([0.02250633, 0.02337177, 0.03232937, 0.2386394 ])
averages = np.mean(memories, axis=1)
medians = np.median(memories, axis=1)
sd = np.std(memories, axis=1)
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
plt.savefig('loops_rerun.png', bbox_inches='tight')
plt.show()


