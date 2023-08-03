# 9/14/22 - Simulation Created by Aadi Desai and Shaan Doshi on behalf of Dr. Randall Berry

import numpy as np
import matplotlib.pyplot as plt
import math

numSats = 100 # number of satellites in an array
numClients = 100 # number of clients in an array
length = 10000 # total length spacing for satellites and clients in kilometers
height = 550 # how high the satellites are above the ground in kilometers
coneAngle = 10 # angle of satellite signal spread
time = 400 # the number of times the simulation runs
interferences = 0 # the number of times a client is included into two spreads of a satellite
difference = 0
SD = 0
sats = np.array([])
clients = np.array([])
ratio = []
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
    
#     ratio.append(interferences / numClients)
#     interferences = 0
# average = np.average(ratio)
# for r in ratio:
#     difference += (( r - average) ** 2)/(len(ratio))
# SD = math.sqrt(difference)
# print(average)
# print(difference)
# print(SD)


print(interferences / (time * numClients))

# look at sqrt (stdev) relative to the mean
# point at average then error bars using stdev
# https://matplotlib.org/stable/gallery/lines_bars_and_markers/errorbar_limits_simple.html#sphx-glr-gallery-lines-bars-and-markers-errorbar-limits-simple-py
# https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/monte-carlo-methods-mathematical-foundations/variance-and-standard-deviation
# find the critical angle for when it doesn't matter anymore for cleints to see all satellites theyd be in a fail with
