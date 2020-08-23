"""
Mainframe for testing a graph API

This will contain basic graph related algorithms

Author: Himika Dastidar
Date: August 2020
"""
from graph import Graph

if __name__ == '__main__':
    graph = {"a": ["c"],
             "b": ["c", "e"],
             "c": ["a", "b", "d", "e"],
             "d": ["c"],
             "e": ["c", "b"],
             "f": []
             }

    G = Graph(graph)
    G.addEdge(('d','e'))
    print(G.DFS('a','d'))


