# 10/5/22 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib.pyplot as plt

numSats = 100
numClients = 2
length = 500
width = 500
height = 500
satAngle = 10
clientAngle = 10
time = 400
interferences = 0

numClientsArr = []
probArr = []

satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
clientSpread = height * math.tan(math.radians(clientAngle / 2)) 

for a in range(100):
    for t in range(1, time+1):
        sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
        clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]

        # clients = np.sort([[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)], axis=0)

        # clientX = np.sort(np.random.uniform(low=0, high=length, size=numClients))
        # clientY = np.random.uniform(low=0, high=width, size=numClients)
        # clients = [[clientX[r], clientY[r]] for r in range(numClients)]

        connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients

        for sat in sats:
            for client in range(len(clients)):
                if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (satSpread**2):
                    connections[client] += 1

        for connection in connections:
            if connection > 1:
                interferences += 1
        
        prob = (interferences / (t * numClients))
    
    numClientsArr.append(numClients)
    probArr.append(prob)
    print(prob)
    numClients += 3
    connections = []
    interferences = 0

fig, axs = plt.subplots()
axs.set_xlabel("Number of Clients")
axs.set_ylabel("Probability")
axs.set_title("Clients vs Probability of Interferences (s=100)")
plt.plot(numClientsArr, probArr)
plt.show()




    
