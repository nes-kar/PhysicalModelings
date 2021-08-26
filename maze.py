import numpy as np
import matplotlib.pyplot as plt
import random

width = 80
heigth = 80

dots = np.arange(width*heigth).reshape(heigth, width)

verticalProb = 0.4 # Probability of formation of a wall between two consecutive vertical nodes
horizontalProb = 0.5

verticalWalls = []
horizontalWalls = []

def vertical(dots):
    for rows in dots:
        for i in rows:
            if list(rows).index(i) + 1 < width: # For end points
                prob = random.random()
                if prob > 1 - verticalProb:
                    verticalWalls.append((i, i+1))

def horizontal(dots):
    for rows in dots:
        for i in rows:
            if i < len(dots.flatten()) - width: # For last row
                prob = random.random()
                if prob > 1 - horizontalProb:
                    horizontalWalls.append((i, i+heigth))

vertical(dots)
horizontal(dots)

def n2Coords(t, matrix): # use np.meshgrid?
    a, b = t
    x = np.where(matrix == a)
    y = np.where(matrix == b)
    coords = [list(zip(x[0], x[1])),  list(zip(y[0], y[1]))]
    return coords

verticals = []

plt.figure(facecolor="black")
ax = plt.axes()
ax.set_aspect("equal")
ax.set_facecolor("black")
ax.axis("off")

for wall in verticalWalls:
    verticals.append(n2Coords(wall, dots))

for wall in verticals:
    ax.plot([wall[0][0][0], wall[1][0][0]], [wall[0][0][1], wall[1][0][1]], "w")

horizontals = []
for wall in horizontalWalls:
    horizontals.append(n2Coords(wall, dots))

for wall in horizontals:
    ax.plot([wall[0][0][0], wall[1][0][0]], [wall[0][0][1], wall[1][0][1]], "w")

plt.show()

