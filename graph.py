class Graph:
    """
    Graph object with a adjacent list implementation.
    Directed graph without weighted edges.
    """

    def __init__(self, graph_dict=None):
        """
        Constructor of graph
        :param graph_dict: Adjacency matrix representation of a graph using a dict data structure
        """
        if graph_dict is None:
            self.graph_dict = {}
            self.vertices = []
            self.edges = []
        else:
            self.graph_dict = graph_dict
            self.vertices = self.graph_dict.keys()
            self.edges = self.generateEdges()

    def getVertices(self) -> list:
        """
        Getter method for vertices in the graph.
        :return: A list of vertices for the graph.
        """
        return list(self.vertices)

    def getEdges(self) -> list:
        """
        Getter method for edges in the graph.
        :return: An array of edges from the graph
        """
        return self.edges

    def generateEdges(self) -> list:
        """
        Generates an array of tuples containing all the edges
        :return: an array of edges
        """
        edges = []
        if self.graph_dict is not None:
            for keys in self.graph_dict:
                for neighbour in self.graph_dict[keys]:
                    if (keys, neighbour) not in edges:
                        edges.append((keys, neighbour))
        return edges

    def addVertex(self, newVertex) -> None:
        """
        Adds a vertex to the graph
        :param newVertex: takes in a Vertex and adds it to the graph dictionary
        :return None
        """
        if newVertex not in self.getVertices():
            self.graph_dict[newVertex] = []

    def addEdge(self, newEdge) -> None:
        """
        Add a new edge to the graph
        :newEdge: takes in a new Edge, pair of vertices in the form of an array, list or tuple
        :return: None
        """
        v1, v2 = tuple(newEdge)
        if newEdge not in self.getEdges():
            if v1 in self.getVertices():
                self.graph_dict[v1].append(v2)
                self.edges = self.generateEdges()
            else:
                self.graph_dict[v1] = v2
                self.edges = self.generateEdges()

    def BFS(self, startVertex, searchVertex) -> list:
        """
        Breadth first search starting from startVertex implementing ALGORITHM.
        :param startVertex: The vertex where we should start searching.
        :param searchVertex: The vertex where that we are searching for.
        :return: Whether or not search vertex is within the graph
        """
        Q = [startVertex]
        visited = []

        while len(Q) != 0:
            # get the first item in the queue
            u = Q.pop(0)
            if u == searchVertex:
                visited.append(u)
                return visited
            else:
                if u not in visited:
                    visited.append(u)
                    for neighbour in self.graph_dict[u]:
                        Q.append(neighbour)
        return []

    def DFS(self, startVertex, searchVertex) -> list:
        """
        Depth first search starting from startVertex implementing ALGORITHM.
        :param startVertex: The vertex where we should start searching.
        :param searchVertex: The vertex where that we are searching for.
        :return: Path that user can backtrack to reach from the searchVertex to the startVertex.
        """
        visited = []
        stack = [startVertex]
        while len(stack) != 0:
            # get the item on top of the stack
            u = stack.pop()
            if u == searchVertex:
                visited.append(u)
                return visited
            else:
                if u not in visited:
                    visited.append(u)
                    for neighbour in self.graph_dict[u]:
                        stack.append(neighbour)
        return []
