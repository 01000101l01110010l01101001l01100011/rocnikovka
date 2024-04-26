import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean
import math
import time


def generate_random_points(num_points, dimension):
    points = np.random.rand(num_points, dimension)
    return points


def generate_subsets(points, subset_length):
    # Všechny (n+1)-prvkové podmnožiny
    subsets = combinations(points, subset_length)
    return subsets


def algorithmnd(points):
    num_points = len(points)  # Počet bodů
    point_indices = list(range(num_points))  # Indexy bodů
    n = len(points[0])   # Dimenze
    # Vytvoří všechny (n+1)-prvkové podmnožiny
    subsets = list(generate_subsets(point_indices, n+1))

    # Vytvoří matici vzdáleností
    distances = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(i+1, num_points):
            distances[i, j] = euclidean(points[i], points[j])
            distances[j, i] = distances[i, j]

    print("Generated subsets")
    polytopes = []  # Seznam polytopů
    podmo = time.time()
    for i, subset in enumerate(subsets):  # Pro podmnožinu (polytop)
        perimeter = 0
        # Množina všech 2-prvkových podmnožin
        edges = generate_subsets(subset, 2)
        for edge in edges:
            perimeter += distances[edge[0], edge[1]]  # Délka hrany
        print("Polytope", i, "of", math.comb(num_points, n+1))
        # Přidá hranu do seznamu polytopů
        current_points = [points[j] for j in subset]
        polytopes.append((current_points, perimeter))
    # Seřadí seznam polytopů podle jejich obvodu
    print(time.time()-podmo)
    sorted_polytopes = sorted(polytopes, key=lambda x: x[-1])
    print("Sorted polytopes")
    while len(sorted_polytopes) > 0:
        polytope, distance = sorted_polytopes[0]  # Polytop a jeho obvod
        x1 = polytope[0]  # První bod polytopu
        differences = []  # Seznam rozdílů
        for x in polytope[1:]:  # Pro bod v TODO
            difference = x - x1  # Rozdíl bodů
            differences.append(difference)  # Přidá rozdíl do seznamu rozdílů
        matrix = np.vstack(differences)  # Vytvoří matici z rozdílů
        determinant = np.linalg.det(matrix)  # Spočítá determinant
        if determinant != 0:  # Pokud je determinant nenulový, řešením je tento polytop
            return polytope, distance
        print("Checked polytope")
