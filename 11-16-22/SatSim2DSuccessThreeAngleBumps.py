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
time = 4
interferences = 0
successes = 0
successArr5 = []
successArr10 = []
successArr15 = []
successArr20 = []
numSatsArr = []
success = []
coneAngle = 5
spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite

def calculate(s, c, sp):
    numCols = math.ceil(length / sp)
    numRows = math.ceil(width / sp)
    successesTemp = 0
    connections = 0
    connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients
    satGrid = []
    satGrid = [[[] for x in range(numRows)] for y in range(numCols)]
    for sat in sats:
        satGrid[math.ceil(sat[0]/sp)-1][math.ceil(sat[1]/sp)-1].append(sat)
    for client in range(len(clients)):
        coords = [(math.ceil(clients[client][0]/sp)-1), (math.ceil(clients[client][1]/sp)-1)]

        checkwith = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                    for s in satGrid[coords[0] + x][coords[1] + y]:
                        checkwith.append(s)

        for sat in checkwith:
            if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (sp**2):
                connections[client] += 1

    for connection in connections:
        if connection == 1:
            successesTemp += 1

    
    return successesTemp

for b in range(4):
    success = []
    numSats = 1
    for a in range(150):
        if (b == 1):
            numSatsArr.append(numSats)
        for t in range(1, time+1):
            sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
            clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]
            numSuccesses = calculate(sats, clients, spread)
            successes += numSuccesses

        numSats += 2
        successRate = successes / (t * numClients)
        success.append(successRate)
        successes = 0
    if (coneAngle == 5):
        successArr5 = success
        coneAngle = 10
        spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite
    elif (coneAngle == 10):
        successArr10 = success
        coneAngle = 15
    elif (coneAngle == 15):
        successArr15 = success
        coneAngle = 20
        spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite
    elif (coneAngle == 20):
        successArr20 = success
    


# print(checkwith)
# print(satGrid)
# how many cars can you assign to blocks without a fail?
# if every block had a car in it how many fails would there be?
# create two graphs (one with regular angle and one with a lesser angle)
# implementing client angles 
# implementing the different companies

fig, axs = plt.subplots()
axs.set_xlabel("Number of Satellites")
axs.set_ylabel("Probability")
axs.set_title("Satellites vs Probability of Successes at Different Satellite Angles (sats=300, l=10000, h=550)")
plt.plot(numSatsArr, successArr5, label="Probability of Success at Satellite Angle 5")
plt.plot(numSatsArr, successArr10, label="Probability of Success at Satellite Angle 10")
plt.plot(numSatsArr, successArr15, label="Probability of Success at Satellite Angle 15")
plt.plot(numSatsArr, successArr20, label="Probability of Success at Satellite Angle 20")
plt.legend()
plt.show()
# coverage graph in 2D
# coverage as angle changes