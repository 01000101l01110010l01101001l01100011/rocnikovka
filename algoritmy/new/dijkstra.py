from networkx import Graph
def dijsktra(G:Graph, start, end):
    Q = set()
    distances = {}
    previous = {}
    for vertex in G:
        distances[vertex] = float('inf')
        previous[vertex] = None
        Q.add(vertex)

    distances[start] = 0
    while Q:
        u = min(Q, key=lambda vertex: distances[vertex])
        if u == end:
            return distances[end], [start, previous[end], end]
        Q.remove(u)
        neighbors = [x for x in Q if (u, x) in G.edges(u)] 
        for neighbor in neighbors:
            alt = distances[u] + G.get_edge_data(u, neighbor)['weight']
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = u

    return distances[end], [start, previous[end], end]

def dijkstra_triangle(G:Graph, start, end):
    Q = set()
    distances = {}
    previous = {}
    for vertex in G:
        distances[vertex] = float('inf')
        previous[vertex] = None
        Q.add(vertex)

    distances[start] = 0
    while Q:
        u = min(Q, key=lambda vertex: distances[vertex])
        if u == end:
            return distances[end], [start, previous[end], end]
        Q.remove(u)

        neighbors = Q
        if u == start:
            neighbors.remove(end)

        for neighbor in neighbors:
            alt = distances[u] + G.get_edge_data(u, neighbor)['weight']
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = u

    return distances[end], [start, previous[end], end]