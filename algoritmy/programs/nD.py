import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean


def generate_random_points(num_points, dimension):
    points = np.random.rand(num_points, dimension)
    return points

def generate_subsets(points, subset_length):
    subsets = combinations(points, subset_length)
    return subsets

def algorithmnd(points):
    # Parameters
    num_points = len(points)  # Number of random points
    n = len(points[0])   # Dimension of the space
    subsets = generate_subsets(points, n+1)
    polytopes = []
    for subset in subsets:
        perimeter = 0
        edges = generate_subsets(subset, 2)
        for edge in edges:
            perimeter += euclidean(edge[0], edge[1])
        polytopes.append((subset, perimeter))
    sorted_polytopes = sorted(polytopes, key=lambda x: x[-1])
    min_p = None
    while len(sorted_polytopes) > 0:
        polytope, distance = sorted_polytopes[0]
        x1 = polytope[0]
        differences = []
        for x in subset[1:]:
            difference = x - x1
            differences.append(difference)
        matrix = np.vstack(differences)
        determinant = np.linalg.det(matrix)
        if determinant != 0:
            return polytope, distance
