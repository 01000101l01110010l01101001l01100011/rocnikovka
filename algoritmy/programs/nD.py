import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean
import math
import time


def generate_random_points(num_points, dimension):
    points = np.random.rand(num_points, dimension)
    return points


def generate_subsets(points, subset_length):
    # Všechny (n+1)-prvkové podmnožiny.
    subsets = combinations(points, subset_length)
    return subsets


def algorithmnd(points):
    num_points = len(points)  # Počet bodů.
    point_indices = list(range(num_points))  # Indexy bodů.
    n = len(points[0])   # Dimenze.
    # Vytvoří všechny (n+1)-prvkové podmnožiny.
    subsets = list(generate_subsets(point_indices, n+1))

    # Vytvoří matici vzdáleností.
    distances = np.zeros((num_points, num_points))
    for i in range(num_points):
        for j in range(i+1, num_points):
            distances[i, j] = euclidean(points[i], points[j])
            distances[j, i] = distances[i, j]

    polytopes = []  # Seznam polytopů.
    for subset in subsets:  # Pro podmnožinu (polytop).
        perimeter = 0
        edges = generate_subsets(subset, 2)
        for edge in edges:
            perimeter += distances[edge[0], edge[1]]  # Z matice vzdáleností spočítá obvod polytopu.
        current_points = [points[j] for j in subset]
        polytopes.append((current_points, perimeter))
    sorted_polytopes = sorted(polytopes, key=lambda x: x[-1])
    while len(sorted_polytopes) > 0:
        polytope, distance = sorted_polytopes[0]  # Polytop a jeho obvod.
        x1 = polytope[0]  # První bod polytopu.
        differences = []  # Seznam rozdílů.
        for x in polytope[1:]:  # Pro bod v polytopu.
            difference = x - x1  # Rozdíl bodů.
            differences.append(difference)  # Přidá rozdíl do seznamu rozdílů.
        matrix = np.vstack(differences)  # Vytvoří matici z rozdílů.
        determinant = np.linalg.det(matrix)  # Spočítá determinant.
        if determinant != 0:  # Pokud je determinant nenulový, řešením je tento polytop.
            return polytope, distance

points = np.array([[1, 2, 3], [7, -5, 2], [4, 8, -4], [7, 10, 3], [-3, 3, 3], [5, 1, -4]])
print(algorithmnd(points))
