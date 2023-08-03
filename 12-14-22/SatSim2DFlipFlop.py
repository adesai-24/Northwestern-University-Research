# 10/5/22 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib as plt
import random

numSats = 100
numClients = 1000
length = 500
width = 500
height = 500
satAngle = 10
clientAngle = 10
time = 1000
interferences = 0
successes = 0
cov = 0
numCompanies = 2
companies = [[.7, 400], [.3, 500]] # company probabilities and heights
satSpreads = [company[1] * math.tan(math.radians(satAngle / 2)) for company in companies] # this calculates the spread of the satellites for each company
clientSpreads = [company[1] * math.tan(math.radians(clientAngle / 2)) for company in companies] # this calculates the spread of the satellites for each companyclientSpread = height * math.tan(math.radians(clientAngle / 2))

np.random.seed(17)

def probability(companies):
    sampleNumbers = np.random.choice(range(numCompanies), 1, p=[company[0] for company in companies])
    return sampleNumbers[0]
    

# np.random.seed(17)

def calculate():
    interferencesTemp = 0
    successesTemp = 0
    noCoverageTemp = 0

    
    if (max(satSpreads) >= max(clientSpreads)):
        numCols = math.ceil(length / max(satSpreads))
        numRows = math.ceil(width/ max(satSpreads))
        satGrid = [[[] for x in range(numRows)] for y in range(numCols)]
        connections = [[0, 0] for _ in range(numClients)]
        for sat in sats:
            satGrid[math.ceil(sat[0]/max(satSpreads))-1][math.ceil(sat[1]/max(satSpreads))-1].append(sat)
        for client in range(len(clients)):
            coords = [(math.ceil(clients[client][0]/max(satSpreads))-1), (math.ceil(clients[client][1]/max(satSpreads))-1)]
            companyClient = clients[client][2]

            checkwith = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                        for sa in satGrid[coords[0] + x][coords[1] + y]:
                            checkwith.append(sa)

            for sat in checkwith:
                companySat = sat[2]
                if (((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (satSpreads[companySat]**2) and ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (clientSpreads[companyClient]**2)):
                    if (companySat == companyClient):
                        connections[client][0] += 1
                    elif (companySat != companyClient):
                        connections[client][1] += 1
            if (connections[client][0] > 0 and connections[client][1] == 0):
                successesTemp += 1
            elif (connections[client][0] == 0):
                noCoverageTemp += 1
    else:
        connections = [[0, 0] for _ in range(numClients)]
        numCols = math.ceil(length / max(clientSpreads))
        numRows = math.ceil(width / max(clientSpreads))
        clientGrid = [[[] for x in range(numRows)] for y in range(numCols)]
        for client in range(len(clients)):
            clientGrid[math.ceil(clients[client][0]/max(clientSpreads))-1][math.ceil(clients[client][1]/max(clientSpreads))-1].append([clients[client][0], clients[client][1], clients[client][2], client])
        for sat in sats:
            coords = [(math.ceil(sat[0]/max(clientSpreads))-1), (math.ceil(sat[1]/max(clientSpreads))-1)]
            companyS = sat[2]

            checkwith = []
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                        for cl in clientGrid[coords[0] + x][coords[1] + y]:
                            checkwith.append(cl)

            for client in checkwith:
                companyC = client[2]
                if ((client[0] - sat[0])**2) + ((client[1] - sat[1])**2) <= (clientSpreads[companyC]**2):
                    if ((client[0] - sat[0])**2) + ((client[1] - sat[1])**2) <= (satSpreads[companyS]**2):
                        if (companyS == companyC):
                            connections[client[3]][0] += 1
                        elif (companyS != companyC):
                            connections[client[3]][1] += 1

        for connection in connections:
            if (connection[0] > 0 and connection[1] == 0):
                successesTemp += 1
            elif (connection[0] == 0):
                noCoverageTemp += 1

    # for connection in connections:
    #     if connection > 1:
    #         interferencesTemp += 1
    #     elif connection == 1:
    #         successesTemp += 1

    return interferencesTemp, successesTemp, noCoverageTemp

for t in range(1, time+1):
    sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width), probability(companies)] for r in range(numSats)]
    clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width), probability(companies)] for r in range(numClients)]
    # True is client 1, False is client 2
    numInterferences, numSuccesses, numCoverage = calculate()
    interferences += numInterferences
    successes += numSuccesses
    cov += numCoverage
    prob = interferences / (t * numClients)
    successRate = successes / (t * numClients)
    coverage = cov / (t * numClients)


# print(checkwith)
# print(satGrid)
print(coverage)
print(successRate) # different because it counts every satellite as on, but in reality they are only on when they have a same company client

# print(sats)
# how many cars can you assign to blocks without a fail?
# if every block had a car in it how many fails would there be?

# coverage graph in 2D
# coverage as angle changes