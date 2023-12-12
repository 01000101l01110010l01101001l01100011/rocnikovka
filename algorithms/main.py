from algorithm import smallest_triangle
from graph import create_plot
from objects import Vertex
import random



points = set(Vertex(random.randint(0, 10), random.randint(0, 10)) for _ in range(14))

triangle = smallest_triangle(points)
print("Smallest triangle:", triangle[0])
edges = (triangle[1][0], triangle[1][1]),(triangle[1][0], triangle[1][3]),(triangle[1][1], triangle[1][3])
create_plot([point.coordinates for point in points], edges)

