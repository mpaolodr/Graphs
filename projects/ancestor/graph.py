class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # add v1 if it's not in self.vertices
        # avoid errors
        if v1 not in self.vertices:
            self.vertices[v1] = set()

        # add v2 if it's not in self.vertices
        if v2 not in self.vertices:
            self.vertices[v2] = set()

        # add edge to v1
        self.vertices[v1].add(v2)

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id not in self.vertices:
            return None

        return self.vertices[vertex_id]

    def get_levels(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        level_dict = dict()
        level = [None] * (max(self.vertices) + 1)

        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        # level of starting vertex
        level[starting_vertex] = 0
        visited.add(starting_vertex)

        while q.size() > 0:
            vert = q.dequeue()

            for nbr in self.get_neighbors(vert):

                if nbr not in visited:
                    q.enqueue(nbr)
                    level[nbr] = level[vert] + 1

                    visited.add(nbr)

        for i in range(1, max(self.vertices) + 1):
            if level[i] is not None:
                level_dict[i] = level[i]

        return level_dict
