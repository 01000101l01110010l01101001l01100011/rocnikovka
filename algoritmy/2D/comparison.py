from control_algorithm import control
from twoD import algorithm, create_points

from math import sqrt


# print(points, set_p)

def con(set_p):
  minimal = 99999
  smallest = None
  for i in set_p:
    for k in set_p:
      for j in set_p:
        if i != k and k!=j and i!=j:
          if (i[1]-k[1])*(j[0]-k[0]) == (j[1]-k[1])*(i[0]-k[0]):
            if sqrt((k[0] - j[0]) ** 2 + (k[1] - j[1]) ** 2) > sqrt((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2):
              set_p.remove((k, j))
            elif sqrt((j[0] - i[0]) ** 2 + (j[1] - i[1]) ** 2) > sqrt((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2):
              set_p.remove(i, j)
            else:
              continue
          if sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) + sqrt((k[0] - j[0]) ** 2 + (k[1] - j[1]) ** 2) + sqrt((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2) < minimal:
            minimal = sqrt((i[0] - j[0]) ** 2 + (i[1] - j[1]) ** 2) + sqrt((k[0] - j[0]) ** 2 + (k[1] - j[1]) ** 2) + sqrt((k[0] - i[0]) ** 2 + (k[1] - i[1]) ** 2)
            smallest = (i, j, k)
  return smallest, minimal


while True:
  points, set_p = create_points(50)
  set_b = set_p.copy()

  points, distance = algorithm(set_p)
  smallest, minimal = con(set_b)
  if int(distance*1000) == int(minimal*1000):
    print("OK")
  else:
    print("Error")
    print(points, distance)
    print(smallest, minimal)
    break

