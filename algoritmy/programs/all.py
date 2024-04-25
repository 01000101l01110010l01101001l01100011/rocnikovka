from oneD import algorithmone
from twoD import algorithmtwo
from nD import algorithm, generate_random_points
import time
import numpy as np

for n_points in range(20):
  n_points += 5
  one_time = np.array([])
  for k in range(20):
    points = generate_random_points(n_points, 1)
    before = time.time()
    algorithmone(points)
    after = time.time() - before
    one_time = np.append(one_time, after)

  # Udelat to 2D aby fungovalo s np.array
  # V 1D PREPSAT TEXT MISTO .SORT NA .np array()

print(one_time.mean())