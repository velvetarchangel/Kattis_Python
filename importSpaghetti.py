"""
Import Spagetti Kattis

Date: 2020-06-14
Name: Himika
"""
import re

class Vertex:
    def __init__(self, value):
        self.value = value

class Edge:
    def __init__(self, startVertex, endVertex):
        self.startVertex = startVertex;
        self.endVertex = endVertex;

class Graph:
    #adjacency matrix representation of the graph
    def __init__(self, arrOfVertices, arrOfEdges):
        self.arrOfVertices = arrOfVertices
        self.arrOfedges = arrOfEdges
        self.G = []
        G = [0]*len(arrOfVertices)
        for v in range(len(arrOfVertices)):
            G[v] = [0]*len(arrOfVertices)
            for v_1 in range(len(arrOfVertices)):
                if((arrOfVertices[v], arrOfVertices[v_1]) in arrOfEdges):
                    G[v][v_1] = 1

    def __getGraph__(self):
        return self.G
"""
Process input
"""

if "__name__==__main__":
    N = int(input())
    arrVertices = input().split()
    arrEdges = []

    for i in range(N):
        filename, line = input().split()
        line = int(line)

        for j in range(line):
            statement = input()
            _import = statement.strip("import ,")
            _connections = _import.split(", ")
            for k in range(len(_connections)):
                arrEdges.append(Edge(filename, _connections[k]))
    graph = Graph(arrVertices, arrEdges)
    print(graph.__getGraph__())


