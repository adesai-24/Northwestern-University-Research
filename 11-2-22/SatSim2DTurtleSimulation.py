# 10/5/22 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import turtle
import math
import numpy as np
import matplotlib as plt
import random
import time as z
wn = turtle.Screen()

wn.tracer(0)

turtle.speed(0)

numSats = 100
numClients = 100
length = 500
width = 600
height = 500
satAngle = 10
clientAngle = 10
time = 1000
interferences = 0

np.random.seed(17)

wn.screensize(width, height, "white")
wn.setworldcoordinates(0, 0, 700, 600)

def circle(xStart, yStart, radius):
    turtle.hideturtle()
    wn.tracer(0)
    turtle.penup()
    turtle.setposition(xStart, yStart)
    turtle.pendown()
    turtle.circle(radius)

def dot(xStart, yStart):
    turtle.hideturtle()
    wn.tracer(0)
    turtle.penup()
    turtle.setposition(xStart, yStart)
    turtle.pendown()
    turtle.dot()

satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
clientSpread = height * math.tan(math.radians(clientAngle / 2)) 

for t in range(1, time+1):
    sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
    clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]
    connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients

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
                    for s in satGrid[coords[0] + x][coords[1] + y]:
                        checkwith.append(s)

        for sat in checkwith:
            if ((sat[0] - clients[client][0])**2) + ((sat[1] - clients[client][1])**2) <= (satSpread**2):
                connections[client] += 1

    for connection in connections:
        if connection > 1:
            interferences += 1

    prob = (interferences / (t * numClients))

    for sat in sats:
        xS = sat[0]
        yS = sat[1]
        circle(xS, yS, satSpread)

    for client in clients:
        xC = client[0]
        yC = client[1]
        dot(xC, yC)
    wn.update()
    z.sleep(1)
    wn.clear()  

    

# print(checkwith)
# print(satGrid)

wn.mainloop()


# how many cars can you assign to blocks without a fail?
# if every block had a car in it how many fails would there be?