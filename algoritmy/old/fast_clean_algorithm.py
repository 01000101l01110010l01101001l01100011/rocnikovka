# Zatim nic
from networkx.algorithms.shortest_paths.weighted import dijkstra_path
from networkx import Graph
import networkx as nx
from random import random
from math import sqrt
import dijkstra
import time

def create_points(n):
    points = {}
    for i in range(n):
            x, y = random()*10, random()*10
            while (x, y) in points.values():
                x, y = random()*10, random()*10
            points[i] = (x, y)

    return points

def create_edges(points:dict):
    edges = {(x, y): sqrt((points[x][0] - points[y][0]) ** 2 + (points[x][1] - points[y][1]) ** 2) for x in points for y in points if x != y}
    G = Graph()
    G.add_weighted_edges_from([*i, edges[i] ] for i in edges)

    return G, edges

def find_path_weight(points:list, edges:dict):
     return sum(edges[(points[i], points[i+1])] for i in range(len(points)-1))

def find_shortest_path(G:Graph, edges):
    shortest_path = None
    smallest_triangle = 999999
    for edge in G.edges:
        G.remove_edge(*edge)
        path_length, path = dijkstra.dijkstra_triangle(G, *edge)
        triangle = edges[edge] + path_length
        if triangle  < smallest_triangle:
            shortest_path = path
            smallest_triangle = triangle
        G.add_edge(*edge, weight=edges[edge])
    return shortest_path


def find_shortest_path_nx(G:Graph, edges):
    shortest_path = None
    smallest_triangle = 999999
    for edge in G.edges:
        G.remove_edge(*edge)
        path = dijkstra_path(G, *edge)
        path_length = find_path_weight(path, edges)
        triangle = edges[edge] + path_length
        if triangle  < smallest_triangle:
            shortest_path = path
            smallest_triangle = triangle
        G.add_edge(*edge, weight=edges[edge])
    return shortest_path

G, edges = create_edges(create_points(500))
# atime = time.time()
# print((find_shortest_path(G, edges)))
# mytime = time.time() - atime
# print("My time:", mytime)
# atime = time.time()
# print((find_shortest_path_nx(G, edges)))
# nxtime = time.time() - atime
# print("Nx time:", nxtime)
# print("My is faster by:", (nxtime - mytime), "seconds", "or by", (nxtime - mytime)/nxtime*100, "%" )


# DIjkstra testing
# print(list(G.nodes))
# print(list(G.edges), [list(G.get_edge_data[x]) for x in G.edges])
# for edge in G.edges:
#     print(edge, G.get_edge_data(edge[0], edge[1]))

edging = (50, 180)
G.remove_edge(edging[0], edging[1])

atime = time.time()
print("NX:",nx.dijkstra_path_length( G, edging[0], edging[1]), nx.dijkstra_path(G, edging[0], edging[1]))
nxtime = time.time()-atime
print("NX TIME:", nxtime)

atime = time.time()
print("FIRST:",dijkstra.dijkstraa( G,edging[0], edging[1]))
firsttime = time.time()-atime
print("FIRST TIME:", firsttime)

atime = time.time()
print("SECOND:",dijkstra.dijkstra_triangle_second( G,edging[0], edging[1]))
secondtime = time.time()-atime
print("SECOND TIME:", secondtime)

if nxtime < secondtime:
    print("nx")
else:
    print("second is winner")
    
    print("It is faster by:", (nxtime/secondtime)*100, "%")

0.06
0.0003