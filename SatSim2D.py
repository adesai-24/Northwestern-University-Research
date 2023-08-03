# 3/8/23 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib.pyplot as plt

numSats = 100
numClients = 100
length = 500 # how far across the simulation is (X axis)
width = 500 # how far deep the simulation is (Y axis)
satAngle = 10 # the angle that satellites' signals spread out at
clientAngle = 10 # the angle that clients' signals spread out at 
time = 400 # the time the simulation repeats in order to gain accuracy
companies = [[1, 400]] # company probabilities and heights
numCompanies = len(companies)
companyClientSizes = [0 for _ in range(numCompanies)]
results = [{"success": 0, "interference": 0, "noCoverage": 0} for _ in range(numCompanies)]
satSpreads = [company[1] * math.tan(math.radians(satAngle / 2)) for company in companies] # this calculates the spread of the satellites for each company
clientSpreads = [company[1] * math.tan(math.radians(clientAngle / 2)) for company in companies] # this calculates the spread of the clients for each company when they hit satellites of their own company
maxSpread = np.max(np.concatenate((satSpreads, clientSpreads))) # the maximum spread in the simulation (used for creating the grid size)

# np.random.seed(17)

def determineCompany(companies, isClient):
    sampleNumbers = np.random.choice(range(numCompanies), 1, p=[company[0] for company in companies])
    if (isClient):
        companyClientSizes[sampleNumbers[0]] += 1
    return sampleNumbers[0] # returns a random company based on the probabilities given. You take the 0th element because its an array with only one value

def deleteSats(): # this deletes the satellites that do not have a client in the same company within range (they are turned off then and don't do anything)
    satConns = [[0, 0] for _ in range(numSats)] # index 0 is number same-company clients each satellite is connected to, index 1 is not the same company
    numCols = math.ceil(length / maxSpread) # the length of each column is max spread, and the total length is length, so you divide them and round up to get the number of columns
    numRows = math.ceil(width / maxSpread) # same as numCols but with width
    clientGrid = [[[] for x in range(numRows)] for y in range(numCols)] # the 2D array that represents the grid
    for client in range(len(clients)):
        clientGrid[math.ceil(clients[client][0]/maxSpread)-1][math.ceil(clients[client][1]/maxSpread)-1].append([clients[client][0], clients[client][1], clients[client][2], client])
        # the above line adds each client to the grid based on its x and y values. It also appends its index so that it isn't lost when you look at checkwith
    for sat in range(len(sats)): # you now look at every satellite and its neighboring clients to determine its connections
        coords = [(math.ceil(sats[sat][0]/maxSpread)-1), (math.ceil(sats[sat][1]/maxSpread)-1)] # the coordinates of the satellite in terms of the grid
        companyS = sats[sat][2] # the satellite's company

        checkwith = [] # the array of all nearby clients to the satellite, using the grid
        for x in range(-1, 2):
            for y in range(-1, 2): # this gives you everything nearby with an x and y of +- 1 away in the grid, since the grid is sized so anything you can see would be next door
                if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows): # checks for edge out of bounds errors
                    for cl in clientGrid[coords[0] + x][coords[1] + y]:
                        checkwith.append(cl) # adds each client thats neighboring the satellite in the grid

        for client in checkwith: # iterates through so youre comparing oen satellite to one nearby client
            companyC = client[2]
            if ((client[0] - sats[sat][0])**2) + ((client[1] - sats[sat][1])**2) <= (clientSpreads[companyC]**2): # if in range of the clientspread
                if ((client[0] - sats[sat][0])**2) + ((client[1] - sats[sat][1])**2) <= (satSpreads[companyS]**2): # if in range of the satspread
                    if (companyS == companyC):
                        satConns[sat][0] += 1 # if theyre the same company, you add to index 0
                    elif (companyS != companyC):
                        satConns[sat][1] += 1 # if theyre differeont companies, you add to index 1
    shift = 0
    for sat in range(len(satConns)): # this deletes every satellite that has no same-company connections becaucse its turned off then
        if (satConns[sat][0] == 0):
            sats.pop(sat-shift) # you have to use shift because it moves over the index every time you delete
            shift += 1

    return sats

def calculate(): # same grid placing code as above, just for satellites in the grid and checkwith for every client
    results = [{"success": 0, "interference": 0, "noCoverage": 0} for _ in range(numCompanies)]
    
    numCols = math.ceil(length / maxSpread)
    numRows = math.ceil(width / maxSpread)
    satGrid = [[[] for x in range(numRows)] for y in range(numCols)]
    connections = [[0, 0] for _ in range(numClients)]
    for sat in sats:
        satGrid[math.ceil(sat[0]/maxSpread)-1][math.ceil(sat[1]/maxSpread)-1].append(sat)
    for client in range(len(clients)):
        coords = [(math.ceil(clients[client][0]/maxSpread)-1), (math.ceil(clients[client][1]/maxSpread)-1)]
        companyClient = clients[client][2]

        checkwith = []
        for x in range(-1, 2):
            for y in range(-1, 2):
                if (coords[0] + x >= 0 and coords[0] + x < numCols and coords[1] + y >= 0 and coords[1] + y < numRows):
                    for sa in satGrid[coords[0] + x][coords[1] + y]:
                        checkwith.append(sa)

        for sat in checkwith:
            companySat = sat[2]
            if (((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (satSpreads[sat[2]]**2)):
                if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (clientSpreads[clients[client][2]]**2):
                    if (companySat == companyClient):
                        connections[client][0] += 1
                    elif (companySat != companyClient):
                        connections[client][1] += 1
    for connection in range(len(connections)):
        companyClient2 = clients[connection][2]
        if (connections[connection][0] > 0 and connections[connection][1] == 0): # if you have same-company connections and nothing else, its a success
            results[companyClient2]["success"] += 1
        elif (connections[connection][0] == 0): # if you have no same company connections, you are out of coverage
            results[companyClient2]["noCoverage"] += 1
        elif (connections[connection][0] > 0 and connections[connection][1] > 0): # if you have same company and outside connections, you're in an interference
            results[companyClient2]["interference"] += 1
    return results 

for t in range(1, time+1):
    sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width), (determineCompany(companies, False))] for r in range(numSats)]
    clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width), (determineCompany(companies, True))] for r in range(numClients)]
    sats = deleteSats() # deletes the sats and returns new clients array
    # format for sats and clients: [x, y, company]
    resultsTemp = calculate()
    for t in range(len(resultsTemp)):
        results[t]["success"] += resultsTemp[t]["success"]
        results[t]["interference"] += resultsTemp[t]["interference"]
        results[t]["noCoverage"] += resultsTemp[t]["noCoverage"]

for g in range(len(results)):
    results[g]["success"] /= companyClientSizes[g]
    results[g]["interference"] /= companyClientSizes[g]
    results[g]["noCoverage"] /= companyClientSizes[g]

for a in range(len(results)):
    print("COMPANY")
    print("Interference:", results[a]["interference"])
    print("No Coverage:", results[a]["noCoverage"])
    print("Success:", results[a]["success"])