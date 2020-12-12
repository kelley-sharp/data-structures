# Course: CS261 - Data Structures
# Author: Kelley Sharp
# Assignment: A6 - Directed Graph
# Description: Implement a directed graph with 10 methods

from collections import deque


class DirectedGraph:
    """
    Class to implement directed weighted graph
    - duplicate edges not allowed
    - loops not allowed
    - only positive edge weights
    - vertex names are integers
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.v_count = 0
        self.adj_matrix = []

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            v_count = 0
            for u, v, _ in start_edges:
                v_count = max(v_count, u, v)
            for _ in range(v_count + 1):
                self.add_vertex()
            for u, v, weight in start_edges:
                self.add_edge(u, v, weight)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        if self.v_count == 0:
            return 'EMPTY GRAPH\n'
        out = '   |'
        out += ' '.join(['{:2}'.format(i) for i in range(self.v_count)]) + '\n'
        out += '-' * (self.v_count * 3 + 3) + '\n'
        for i in range(self.v_count):
            row = self.adj_matrix[i]
            out += '{:2} |'.format(i)
            out += ' '.join(['{:2}'.format(w) for w in row]) + '\n'
        out = f"GRAPH ({self.v_count} vertices):\n{out}"
        return out

    # ------------------------------------------------------------------ #

    def add_vertex(self) -> int:
        """
        Adds a new vertex to the graph
        """
        # Example adjacency matrix: [[0, 15, 0, 7], [3, 0, 1, 1]]
        # self.v_count is also the number of rows in the matrix
        self.v_count += 1
        if self.v_count > 1:
            # add an empty edge weight to all existing vertices
            row_i = 0
            while row_i < len(self.adj_matrix):
                self.adj_matrix[row_i].append(0)
                row_i += 1

            # add the new row to the bottom
            new_v_row = []
            self.adj_matrix.append(new_v_row)
            # fill the new row with empty edges
            i = 0
            while i < self.v_count:
                new_v_row.append(0)
                i += 1

        else:
            self.adj_matrix = [[0]]

        return self.v_count

    def add_edge(self, src: int, dst: int, weight=1) -> None:
        """
        Adds an edge to the graph or updates the weight of an existing edge
        """
        if src == dst or weight < 0:
            return
        # Or if one or both vertices are not in the matrix
        elif src >= len(self.adj_matrix) or dst >= len(self.adj_matrix):
            return
        else:
            self.adj_matrix[src][dst] = weight

    def remove_edge(self, src: int, dst: int) -> None:
        """
        Removes an edge between two vertices with provided names
        """
        # If src or dst are not vertices in the graph
        if src < 0 or src > self.v_count - 1:
            return
        if dst < 0 or dst > self.v_count - 1:
            return

        # If there is no edge to remove between those vertices
        if self.adj_matrix[src][dst] == 0:
            return

        self.adj_matrix[src][dst] = 0

    def get_vertices(self) -> []:
        """
        Returns a list of vertices of the graph
        """
        vertices = []

        i = 0
        while i < self.v_count:
            vertices.append(i)
            i += 1

        return vertices

    def get_edges(self) -> []:
        """
        Returns a list of edges and their weights in the graph as tuples
        """
        edges_list = []
        # Use a nested loop to gain access to src, dst, and weights of edges
        i = 0
        while i < len(self.adj_matrix):
            j = 0
            while j < len(self.adj_matrix):
                if self.adj_matrix[i][j] > 0:
                    edges_list.append((i, j, self.adj_matrix[i][j]))
                j += 1
            i += 1

        return edges_list

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex names and returns True if the sequence of vertices
        represents a valid path in the graph. Empty path is considered valid
        """
        if len(path) == 0:
            return True

        if path[0] < 0 or path[0] > self.v_count - 1:
            return False
        # Otherwise there are at least two vertices in the path
        # Loop through each vertex's neighbors. If there is no edge shared
        # with the next vertex in the path, return False
        i = 0
        while i < len(path) - 1:
            if self.adj_matrix[path[i]][path[i + 1]] == 0:
                return False
            i += 1

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs a depth-first search in the graph and returns a list of vertices visited,
        in the order they were visited during the search
        """
        # If v_start is not in the graph
        if v_start > self.v_count or v_start < 0:
            return []

        visited = []
        # Starting stack has start vertex
        stack = [v_start]

        while len(stack) > 0:
            # Get current by popping off top of stack
            cur = stack.pop()
            # Visit the current vertex
            visited.append(cur)
            # If current is the provided end vertex
            if cur == v_end:
                break
            # Push neighbors onto the stack in ascending order
            neighbor = len(self.adj_matrix) - 1
            row = self.adj_matrix[cur]
            while neighbor >= 0:
                neighbor_edge = row[neighbor]
                # make sure there is a nonzero edge weight
                if neighbor_edge > 0 and neighbor not in visited:
                    if neighbor in stack:
                        stack.remove(neighbor)
                    stack.append(neighbor)
                neighbor -= 1

        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        # If v_start is not in the graph
        if v_start > self.v_count or v_start < 0:
            return []

        visited = []

        # Queue up starting vertex
        queue = deque([v_start])

        while len(queue) > 0:
            # Get current by dequeuing
            cur = queue.popleft()
            # Visit the current vertex
            visited.append(cur)
            # If current is the provided end vertex
            if cur == v_end:
                break
            # Enqueue neighbors in ascending order
            # if they have not been visited yet
            neighbor = 0
            row = self.adj_matrix[cur]
            while neighbor < len(self.adj_matrix):
                neighbor_edge = row[neighbor]
                # make sure there is a nonzero edge weight
                if neighbor_edge > 0 and neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                neighbor += 1

        return visited

    def has_cycle(self):
        """
        TODO: Write this implementation
        """
        def detect_cycle(v, visited, current_visited):
            """
            Recursive helper method that does a DFS-style traversal of
            all the neighbors, looking for a cycle
            """
            # visit the current vertex
            visited.add(v)
            # add current vertex to current visit iteration
            #  so that the current vertex is the origin of the cycle check
            current_visited.add(v)
            # go through neighbors in the row
            neighbor = 0
            row = self.adj_matrix[v]
            while neighbor < self.v_count:
                neighbor_edge = row[neighbor]
                # if neighbor has a nonzero edge
                if neighbor_edge > 0:
                    # if we've already visited neighbor this iteration
                    #  then we've found a cycle
                    if neighbor in current_visited:
                        return True
                    # otherwise recurse on that neighbor and look for cycles
                    elif detect_cycle(neighbor, visited, current_visited):
                        return True
                neighbor += 1
            # remove the current vertex from this iteration
            #  so that the next iteration starts clean
            current_visited.remove(v)
            return False
        visited = set()
        current_visited = set()
        for vertex in range(self.v_count):
            if vertex not in visited and detect_cycle(vertex, visited, current_visited):
                return True
        return False

    def dijkstra(self, src: int) -> []:
        """
        TODO: Write this implementation
        """


if __name__ == '__main__':
    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = DirectedGraph()
    # print(g)
    # for _ in range(5):
    #     g.add_vertex()
    # print(g)

    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # for src, dst, weight in edges:
    #     g.add_edge(src, dst, weight)
    # print(g)

    # print("\nPDF - method get_edges() example 1")
    # print("----------------------------------")
    # g = DirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # print(g.get_edges(), g.get_vertices(), sep='\n')

    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
             (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    g = DirectedGraph(edges)
    test_cases = [[0, 1, 4, 3], [1, 3, 2, 1], [0, 4], [4, 0], [], [2]]
    for path in test_cases:
        print(path, g.is_valid_path(path))

    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for start in range(5):
    #     print(f'{start} DFS:{g.dfs(start)} BFS:{g.bfs(start)}')

    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)

    # edges_to_remove = [(3, 1), (4, 0), (3, 2)]
    # for src, dst in edges_to_remove:
    #     g.remove_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')

    # edges_to_add = [(4, 3), (2, 3), (1, 3), (4, 0)]
    # for src, dst in edges_to_add:
    #     g.add_edge(src, dst)
    #     print(g.get_edges(), g.has_cycle(), sep='\n')
    # print('\n', g)

    # print("\nPDF - dijkstra() example 1")
    # print("--------------------------")
    # edges = [(0, 1, 10), (4, 0, 12), (1, 4, 15), (4, 3, 3),
    #          (3, 1, 5), (2, 1, 23), (3, 2, 7)]
    # g = DirectedGraph(edges)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
    # g.remove_edge(4, 3)
    # print('\n', g)
    # for i in range(5):
    #     print(f'DIJKSTRA {i} {g.dijkstra(i)}')
