from oneD import algorithmone
from twoD import algorithmtwo
from nD import generate_random_points, algorithmnd
import time
import numpy as np
import csv


number_of_cycles = 2
numbers = []
for i in range(100000):
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
def all():
  with open('data_2D.csv', 'w', newline='') as file_2d:
    writer_2D = csv.writer(file_2d)
    with open('data_1D.csv', 'w', newline='') as file_1d:
      writer_1D = csv.writer(file_1d)
      with open('data_nD_2D.csv', 'w', newline='') as file_nd:
        writer_nd = csv.writer(file_nd)
        with open('data_nD_10D.csv', 'w', newline='') as file_ndd:
          writer_ndd = csv.writer(file_ndd)
          with open('data_nD_20D.csv', 'w', newline='') as file_nddd:
            writer_nddd = csv.writer(file_nddd)
            for n_points in numbers:
              print(n_points)
              # 1D
              for k in range(number_of_cycles):
                points = generate_random_points(n_points, 1)
                before = time.time()
                algorithmone(points)
                after = time.time() - before
                writer_1D.writerows([["1D", "Points:", n_points, "Time:", after]])
                print("1D", n_points)
                

              # 2D
              for k in range(number_of_cycles):
                points = generate_random_points(n_points, 2)

                before = time.time()
                algorithmtwo(points)
                after = time.time() - before
                writer_2D.writerows([["2D", "Points:", n_points, "Time:", after]])
                print("2D", n_points)

              # # nD
              # for k in range(number_of_cycles):
              #   points = generate_random_points(n_points, 2)
              #   before = time.time()
              #   algorithmnd(points)
              #   after = time.time() - before
              #   writer_nd.writerows([["nD - 2D", "Points:", n_points, "Time:", after]])
              #   print("nd-2D", n_points)

              # for k in range(2):
              #   points = generate_random_points(n_points, 10)
              #   before = time.time()
              #   algorithmnd(points)
              #   after = time.time() - before
              #   writer_ndd.writerows([["nD - 10D", "Points:", n_points, "Time:", after]])
              #   print("nd-10D", n_points)

              # for k in range(2):
              #   points = generate_random_points(n_points, 20)
              #   before = time.time()
              #   algorithmnd(points)
              #   after = time.time() - before
              #   writer_nddd.writerows([["nD - 20D", "Points:", n_points, "Time:", after]])
              #   print("nd-20D", n_points)


# 20, 10 = 101.5 sekund
def nd_test():
  print(numbers)
  with open('data_10D.csv', 'w', newline='') as file_ndd:
    writer_ndd = csv.writer(file_ndd)
    for n_points in numbers:
      points = generate_random_points(n_points, 10)
      # print(points)
      before = time.time()
      algorithmnd(points)
      after = time.time() - before
      print(n_points, ":", after)
      writer_ndd.writerows([["nD - 10D", "Points:", n_points, "Time:", after]])

nd_test()
# all()