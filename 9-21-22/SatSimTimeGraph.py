# 9/14/22 - Simulation Created by Aadi Desai and Shaan Doshi on behalf of Dr. Randall Berry

import numpy as np
import matplotlib.pyplot as plt
import math

numSats = 100 # number of satellites in an array
numClients = 100 # number of clients in an array
length = 10000 # total length spacing for satellites and clients in kilometers
height = 550 # how high the satellites are above the ground in kilometers
coneAngle = 10 # angle of satellite signal spread
time = 1000 # the number of times the simulation runs 400 has been determined as the minimum amount you need to run the simulation
interferences = 0 # the number of times a client is included into two spreads of a satellite
sats = np.array([])
clients = np.array([])

ratioArr = []

spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite 

for p in range(time):

    sats = np.sort(np.random.uniform(low=0, high=length, size=(numSats))) # this randomizes the numbers in satellite array
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

    ratio = interferences / ((p+1) * numClients)
    if (p >= 50):
        ratioArr.append(ratio)

ratioArr = [abs(rat - ratioArr[-1]) for rat in ratioArr]


fig, axs = plt.subplots()
axs.set_xlabel("Number of times ran")
axs.set_ylabel("Difference from final probability")
axs.set_title("Convergence of probability (100x100)")
plt.plot(np.arange(51, time+1), ratioArr)
plt.grid(True)
plt.show()