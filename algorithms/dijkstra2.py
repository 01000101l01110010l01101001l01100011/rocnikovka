from objects import Graph, Vertex
def dijkstra(graph:Graph, start:Vertex, end:Vertex):

    Q = set(graph.vertices)

    distances = {vertex: float('inf') for vertex in graph.vertices}

    neighbors = set(graph.vertices)
    distances[start] = 0
    previous = {}
    previous_vertex = None
    current = start
    while Q:
        current = min(Q, key=lambda vertex: distances[vertex]) 
        if current is not start:
            previous[current] = previous_vertex
        Q.remove(current)
        neighbors = set(Q)
        if current == start:
            neighbors.remove(end)
        elif current == end:
            return distances[end], previous[end]
        else:
            neighbors.add(end)
        for neighbor in neighbors:
            alt = distances[current] + graph.distance(current, neighbor)
            if alt < distances[neighbor]:
                distances[neighbor] = alt
        previous_vertex = current

    return distances[end], previous[end]