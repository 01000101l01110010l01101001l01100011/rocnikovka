from random import random
import numpy as np

def algorithmone(points:np.array):
  points = np.sort(points)
  shortest = float('inf')
  for i in range(len(points)-1):
    if abs((points[i] - points[i+1])) < shortest:
      shortest = points[i] - points[i+1]
      closest_points = points[i], points[i+1]
  return closest_points