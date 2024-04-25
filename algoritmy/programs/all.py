from oneD import algorithmone
from twoD import algorithmtwo
from nD import generate_random_points, algorithmnd
import time
import numpy as np
import csv


number_of_cycles = 5
numbers = []
for i in range(60):
   numbers.append(i)
for i in range(10):
   numbers.remove(i)

one_time = np.array([])
one_list = []
second_time = np.array([])
second_list = []


nd_twod_list = []
nd_five_list = []
nd_ten_list = []
nd_twt_list = []
with open('data.csv', 'w', newline='') as file:
  writer = csv.writer(file)
  for n_points in numbers:
    print(n_points)
    # 1D
    for k in range(number_of_cycles):
      points = generate_random_points(n_points, 1)
      before = time.time()
      algorithmone(points)
      after = time.time() - before
      writer.writerows([["1D", "Points:", n_points, "Time:", after]])
      

    # 2D
    for k in range(number_of_cycles):
      points = generate_random_points(n_points, 2)

      before = time.time()
      algorithmtwo(points)
      after = time.time() - before
      writer.writerows([["2D", "Points:", n_points, "Time:", after]])


    # nD
    for k in range(number_of_cycles):
      points = generate_random_points(n_points, 2)
      before = time.time()
      algorithmnd(points)
      after = time.time() - before
      writer.writerows([["nD - 2D", "Points:", n_points, "Time:", after]])


    for k in range(number_of_cycles):
      points = generate_random_points(n_points, 5)
      before = time.time()
      algorithmnd(points)
      after = time.time() - before
      writer.writerows([["nD - 5D", "Points:", n_points, "Time:", after]])

    for k in range(number_of_cycles//2):
      points = generate_random_points(n_points, 10)
      before = time.time()
      algorithmnd(points)
      after = time.time() - before
      writer.writerows([["nD - 10D", "Points:", n_points, "Time:", after]])

    for k in range(number_of_cycles//4):
      points = generate_random_points(n_points, 20)
      before = time.time()
      algorithmnd(points)
      after = time.time() - before
      writer.writerows([["nD - 20D", "Points:", n_points, "Time:", after]])

# print("1D", one_time.mean())
# print("2D", second_time.mean())
# print("nD", n_time.mean())

    


