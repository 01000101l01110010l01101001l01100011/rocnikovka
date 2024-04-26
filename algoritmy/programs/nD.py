import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean
import math, time

def generate_random_points(num_points, dimension):
    points = np.random.rand(num_points, dimension)
    return points

def generate_subsets(points, subset_length):
    subsets = combinations(points, subset_length)   # Všechny (n+1)-prvkové podmnožiny
    return subsets

def algorithmnd(points):
    num_points = len(points)  # Počet bodů
    n = len(points[0])   # Dimenze
    subsets = generate_subsets(points, n+1) # Vytvoří všechny (n+1)-prvkové podmnožiny
    print("Generated subsets")
    polytopes = [] # Seznam polytopů
    podmo = time.time()
    for i, subset in enumerate(subsets): # Pro podmnožinu (polytop)
        perimeter = 0
        edges = generate_subsets(subset, 2) # Množina všech 2-prvkových podmnožin
        for edge in edges:
            perimeter += euclidean(edge[0], edge[1]) # Délka hrany
        print("Polytope",i, "of", math.comb(num_points, n+1))
        polytopes.append((subset, perimeter)) # Přidá hranu do seznamu polytopů
    print(time.time()-podmo)
    podmo = time.time()
    sorted_polytopes = sorted(polytopes, key=lambda x: x[-1]) # Seřadí seznam polytopů podle jejich obvodu
    print(time.time()-podmo)
    print("Sorted polytopes")
    while len(sorted_polytopes) > 0:
        polytope, distance = sorted_polytopes[0] # Polytop a jeho obvod
        x1 = polytope[0] # První bod polytopu
        differences = [] # Seznam rozdílů
        for x in polytope[1:]: # Pro bod v TODO
            difference = x - x1 # Rozdíl bodů
            differences.append(difference) # Přidá rozdíl do seznamu rozdílů
        matrix = np.vstack(differences) # Vytvoří matici z rozdílů
        determinant = np.linalg.det(matrix) # Spočítá determinant
        if determinant != 0: # Pokud je determinant nenulový, řešením je tento polytop
            return polytope, distance
        print("Checked polytope")

l = np.array([[1, 2, 3], [3, 2, 1], [4, 7, 0], [9, 5, 2], [2, 4, 6]])
print(algorithmnd(l))