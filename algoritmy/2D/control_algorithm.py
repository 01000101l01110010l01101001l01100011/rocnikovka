import networkx as nx
import random, math, time

def control(points):
    # ti = time.time()
    # points = {}
    # number_of_points = n
    # for i in range(number_of_points):
    #     x, y = random.random()*10, random.random()*10
    #     while (x, y) in points.values():
    #         x, y = random.random()*10, random.random()*10
    #     points[i] = (x, y)

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

    mininininninninmal = 99999999
    smalllllllest = []
    # i=0
    for poo1 in points:
        for poo2 in points:
            for poo3 in points:
                # print("All: ", (i)/(len(points)**3)*100, "% Done")
                # i+=1
                if poo1 == poo2 or poo1 == poo3 or poo2 == poo3:
                    continue
                x1, y1 = points[poo1]
                x2, y2 = points[poo3]
                distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # I add the weight of the edge because the function down returns only the weight of path and not of the cycle
                distance += find_path_weight([poo1, poo2, poo3])
                if distance < mininininninninmal:
                    mininininninninmal = distance
                    smalllllllest = [poo1, poo2, poo3]
                elif distance == mininininninninmal and not (poo1 in smalllllllest and poo2 in smalllllllest and poo3 in smalllllllest):
                    mininininninninmal = distance
                    smalllllllest.append([poo1, poo2, poo3])

    return smalllllllest, mininininninninmal