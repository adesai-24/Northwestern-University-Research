# 9/14/22 - Simulation Created by Aadi Desai and Shaan Doshi on behalf of Dr. Randall Berry

import numpy as np
import matplotlib.pyplot as plt
import math

length = 10000 # total length spacing for satellites and clients in kilometers
height = 550 # how high the satellites are above the ground in kilometers
coneAngle = 5 # angle of satellite signal spread
spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite
time = 400 # the number of times the simulation runs
covs = 0 # 
interferences = 0 # the number of times a client is included into two spreads of a satellite
sats = np.array([])
clients = np.array([])
numSatsArr = []
ratioArr5 = []
ratioArr10 = []
ratioArr20 = []
coverageArr5 = []
coverageArr10 = []
coverageArr20 = []
numSats = 10 # number of satellites in an array
numClients = 100 # number of clients in an array
interferences = 0 # the number of times a client is included into two spreads of a satellite
for b in range(3):
    array = []
    cov = []
    numSats = 10
    for x in range(40):
        interferences = 0
        covs = 0
        if (b == 1):
            numSatsArr.append(numSats)
        for p in range(time):
            sats = np.sort(np.random.uniform(low = 0, high = length, size=(numSats))) # this randomizes the numbers in satellite array
            clients = np.sort(np.random.uniform(low = 0, high = length, size=(numClients))) # this randomizes the numbers in client array
            connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients
            for sat in sats:
                start = 0
                for c in range(start, numClients):
                    if (clients[c] > (sat + spread)):
                        break
                    elif (clients[c] < (sat - spread)):
                        start = c
                    else:
                        connections[c] += 1
            for connection in connections:
                if (connection > 1):
                    interferences += 1
                elif (connection == 0):
                    covs += 1
        ratio = interferences / (time * numClients) 
        coverage = covs / (time * numClients)       
        numSats += 25
        array.append(ratio)
        cov.append(coverage)
    if (coneAngle == 5):
        ratioArr5 = array
        coverageArr5 = cov
        coneAngle = 10
        spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite
    elif (coneAngle == 10):
        ratioArr10 = array
        coverageArr10 = cov
        coneAngle = 20
        spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite
    elif (coneAngle == 20):
        ratioArr20 = array
        coverageArr20 = cov
fig, axs = plt.subplots()
axs.set_xlabel("Number of Satellites")
axs.set_ylabel("Probability of interferences to number of Satellites")
axs.set_title("Satellites vs Probability of Interferences/Coverage fails at different ConeAngles (sats=100, l=10000, h=550)")
plt.plot(numSatsArr, ratioArr5, label="Probability of interference at ConeAngle 5", color = 'red')
plt.plot(numSatsArr, coverageArr5, label="Probability of Client not having coverage at ConeAngle 5", color = 'red')
plt.plot(numSatsArr, ratioArr10, label="Probability of interference at ConeAngle 10", color = 'blue')
plt.plot(numSatsArr, coverageArr10, label="Probability of Client not having coverage at ConeAngle 10", color = 'blue')
plt.plot(numSatsArr, ratioArr20, label="Probability of interference at ConeAngle 20", color = 'black')
plt.plot(numSatsArr, coverageArr20, label="Probability of Client not having coverage at ConeAngle 20", color = 'black')
plt.legend(loc = 'lower right', title = 'Legend')
plt.show()


