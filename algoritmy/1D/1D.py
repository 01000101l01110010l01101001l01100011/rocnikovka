from random import random

def algorithm(n):
  points = [random()*10 for _ in range(n)]
  points.sort()
  shortest = float('inf')
  points = None
  for i in range(len(points-1)):
    if abs((points[i] - points[i+1])) < shortest:
      shortest = points[i] - points[i+1]
      points = points[i], points[i+1]
  return points