# 9/14/22 - Simulation Created by Aadi Desai and Shaan Doshi on behalf of Dr. Randall Berry

import numpy as np
import matplotlib.pyplot as plt
import math

numSats = 1 # number of satellites in an array
numClients = 100 # number of clients in an array
length = 10000 # total length spacing for satellites and clients in kilometers
height = 550 # how high the satellites are above the ground in kilometers
coneAngle = 10 # angle of satellite signal spread
time = 400 # the number of times the simulation runs
interferences = 0 # the number of times a client is included into two spreads of a satellite
difference = 0 # unit of variance
SD = 0 # standard deviation creation
sats = np.array([])
clients = np.array([])
spread = height * math.tan(math.radians(coneAngle / 2)) # this calculates the spread of each satellite 
numSatsArr = []
ratioArr = []
ratioDataSet = []
SDA = [] # the array for holding all standard deviation values
for a in range(20):
    ratioDataSet = []
    numSatsArr.append(numSats)
    difference = 0
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
        ratioDataSet.append(interferences / (numClients))
        interferences = 0
    
    numSats += 50
    
    average = np.average(ratioDataSet)
    ratioArr.append(average)
    for r in ratioDataSet:
        difference += (( r - average) ** 2)/(len(ratioDataSet))
    SD = math.sqrt(difference)
    SDA.append(SD)
    
    
    

print(average)
print(difference)
print(SD)
print(SDA)

print(ratioDataSet)

fig, axs = plt.subplots()
axs.set_xlabel("Number of Satellites")
axs.set_ylabel("Probability of Satellite Interferences")
axs.set_title("Number of Satellites vs Probability of Interferences (clients=100, L=10000, h=550)")
plt.errorbar(numSatsArr, ratioArr, yerr=SDA)
plt.show()