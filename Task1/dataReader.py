import pickle
import json
import numpy as np
import matplotlib.pyplot as plt

# read pkl file to pandas df
rawData = pickle.load(open("data.pkl", "rb"))
onlyTaskData = rawData["task"]

# read json file to dict
with open('names.json') as names_file:
    jsonData = json.load(names_file);


# for storing the repetation number
count_arr = []

# finding the ones and count them to array
ctr = 0
jsonCtr = 1
while ctr < len(onlyTaskData):
    if onlyTaskData[ctr] == 0:
        ctr += 1
        continue
    else :
        localCtr = 0
        while onlyTaskData[ctr] != 0:
                onlyTaskData[ctr] = jsonData[str(jsonCtr)]
                localCtr += 1
                ctr += 1
        jsonCtr += 1
        count_arr.append(localCtr)

# showing them on graph
dictForGraph = {}
for i in range(len(count_arr)):
    dictForGraph[jsonData[str(i+1)]] = count_arr[i]

names = list(dictForGraph.keys())
countedNums = list(dictForGraph.values())

fig = plt.figure(figsize = (30,5))

plt.bar(names, countedNums, color = 'blue', width = 0.5)
plt.xlabel("names")
plt.ylabel("counts")
plt.title("Counts of repetations")
plt.show()
