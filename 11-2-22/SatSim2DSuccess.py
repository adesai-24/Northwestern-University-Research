# 10/5/22 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib.pyplot as plt

numSats = 1
numClients = 100
length = 500
width = 500
height = 500
satAngle = 10
clientAngle = 10
time = 10
interferences = 0
successes = 0
interArr = []
successArr = []
numSatsArr = []
satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
clientSpread = height * math.tan(math.radians(clientAngle / 2))
numCols = math.ceil(length / satSpread)
numRows = math.ceil(width/ satSpread)

np.random.seed(17)

def calculate(s, c):
    
    interferencesTemp = 0
    successesTemp = 0
    connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients
    satGrid = [[[] for x in range(numRows)] for y in range(numCols)]
    for sat in sats:
        satGrid[math.ceil(sat[0]/satSpread)-1][math.ceil(sat[1]/satSpread)-1].append(sat)
    for client in range(len(clients)):
        coords = [(math.ceil(clients[client][0]/satSpread)-1), (math.ceil(clients[client][1]/satSpread)-1)]

        checkwith = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                    for s in satGrid[coords[0] + x][coords[1] + y]:
                        checkwith.append(s)

        for sat in checkwith:
            if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (satSpread**2):
                connections[client] += 1

    for connection in connections:
        if connection > 1:
            interferencesTemp += 1
        elif connection == 1:
            successesTemp += 1

    
    return interferencesTemp, successesTemp

for a in range(150):
    numSatsArr.append(numSats)
    for t in range(1, time+1):
        sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
        clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]
        numInterferences, numSuccesses = calculate(sats, clients)

        interferences += numInterferences
        successes += numSuccesses
    numSats += 2
    prob = interferences / (t * numClients)
    successRate = successes / (t * numClients)
    interArr.append(prob)
    successArr.append(successRate)
    interferences = 0
    successes = 0  


# print(checkwith)
# print(satGrid)
# print(prob)
# print(successRate)
# how many cars can you assign to blocks without a fail?
# if every block had a car in it how many fails would there be?

fig, axs = plt.subplots()
axs.set_xlabel("Number of Satellites")
axs.set_ylabel("Probability")
axs.set_title("Satellites vs Probability of Interferences and Success (sats=300, l=10000, h=550)")
plt.plot(numSatsArr, interArr, label="Probability of Interference")
plt.plot(numSatsArr, successArr, label="Probability of Client not having coverage")
plt.legend()
plt.show()
# coverage graph in 2D
# coverage as angle changes