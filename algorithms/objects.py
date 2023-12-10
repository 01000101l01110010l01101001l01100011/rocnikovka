from itertools import combinations
class Graph:
    """ A complete graph"""
    def __init__(self, vertices: set):
        self.vertices = vertices
        self.edges = list(combinations(self.vertices, 2))
        self.weights = {}

    def distance(self, first, other):
        """ Distance between two vertices"""
        try:
            return self.weights[(first, other)]
        except KeyError:
            return self.weights[(other, first)]


class Verticle:
    """ A verticle in a graph"""
    def __init__(self, x, y):
        self.x = x
        self.y = y