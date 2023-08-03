# 3/8/23 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry
# This file is very similar to the SatSim2DSuccessThreeAngleBump graph, but switches the x-axis with Satellite Denisty we are plotting

import math
import numpy as np
import matplotlib.pyplot as plt

numSats = 50
numClients = 300
length = 500
width = 500
height = 400
time = 400
interferences = 0
successes = 0
satArr50 = []
satArr100 = []
satArr150 = []
satArr300 = []
numAngleArr = []
success = []
satAngle = 5
spread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite


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
    satAngle = 5
    spread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite
    for a in range(25):
        if (b == 1):
            numAngleArr.append(satAngle)
        for t in range(1, time+1):
            sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
            clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]
            numSuccesses = calculate(sats, clients, spread)
            successes += numSuccesses

        satAngle += 1
        spread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite
        successRate = successes / (t * numClients)
        success.append(successRate)
        
        successes = 0
    print(len(success))
    if (numSats == 50):
        satArr50 = success
        numSats = 100
    elif (numSats == 100):
        satArr100 = success
        numSats = 150
    elif (numSats == 150):
        satArr150 = success
        numSats = 300
    elif (numSats == 300):
        satArr300 = success
    sats = []
    clients = []
    


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
axs.set_title("Satellite Angle vs Probability of Successes at Different Satellite Densities (sats=300, l=10000, h=550)")
plt.plot(numAngleArr, satArr50, label="Probability of Success at 50 Satellites")
plt.plot(numAngleArr, satArr100, label="Probability of Success at 100 Satellites")
plt.plot(numAngleArr, satArr150, label="Probability of Success at 150 Satellites")
plt.plot(numAngleArr, satArr300, label="Probability of Success at 300 Satellites")
plt.legend()
plt.show()
# coverage graph in 2D
# coverage as angle changes





