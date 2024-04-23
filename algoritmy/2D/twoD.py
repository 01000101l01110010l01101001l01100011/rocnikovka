from random import random
from math import sqrt, dist
from networkx import Graph, neighbors

def create_points(n):
  points = {}
  set_points = set()
  for i in range(n):
    x, y = random()*10, random()*10
    while (x, y) in points.values():
      x, y = random()*10, random()*10
    points[i] = (x, y)
    set_points.add((x, y))
  return points, set_points


def find_path(G:Graph, start, end):
  min_path = None, None, None, float("inf")
  for x in neighbors(G, start) :
    path = G.get_edge_data(start, x)["weight"] + G.get_edge_data(end, x)["weight"]
    if float(min_path[3]) > path:
      min_path = start, x, end, path
  return min_path

def algorithm(V:set):
  G = Graph()
  edges = []
  while V:
    x = V.pop()
    for v in V:
      if x!=v:
        edges.append((x, v, dist(x, v)))
  if V:
    print("Error")
  G.add_weighted_edges_from(edges)

  min_triangle = None
  min_triangle_weight = float("inf")
  for edge in edges:
    edge_weight = G.get_edge_data(edge[0], edge[1])["weight"]
    G.remove_edge(edge[0], edge[1])
    u, j, v, weight= find_path(G, edge[0], edge[1])
    if (v[1]-u[1])*(j[0]-u[0]) == (j[1]-u[1])*(v[0]-u[0]):
      if dist(u, j) > dist(u, v):
        G.remove_edge(u, j)
      elif dist(j, v) > dist(u, v):
        G.remove_edge(v, j)
      else:
        continue
    elif weight + edge_weight < min_triangle_weight:
      min_triangle = (u, j, v)
      min_triangle_weight = weight + edge_weight
    G.add_weighted_edges_from([(u, v, dist(u, v))])

  return min_triangle, min_triangle_weight