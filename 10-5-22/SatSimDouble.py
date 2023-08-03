# 9/14/22 - Simulation Created by Aadi Desai and Shaan Doshi on behalf of Dr. Randall Berry

from http import client
import numpy as np
import matplotlib.pyplot as plt
import math

numSats = 100 # number of satellites in an array
numClients = 100 # number of clients in an array
length = 10000 # total length spacing for satellites and clients in kilometers
height = 550 # how high the satellites are above the ground in kilometers
time = 1000 # the number of times the simulation runs
satAngle = 10 # angle of satellite signal spread
clientAngle = 1 

sats = np.array([])
clients = np.array([])
ratioArr = []
angleArr = []

satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 


for n in range(20):
    interferences = 0 # the number of times a client is included into two spreads of a satellite
    clientSpread = height * math.tan(math.radians(clientAngle / 2)) # this calculates the spread of each satellite 
    for p in range(time):

        sats = np.sort(np.random.uniform(low=0, high=length, size=(numSats))) # this randomizes the numbers in satellite array
        clients = np.sort(np.random.uniform(low = 0, high = length, size=(numClients))) # this randomizes the numbers in client array

        connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients
        
        for sat in sats:
            start = 0
            for c in range(start, numClients):
                if (clients[c] > (sat + satSpread)):
                    break
                elif (clients[c] < (sat -satSpread)):
                    start = c
                else:
                    if (clients[c] - clientSpread <= sat and clients[c] + clientSpread >= sat):
                        connections[c] += 1

        for connection in connections:
            if (connection > 1):
                interferences += 1

    ratioArr.append(interferences / (time * numClients))
    angleArr.append(clientAngle)
    clientAngle += 1

fig, axs = plt.subplots()
axs.set_xlabel("Angle of client spread")
axs.set_ylabel("Probability of Satellite Interference")
axs.set_title("Number of Clients vs Probability of Interferences (100, 100, l=10000, h=550, sa=10)")
plt.plot(angleArr, ratioArr)
plt.grid(True)
plt.show()

        


    

# find the critical angle for when it doesn't matter anymore for cleints to see all satellites theyd be in a fail with
