from twoD import algorithmtwo
import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean

def calculate_perimeter(triangle):
    perimeter = sum(euclidean(triangle[i], triangle[(i + 1) % 3]) for i in range(3))
    return perimeter

def controls(points):
    smallest_perimeter = float('inf')
    smallest_triangle = None

    for triangle_points in combinations(points, 3):
        perimeter = calculate_perimeter(triangle_points)
        if perimeter < smallest_perimeter:
            smallest_perimeter = perimeter
            smallest_triangle = triangle_points

    return smallest_triangle, smallest_perimeter


while True:
  points = np.random.rand(5, 2)
  minimal, shortest = controls(points)
  min, weight = algorithmtwo(points)

  if int(shortest*100000) == int(weight*100000):
    print("OK")
  else:
    print("Error")
    print(points,"\n", minimal,"\n", shortest, "\n", min, "\n", weight)
    break

