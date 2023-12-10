def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph.vertices}

    Q = set(graph.vertices)
    neighbors = set(graph.vertices)
    distances[start] = 0
    point = None

    while Q:
        current = min(Q, key=lambda vertex: distances[vertex])
        Q.remove(current)
        neighbors = set(Q)
        if current == start or current == end:
            neighbors.remove(end)
        else:
            neighbors.remove(current)
        for neighbor in neighbors:
            alt = distances[current] + graph.distance(current, neighbor)
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                point = current

    print(distances[end])
    return distances[end]