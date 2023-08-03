# 3/29/23 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(17)

def SatSim(angle, numSats):
    numClients = 100
    length = 500
    width = 500
    height = 100
    satAngle = angle
    clientAngle = angle
    time = 200
    interferences = 0
    successes = 0
    noCoverages = 0
    satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
    clientSpread = height * math.tan(math.radians(clientAngle / 2))

    def calculate(s, c):
        interferencesTemp = 0
        successesTemp = 0
        noCoverageTemp = 0
        connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients
        if (satSpread >= clientSpread):
            numCols = math.ceil(length / satSpread)
            numRows = math.ceil(width/ satSpread)
            satGrid = [[[] for x in range(numRows)] for y in range(numCols)]
            for sat in sats:
                satGrid[math.ceil(sat[0]/satSpread)-1][math.ceil(sat[1]/satSpread)-1].append(sat)
            for client in range(len(clients)):
                coords = [(math.ceil(clients[client][0]/satSpread)-1), (math.ceil(clients[client][1]/satSpread)-1)]

                checkwith = []
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                            for sa in satGrid[coords[0] + x][coords[1] + y]:
                                checkwith.append(sa)

                for sat in checkwith:
                    if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (satSpread**2):
                        if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (clientSpread**2):
                            connections[client] += 1
        else:
            numCols = math.ceil(length / clientSpread)
            numRows = math.ceil(width/ clientSpread)
            clientGrid = [[[] for x in range(numRows)] for y in range(numCols)]
            for client in clients:
                clientGrid[math.ceil(client[0]/clientSpread)-1][math.ceil(client[1]/clientSpread)-1].append(client)
            for sat in sats:
                coords = [(math.ceil(sat[0]/clientSpread)-1), (math.ceil(sat[1]/clientSpread)-1)]

                checkwith = []
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                            for cl in clientGrid[coords[0] + x][coords[1] + y]:
                                checkwith.append(cl)

                for client in checkwith:
                    if ((client[0] - sat[0])**2) + ((client[1] - sat[1])**2) <= (clientSpread**2):
                        if ((client[0] - sat[0])**2) + ((client[1] - sat[1])**2) <= (satSpread**2):
                            for cl in range(len(clients)):
                                if (clients[cl][0] == client[0] and clients[cl][1] == client[1]):
                                    connections[cl] += 1
                                    break

        for connection in connections:
            if connection > 1:
                interferencesTemp += 1
            elif connection == 1:
                successesTemp += 1
            elif connection == 0:
                noCoverageTemp += 1

        return interferencesTemp, successesTemp, noCoverageTemp

    for t in range(1, time+1):
        sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
        clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]
        numInterferences, numSuccesses, numNoCoverages = calculate(sats, clients)
        interferences += numInterferences
        successes += numSuccesses
        noCoverages += numNoCoverages
        prob = interferences / (t * numClients)
        successRate = successes / (t * numClients)
        percentNoCoverage = noCoverages / (t * numClients)

    return successRate

def GoldenSectionSearch(domain, tolerance, numSats):
    domainLength = domain[1] - domain[0]

    while (domainLength > tolerance):
        quarterPts = [domain[0] + (domainLength / 4) * i for i in range(1, 4)]
        curveVals = [SatSim(pt, numSats) for pt in quarterPts]
        maxPt = max(curveVals)
        if (curveVals.index(maxPt) == 0):
            domain[1] -= (domainLength / 2)
        elif(curveVals.index(maxPt) == 1):
            domain[0] += (domainLength / 4)
            domain[1] -= (domainLength / 4)
        else:
            domain[0] += (domainLength / 2)
        
        domainLength = domain[1] - domain[0]

    peak = np.average(domain)
    return peak

def f(x):
    return ((2800 / (x + 20)) + 6)

print("NumSats\tAngle")
for ns in range(20, 150):
    angle = GoldenSectionSearch([f(ns) - 6, f(ns) + 6], .1, ns)
    print(str(ns) + "\t" + str(angle))
