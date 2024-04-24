import numpy as np
from itertools import combinations

def generate_random_points(num_points, dimension):
    points = np.random.rand(num_points, dimension)
    return points

def generate_subsets(points, subset_length):
    subsets = list(combinations(points, subset_length))
    return subsets

# Parameters
num_points = 50  # Number of random points
dimension = 5   # Dimension of the space

# Generate random points
points = generate_random_points(num_points, dimension)

# Generate subsets of length n+1
subsets = generate_subsets(points, dimension+1)

# Display the generated subsets
print("Random Points:")
print(points)
print("\nSubsets of length n+1:")
for subset in subsets:
    print(subset)
