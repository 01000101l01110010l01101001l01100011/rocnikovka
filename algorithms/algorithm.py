from objects import Graph
from dijkstra2 import dijkstra


def smallest_triangle(vertices:set):
    """
    Find the smallest triangle in a set of vertices.
    """
    graph = Graph(vertices)
    
    smallest_triangle = (float('inf'), None)
    for edge in graph.edges:
        graph.edges.remove(edge)
        smallest_distance, middle_point = dijkstra(graph, edge[0], edge[1])
        smallest_distance += graph.weights[edge[0], edge[1]]
        if smallest_distance < smallest_triangle[0]:
            smallest_triangle = (smallest_distance, (middle_point.coordinates, edge[0].coordinates,"-->", edge[1].coordinates))

        graph.edges.append(edge)


    return smallest_triangle


