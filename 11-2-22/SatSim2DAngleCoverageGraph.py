# 10/5/22 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib.pyplot as plt

numSats = 100
numClients = 100
length = 500
width = 500
height = 500
satAngle = 1
clientAngle = 10
time = 400
interferences = 0
transmits = 0
satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
clientSpread = height * math.tan(math.radians(clientAngle / 2))
numCols = math.ceil(length / satSpread)
numRows = math.ceil(width/ satSpread)

angleArr = []
ratioArr = []
coverageArr = []

satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
clientSpread = height * math.tan(math.radians(clientAngle / 2)) 

for a in range(20):
    for t in range(1, time+1):
        sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
        clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]
        connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients

        numCols = math.ceil(length / satSpread)
        numRows = math.ceil(width/ satSpread)
        satGrid = [[[] for x in range(numCols)] for x in range(numRows)]
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
                interferences += 1
            if connection == 0:
                transmits += 1

    prob = (interferences / (t * numClients))
    noCov = (transmits / (t * numClients))
    angleArr.append(satAngle)
    ratioArr.append(prob)
    coverageArr.append(noCov)
    satAngle += 1
    satSpread = height * math.tan(math.radians(satAngle / 2))
    interferences = 0
    transmits = 0


fig, axs = plt.subplots()
axs.set_xlabel("Satellite Angle")
axs.set_ylabel("Probability")
axs.set_title("Angle vs probablity of interferences and no coverage (c=100)")
plt.plot(angleArr, ratioArr, label="Probability of Interference")
plt.plot(angleArr, coverageArr, label="Probability of no coverage")
plt.legend()
plt.show()



# coverage graph in 2D
