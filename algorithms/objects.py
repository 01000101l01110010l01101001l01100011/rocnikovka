class Graph:
    """ A complete graph"""
    def __init__(self, vertices: set):
        self.vertices = vertices
        self.weights = dict()
        for vertex in vertices:
            for other in vertices:
                if vertex != other:
                    self.weights[(vertex, other)] = ((vertex.x - other.x)**2 + (vertex.y - other.y)**2)**0.5
        self.edges = list(self.weights.keys())
    def distance(self, first, other):
        """ Distance between two vertices"""
        return self.weights[(first, other)]


class Vertex:
    """ A vertex in a graph"""
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.coordinates = (x, y)