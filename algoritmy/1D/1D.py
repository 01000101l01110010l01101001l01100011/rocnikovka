from random import random

def algorithm(n):
  points = [random()*10 for _ in range(n)]
  points.sort()
  return points[0]