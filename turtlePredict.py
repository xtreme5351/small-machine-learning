import matplotlib.pyplot as plt
# import numpy as np
import turtle
import random
totalAng = []
totalLst = []
totalErrorA = []
totalErrorD = []
ang = []
lst = []
n = 0
# was too slow before, and now it isnt
turtle.speed(100)

# total angle
def tang(ang):
    return sum(ang)

# total sum of list
def tlst(lst):
    return sum(lst)


def avg(lst):
    return sum(lst) / len(lst)


def angle(ang):
    return sum(ang) / len(ang)


# predicted distance of movement (self-made algorithim)
def prdy(totalL, totalA, average, avgDist):
    return (totalA / totalL - 3.1) + ((1 + avgDist / average) * avgDist) * (1 - avgDist / average)


# predicted angle of movement (self-made algorithim)
def prdx(totalL, totalA, average, avgDist):
    return (190 - (10 * (totalA / totalL))) + ((1 + avgDist / average) * avgDist) * (1 - avgDist / average)


# n = number of times the code will run, the more it runs, the more accurate the result
while n < 1000:
    a = random.randint(1, 360)
    d = random.randint(1, 75)
    turtle.right(a)
    turtle.fd(d)

    totalAng.append(a)
    ang.append(a)
    lst.append(d)
    avgDist = avg(lst)
    average = avg(ang)
    #spaceholders to make console output easier to read
    print("======")
    print("Average dist: " + str(round(avgDist, 4)) + " Average angle: " + str(round(average, 4)))

    totalL = tlst(lst)
    totalA = tang(ang)
    initalPy = prdy(totalL, totalA, average, avgDist)
    initialPx = prdx(totalL, totalA, average, avgDist)
    print("Predicted Angle: " + str(round(initialPx, 4)))
    print("Predicted Dist: " + str(round(initalPy, 4)))

    errorA = (a - initialPx) / a
    errorD = (d - initalPy) / d
    totalErrorA.append(errorA)
    totalErrorD.append(errorD)
    print("Angular error: ", round(errorA, 4))
    print("Distance error: ", round(errorD, 4))
    totalLst.append(d)
    n += 1

average = angle(ang)
avgDist = avg(lst)
totalL = tlst(lst)
totalA = tang(ang)
py = prdy(totalL, totalA, average, avgDist)
px = prdx(totalL, totalA, average, avgDist)


print("Total Dist: " + str(round(totalL, 4)) + " Total Angle: " + str(round(totalA, 4)))
print("Final predicted Angle of movement: " + str(round(px, 4)))
print("Final predicted Distance of movement: " + str(round(py, 4)))
print("Avg angle error: ", round(avg(totalErrorA), 4))
print("Avg dist error: ", round(avg(totalErrorD), 4))

x = ang
y = lst

plt.scatter(x, y, marker='*', s=10)
plt.legend()
plt.show()
