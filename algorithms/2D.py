from objects import Graph, Verticle
from dijkstra2 import dijkstra
import random

def smallest_triangle(vertices:set):
    """
    Find the smallest triangle in a set of vertices.
    """
    graph = Graph(vertices)
    for edge in graph.edges:
        graph.weights[edge] = ((edge[0].x - edge[1].x)**2 + (edge[0].y - edge[1].y)**2)**0.5
    
    smallest_triangle = {"a" : (float('inf'), float('inf'))}
    for edge in graph.edges:
        graph.edges.remove(edge)
        smallest_distance = dijkstra(graph, edge[0], edge[1])
        smallest_distance += graph.weights[edge[0], edge[1]]
        print(smallest_distance)
        if smallest_distance < smallest_triangle.values()[0]:
            smallest_triangle = {edge: smallest_distance}

        graph.edges.append(edge)


    return smallest_triangle

print(smallest_triangle(set(Verticle(random.randint(0, 100), random.randint(0, 100)) for _ in range(5))))
