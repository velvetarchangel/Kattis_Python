import unittest
from graph import Graph


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.graph = {"a": ["c"],
                      "b": ["c", "e"],
                      "c": ["a", "b", "d", "e"],
                      "d": ["c"],
                      "e": ["c", "b"],
                      "f": []
                      }

    def test_constructor_emptyGraph(self):
        G = Graph(None)
        assert G.graph_dict == {}
        assert G.vertices == []
        assert G.edges == []

    def test_constructor_nonEmptyGraph(self):
        G = Graph(self.graph)
        assert G.graph_dict == self.graph
        assert list(G.vertices) == ['a', 'b', 'c', 'd', 'e', 'f']
        assert G.edges == [('a', 'c'), ('b', 'c'), ('b', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'),
                           ('d', 'c'), ('e', 'c'), ('e', 'b')]

    def test_getVertices(self):
        G = Graph(self.graph)
        expected_vertices = ['a', 'b', 'c', 'd', 'e', 'f']
        obtained_vertices = G.getVertices()
        self.assertEqual(obtained_vertices, expected_vertices)

    def test_addVertices(self):
        G = Graph(self.graph)
        G.addVertex('g')
        expected_vertices = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        obtained_vertices = G.getVertices()
        self.assertEqual(obtained_vertices, expected_vertices)

    def test_addEdges(self):
        G = Graph(self.graph)
        G.addEdge(('d', 'e'))
        obtained_edges = G.getEdges()
        expected_edges = [('a', 'c'), ('b', 'c'), ('b', 'e'), ('c', 'a'), ('c', 'b'), ('c', 'd'), ('c', 'e'),
                          ('d', 'c'), ('d', 'e'), ('e', 'c'), ('e', 'b')]
        self.assertEqual(obtained_edges, expected_edges)


if __name__ == '__main__':
    unittest.main()
