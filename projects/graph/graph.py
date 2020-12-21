"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        q = Queue()
        visited = set()

        q.enqueue(starting_vertex)

        while q.size() > 0:
            vert = q.dequeue()

            if vert not in visited:
                print(vert)
                visited.add(vert)

                for nbr in self.get_neighbors(vert):
                    q.enqueue(nbr)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        s = Stack()
        visited = set()

        s.push(starting_vertex)

        while s.size() > 0:
            vert = s.pop()

            if vert not in visited:
                print(vert)
                visited.add(vert)

                for nbr in self.get_neighbors(vert):
                    s.push(nbr)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        if not visited:
            visited = set()

        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)

            for nbr in self.get_neighbors(starting_vertex):
                self.dft_recursive(nbr, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        q = Queue()
        visited = set()
        path = [starting_vertex]

        q.enqueue(path)

        while q.size() > 0:
            p = q.dequeue()

            # vertex to grab neighbors
            v = p[-1]

            if v not in visited:
                visited.add(v)

                # the last vertex in p is already the target
                if v == destination_vertex:
                    return p

                for nbr in self.get_neighbors(v):
                    # add a new path, prev path and adding the nbr
                    new_path = p + [nbr]
                    q.enqueue(new_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        s = Stack()
        visited = set()
        path = [starting_vertex]

        s.push(path)

        while s.size() > 0:
            p = s.pop()

            # vertex to grab neighbors
            v = p[-1]

            if v not in visited:
                visited.add(v)

                if v == destination_vertex:
                    return p

                for nbr in self.get_neighbors(v):
                    new_path = p + [nbr]
                    s.push(new_path)

    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # initialize visited and path
        if not visited and not path:
            path = [starting_vertex]
            visited = set()

        # base case
        # this will return none on other paths not having the target
        if destination_vertex in path:
            return path

        # base case
        if starting_vertex in visited:
            return

        # last elem in path list is the vert that hasn't been checked yet
        vert = path[-1]
        visited.add(vert)

        for nbr in self.get_neighbors(vert):
            new_path = path + [nbr]
            p = self.dfs_recursive(nbr, destination_vertex, visited, new_path)

            if p is not None:
                return p


if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
    print(f"recursive: {graph.dfs_recursive(1, 6)}")
