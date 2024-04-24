import numpy as np
from itertools import combinations
from scipy.spatial.distance import euclidean


def generate_random_points(num_points, dimension):
    points = np.random.rand(num_points, dimension)
    return points

def generate_subsets(points, subset_length):
    subsets = list(combinations(points, subset_length))
    return subsets

# Parameters
num_points = 25  # Number of random points
n = 3   # Dimension of the space

# Generate random points
points = generate_random_points(num_points, n)

# Generate subsets of length n+1
subsets = generate_subsets(points, n+1)

polytopes = []

for subset in subsets:
    # subset = list(subset)
    perimeter = 0
    # print("SUBSET:", subset)
    for i in range(len(subset)-1):
        perimeter += euclidean(subset[i], subset[i+1])
    polytopes.append((subset, perimeter))
# print("Unsorted", polytopes)

sorted_polytopes = sorted(polytopes, key=lambda x: x[-1])
# print("Sorted", sorted_polytopes)

min_p = None
while len(sorted_polytopes) > 0:
    polytope, distance = sorted_polytopes[0]
    # print(polytope)
    # Extract the first point
    x1 = polytope[0]

    # Initialize an empty list to store differences
    differences = []
    # Iterate over each point after the first point
    for x in subset[1:]:
        # Calculate the difference between each coordinate of the current point and the first point
        difference = x - x1
        differences.append(difference)
    # print("Differences", differences)
    # Stack the differences vertically to form the matrix
    matrix = np.vstack(differences)
    determinant = np.linalg.det(matrix)
    if determinant != 0:
        print(polytope, distance)
        break

    # # Print the matrix
    # print("Matrix:")
    # print(matrix)
    # break