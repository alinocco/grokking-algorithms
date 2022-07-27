
class Graph:
    def __init__(self, number_of_vertices, graph=[]):
        self.number_of_vertices = number_of_vertices
        self.graph = graph

    def add_edge(self, start, end, length):
        self.graph.append([start, end, length])

    def print_distances(self, distances):
        for i in range(self.number_of_vertices):
            print("%s\t\t%s" % (i, distances[i]))

    def bellman_ford_algorithm(self, source):
        distances = [float('inf')] * self.number_of_vertices
        distances[source] = 0

        for _ in range(self.number_of_vertices - 1):
            for start, end, length in self.graph:
                if distances[start] != float('inf') and distances[start] + length < distances[end]:
                    distances[end] = distances[start] + length

        # Check for negative-weight cycle
        for start, end, length in self.graph:
            if distances[start] != float('inf') and distances[start] + length < distances[end]:
                raise Exception('NegativeWeightCycle')

        self.print_distances(distances)


graph = Graph(5, [
    [0, 1, -1],
    [0, 2, 4],
    [1, 2, 3],
    [1, 3, 2],
    [1, 4, 2],
    [3, 2, 5],
    [3, 1, 1],
    [4, 3, -3],
])

graph.bellman_ford_algorithm(0)
