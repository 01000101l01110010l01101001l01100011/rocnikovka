from objects import Graph, Verticle
def dijkstra(graph:Graph, start:Verticle, end:Verticle):
    """
    Dijkstra's algorithm for finding the shortest path between two nodes in a graph.
    """
    unvisited = set(graph.vertices)
    unvisited.remove(start)

    neighbors = set(graph.vertices)


    distances = {verticle: float('inf') for verticle in graph.vertices} # Distance from start to verticle
    distances[start] = 0

    current = start
    while current != end:
        while unvisited:
            neighbors = set(graph.vertices)
            if current == start:
                neighbors.remove(start)
                neighbors.remove(end)
            else:
                neighbors.remove(current)
            while neighbors:
                verticle = neighbors.pop()
                distances[verticle] = min(distances[verticle], distances[current] + graph.distance(current, verticle))
            
            current_distance = float('inf')
            for verticle in unvisited:
                if distances[verticle] < current_distance:
                    current = verticle
                    current_distance = distances[verticle]
            unvisited.remove(current)
        print("amogus")  
            
    return distances[end]