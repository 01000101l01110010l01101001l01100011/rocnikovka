from networkx import Graph
def dijkstraa(G:Graph, start, end):
    Q = set()
    distances = {}
    previous = {}
    depth = 0
    for vertex in G:
        distances[vertex] = float('inf')
        previous[vertex] = None
        Q.add(vertex)

    distances[start] = 0
    while Q:
        u = min(Q, key=lambda vertex: distances[vertex])
        depth += 1
        if u == end:
            return distances[end], [start, previous[end], end]
        Q.remove(u)
        neighbors = [x for x in Q if (u, x) in G.edges(u)] # tohle je spatny
        for neighbor in neighbors:
            alt = distances[u] + G.get_edge_data(u, neighbor)['weight'] 
            if alt < distances[neighbor]:
                distances[neighbor] = alt
                previous[neighbor] = u

    return distances[end], [start, previous[end], end]

def dijkstra_triangle(G:Graph, start, end):
    Q = set() # All vertices are here
    distances = {} # A dictionary with distances of how to get to the given vertex
    middle_point = {} # A dictionary to remember the vertex that was before 


    # Label all vertices in graph with distance infinity
    for vertex in G:
        distances[vertex] = float('inf')
        middle_point[vertex] = None
        Q.add(vertex)
    depth = 0
    distances[start] = 0
    while Q: # Going through all vertices
        # Choosing the vertex with smallest distance from start.
        print("Amogus")
        actual = min(Q, key=lambda vertex: distances[vertex])
        depth +=1

        if actual == end or depth == 3:
            return distances[end], [start, middle_point[end], end]
        Q.remove(actual)

        neighbors = Q.copy() # tohle jinak Dela to neco spatne
        if actual == start:
            neighbors.remove(end)
            
        print("Morbius")

        # Check the distances and write the smaller ones
        for neighbor in neighbors:
            calculated_distance = distances[actual] + G.get_edge_data(actual, neighbor)['weight']
            if calculated_distance < distances[neighbor]:
                distances[neighbor] = calculated_distance
                middle_point[neighbor] = actual


    return distances[end], [start, middle_point[end], end]



def dijkstra_triangle_second(G:Graph, start, end):
    Q = set() # All vertices are here
    distances = {} # A dictionary with distances of how to get to the given vertex
    middle_point = {} # A dictionary to remember the vertex that was before 


    # Label all vertices in graph with distance infinity
    for vertex in G:
        distances[vertex] = float('inf')
        middle_point[vertex] = None
        Q.add(vertex)

    distances[start] = 0
    Q.remove(start)
    Q.remove(end)
    for neighbor in Q:
        # print(neighbor)
        distance = G.get_edge_data(start, neighbor)['weight']
        distances[neighbor] = distance
        middle_point[neighbor] = neighbor
    
    for neighbor in Q:
        # print(neighbor)
        distance = G.get_edge_data(neighbor, end)['weight']
        if distances[end] > distances[neighbor] + distance:
            distances[end] =  distances[neighbor] + distance
            middle_point[end] = neighbor

    return distances[end], [start, middle_point[end], end]