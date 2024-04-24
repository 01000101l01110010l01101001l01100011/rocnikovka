import random
import numpy as np

n = 5
points = np.array()
points = np.array([], dtype=float)

for i in range(n**3):
    point = ()
    list = []
    for k in range(n+1):
        list.append(random.random()*random.randint(0, 100))
    point = tuple(list)
    points.add(point)
# print(points)

def perimeter(V:set):
    for i in V:
        for k in V:
            for u in range(n):
                a = 9 #mogus