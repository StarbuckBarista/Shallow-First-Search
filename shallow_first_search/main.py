"""
Project Started: 3/25/2021

@author: StarbuckBarista
"""
class Node(object):
    def __init__(self, name: str):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self, source: Node, destination: Node):
        self.source = source
        self.destination = destination
    def getSource(self):
        return self.source
    def getDestination(self):
        return self.destination
    def __str__(self):
        return "{} -> {}".format(self.source.getName(), self.destination.getName())

class Diagraph(object):
    def __init__(self):
        self.edges = {}
    def addNode(self, node: Node):
        if node in self.edges:
            raise ValueError("Duplicate Node")
        else:
            self.edges[node] = []
    def addEdge(self, edge: Edge):
        if not (edge.getSource() in self.edges and edge.getDestination() in self.edges):
            raise ValueError("Unknown Node")
        else:
            self.edges[edge.getDestination()].append(edge.getSource())
    def parentsOf(self, node: Node):
        if node not in self.edges:
            raise ValueError("Unknown Node")
        else:
            return self.edges[node]
    def hasNode(self, node: Node):
        return node in self.edges
    def getNode(self, name: str):
        for node in self.edges:
            if node.getName() == name:
                return node

        raise NameError(name)
    def __str__(self):
        result = ""

        for source in self.edges:
            for destination in self.edges[source]:
                result += "{} -> {}\n".format(source.getName(), destination.getName())

        return result[:-1]

class Graph(Diagraph):
    def addEdge(self, edge: Edge):
        Diagraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Diagraph.addEdge(self, rev)

def SFS(graph: Diagraph, source: Node, destination: Node, path = [], shortest = None):
    path = path + [source]

    if source == destination:
        return path

    for node in graph.parentsOf(source):
        if node not in path:
            if shortest == None or len(path) < len(shortest):
                newPath = SFS(graph, node, destination, path, shortest)

                if newPath != None:
                    shortest = newPath

    return shortest

def shortestPath(graph: Diagraph, source: Node, destination: Node):
    if not (graph.hasNode(source) and graph.hasNode(destination)):
        if not graph.hasNode(source):
            raise NameError(source.getName())
        else:
            raise NameError(destination.getName())
    else:
        path = SFS(graph, destination, source, [], None)

        if path != None:
            path.reverse()

        return path

def evaluateAnswer(answer):
    result = ""

    if answer != None:
        for i in range(len(answer)):
            result += str(answer[i])

            if i != len(answer) - 1:
                result += " -> "
    else:
        result = "No Solution Found!"

    return result
