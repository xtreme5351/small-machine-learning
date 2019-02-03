import matplotlib.pyplot as plt
# import numpy as np
import turtle
import random
totalAng = []
totalLst = []
ang = []
lst = []
n = 0


def tang(ang):
    return  sum(ang)


def tlst(lst):
    return sum(lst)


def avg(lst):
    return sum(lst) / len(lst)


def angle(ang):
    return sum(ang) / len(ang)


while n < 50:
    a = random.randint(1, 360)
    d = random.randint(1, 75)
    turtle.right(a)
    turtle.fd(d)
    totalAng.append(a)
    ang.append(a)
    lst.append(d)
    avgDist = avg(lst)
    average = avg(ang)
    print("Average dist: " + str(round(avgDist, 4)) + " Average angle: " + str(round(average, 4)))
    totalLst.append(d)
    n += 1


def prdy(totalL, totalA, average, avgDist):
    return (totalA / totalL - 3.1) + ((1 + avgDist / average) * avgDist) * (1 - avgDist / average)


def prdx(totalL, totalA, average, avgDist):
    return (190 - (10 * (totalA / totalL))) + ((1 + avgDist / average) * avgDist) * (1 - avgDist / average)


average = angle(ang)
avgDist = avg(lst)
totalL = tlst(lst)
totalA = tang(ang)
py = prdy(totalL, totalA, average, avgDist)
px = prdx(totalL, totalA, average, avgDist)


print("Total Dist: " + str(round(totalL, 4)) + " Total Angle: " + str(round(totalA, 4)))
print("Predicted X value: " + str(round(px, 4)))
print("Predicted Y value: " + str(round(py, 4)))


x = ang
y = lst

plt.scatter(x, y, marker='*', s=10)
plt.legend()
plt.show()
