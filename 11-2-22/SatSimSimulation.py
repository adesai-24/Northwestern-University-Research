# 10/5/22 2D Mega Constellation Simulation by Shaan Doshi and Aadi Desai with guidance from Prof Randall Berry

import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

numSats = 100
numClients = 100
length = 500
width = 500
height = 500
satAngle = 10
clientAngle = 10
time = 1000
interferences = []
frames = [1, 1]
probs = []
satSpread = height * math.tan(math.radians(satAngle / 2)) # this calculates the spread of each satellite 
clientSpread = height * math.tan(math.radians(clientAngle / 2))
numCols = math.ceil(length / satSpread)
numRows = math.ceil(width/ satSpread)

sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]

fig, axs = plt.subplots()

def animate(frameNumber):
    sats = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numSats)]
    clients = [[np.random.uniform(low=0, high=length), np.random.uniform(low=0, high=width)] for r in range(numClients)]

    interferencesTemp = 0
    connections = np.repeat(0, numClients) # the number of connections made between the satellites and the clients
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
            interferencesTemp += 1

    prob = interferencesTemp / (numClients)
    probs.append(prob)
    axs.clear()
    ttl = axs.text(0, 1.05, "Frame Probability: " + str(prob), transform = axs.transAxes, va='center')
    ttl2 = axs.text(.55, 1.05, "Cumulative Probability: " + str(round(np.average(probs), 5)), transform = axs.transAxes, va='center')
    plt.grid()

    axs.scatter([clients[client][0] for client in range(len(clients)) if connections[client] > 1], [clients[client][1] for client in range(len(clients)) if connections[client] > 1], facecolors="red")
    axs.scatter([clients[client][0] for client in range(len(clients)) if connections[client] <= 1], [clients[client][1] for client in range(len(clients)) if connections[client] <= 1], facecolors="blue")
    size = (satSpread)**2
    axs.scatter([sat[0] for sat in sats], [sat[1] for sat in sats], s=size, facecolors='none', edgecolors="orange")

def _blit_draw(self, artists, bg_cache):
    # Handles blitted drawing, which renders only the artists given instead
    # of the entire figure.
    updated_ax = []
    for a in artists:
        # If we haven't cached the background for this axes object, do
        # so now. This might not always be reliable, but it's an attempt
        # to automate the process.
        if a.axes not in bg_cache:
            # bg_cache[a.axes] = a.figure.canvas.copy_from_bbox(a.axes.bbox)
            # change here
            bg_cache[a.axes] = a.figure.canvas.copy_from_bbox(a.axes.figure.bbox)
        a.axes.draw_artist(a)
        updated_ax.append(a.axes)

    # After rendering all the needed artists, blit each axes individually.
    for ax in set(updated_ax):
        # and here
        # ax.figure.canvas.blit(ax.bbox)
        ax.figure.canvas.blit(ax.figure.bbox)
# MONKEY PATCH!!
matplotlib.animation.Animation._blit_draw = _blit_draw

animation = FuncAnimation(fig, animate, interval=75)
plt.show()


# how many cars can you assign to blocks without a fail?
# if every block had a car in it how many fails would there be?
# 398 or 389 Junet