import networkx as nx
import matplotlib.pyplot as plt
from random import random
import math, time
import sys

def sus(n):
    ti = time.time()
    # Generate points
    points = {}
    number_of_points = n
    for i in range(number_of_points):
        x, y = random()*10, random()*10
        while (x, y) in points.values():
            x, y = random()*10, random()*10
        points[i] = (x, y)

    #Generate edges
    edges = {}
    G = nx.Graph()
    for i in points:
        for j in points:
            if i == j:
                continue
            x1, y1 = points[i]
            x2, y2 = points[j]
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
            G.add_edge(i, j, weight=distance)
            edges[(i, j)] = distance
            edges[(j, i)] = distance

    # function to find a weight of a path
    def find_path_weight(points:list):
        weight = 0
        for i in range(len(points)-1):
            poin1 = points[i]
            poin2 = points[i+1]
            weight += edges[(poin1, poin2)]
        return weight


    # algorithm
    shortest_path = None
    smallest_triangle = 999999
    # i=0
    for edge in G.edges:
        # print("Sus: ", i/(len(G.edges))*100, "% Done")
        # i+=1
        G.remove_edge(edge[0], edge[1])
        path = nx.dijkstra_path(G, edge[0], edge[1]) # Path as a list of points [1, 2, 3]
        path_length = find_path_weight(path) # Length of the path
        triangle = edges[edge] + path_length # Circumference of the triangle
        if triangle  < smallest_triangle:
            shortest_path = path
            smallest_triangle = triangle # change the values if it is smaller
            # print(edge, "yes")
        # print(path)
        G.add_edge(edge[0], edge[1], weight=edges[edge])
        # print(edge)


    # Some printing
    # print("Path", shortest_path,":", smallest_triangle)
    # print("Edge 1:", (shortest_path[0], shortest_path[1]), edges[(shortest_path[0], shortest_path[1])])
    # print("Edge 2:", (shortest_path[1], shortest_path[2]), edges[(shortest_path[1], shortest_path[2])])
    # print("Edge 3:", (shortest_path[0], shortest_path[2]), edges[(shortest_path[0], shortest_path[2])])

    # Some colors
    node_color = ['orange'] * number_of_points  # Set default color for all nodes
    node_color[shortest_path[0]] = 'red'  # Change color of the first node to red
    node_color[shortest_path[1]] = 'red'
    node_color[shortest_path[2]] = 'red'

    # # 'To prove that the algorithm above is wrong' type of algorithm 
    # mininininninninmal = 99999999
    # smalllllllest = []
    # for poo1 in points:
    #     for poo2 in points:
    #         for poo3 in points:
    #             if poo1 == poo2 or poo1 == poo3 or poo2 == poo3:
    #                 continue
    #             x1, y1 = points[poo1]
    #             x2, y2 = points[poo3]
    #             distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # I add the weight of the edge because the function down returns only the weight of path and not of the cycle
    #             distance += find_path_weight([poo1, poo2, poo3])
    #             if distance < mininininninninmal:
    #                 mininininninninmal = distance
    #                 smalllllllest = [poo1, poo2, poo3]
    #             elif distance == mininininninninmal and not (poo1 in smalllllllest and poo2 in smalllllllest and poo3 in smalllllllest):
    #                 mininininninninmal = distance
    #                 smalllllllest.append([poo1, poo2, poo3])

    # # print("TRUE SMALLEST TRIANGLE:")
    # # print(smalllllllest, ":", mininininninninmal)
    # if set(smalllllllest) == set(shortest_path) and mininininninninmal == smallest_triangle:
    #     print("YES")
    # else:
    #     print(r"NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    nx.draw(G, points, node_color=node_color)  
    nx.draw_networkx_labels(G, points)
    plt.show()
    sys.exit()  # Stop the program
    return time.time() - ti
        
sus(5)
# for i in range(10000):
#     sus()
