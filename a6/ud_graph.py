# Course: CS261 - Data Structures
# Author: Kelley Sharp
# Assignment: A6 - Undirected Graph
# Description: Implement an undirected graph with 11 methods

from heapq import heappush, heappop
from collections import deque


class UndirectedGraph:
    """
    Class to implement undirected graph
    - duplicate edges not allowed
    - loops not allowed
    - no edge weights
    - vertex names are strings
    """

    def __init__(self, start_edges=None):
        """
        Store graph info as adjacency list
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.adj_list = dict()

        # populate graph with initial vertices and edges (if provided)
        # before using, implement add_vertex() and add_edge() methods
        if start_edges is not None:
            for u, v in start_edges:
                self.add_edge(u, v)

    def __str__(self):
        """
        Return content of the graph in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = [f'{v}: {self.adj_list[v]}' for v in self.adj_list]
        out = '\n  '.join(out)
        if len(out) < 70:
            out = out.replace('\n  ', ', ')
            return f'GRAPH: {{{out}}}'
        return f'GRAPH: {{\n  {out}}}'

    # ------------------------------------------------------------------ #

    def add_vertex(self, v: str) -> int:
        """
        Adds a new vertex to the graph
        """
        # Adjacency list example: {'A': [], 'B', []...}
        # If the vertex name is already present in the graph
        if v not in self.adj_list:
            self.adj_list[v] = []

        return len(self.adj_list.keys())

    def add_edge(self, u: str, v: str) -> None:
        """
        Adds a new edge to the graph connecting two vertices with provided names
        """
        # If u and v refer to the same vertex
        if u == v:
            return
        # or if u or v are not in the graph
        if u not in self.adj_list:
            self.add_vertex(u)
        if v not in self.adj_list:
            self.add_vertex(v)

        if v in self.adj_list[u]:
            return
        else:
            self.adj_list[u].append(v)
            self.adj_list[v].append(u)

    def remove_edge(self, v: str, u: str) -> None:
        """
        Removes an edge between two vertices with provided names
        """
        # If either (or both) of the vertex names do not exist in the graph
        if v not in self.adj_list or u not in self.adj_list:
            return
        # If an edge does not exist between them
        if u not in self.adj_list[v] or v not in self.adj_list[u]:
            return
        else:
            self.adj_list[u].remove(v)
            self.adj_list[v].remove(u)

    def remove_vertex(self, v: str) -> None:
        """
        Removes a vertex with a given name and all edges incident to it from the graph
        """
        # if the given vertex does not exist in the graph
        if v not in self.adj_list:
            return
        else:  # for each vertex v shares an edge with, remove v from that vertex's edges list
            for value in self.adj_list[v]:
                self.adj_list[value].remove(v)
            # remove the given vertex itself from the adjacency list
            del self.adj_list[v]

    def get_vertices(self) -> []:
        """
        Returns a list of vertices of the graph, unordered
        """
        return list(self.adj_list.keys())

    def get_edges(self) -> []:
        """
        Returns a list of edges in the graph as tuples, unordered
        """
        edge_set = set()
        # loop over key, value tuples
        for vertex, adjacent_vertices in self.adj_list.items():
            # loop over each vertex's adjacent vertices
            for adjacent in adjacent_vertices:
                # place alphabetically sorted tuples into a set
                if vertex > adjacent:
                    edge_set.add((adjacent, vertex))
                else:
                    edge_set.add((vertex, adjacent))

        return list(edge_set)

    def is_valid_path(self, path: []) -> bool:
        """
        Takes a list of vertex names and returns True if the sequence of vertices
        represents a valid path in the graph (empty paths are considered valid)
        """
        if path == []:
            return True

        # If there is only one vertex name in the path and that vertex is not in the graph
        if len(path) == 1 and path[0] not in self.adj_list:
            return False

        # Otherwise there are at least two vertices in the path to visit we can check for edges
        i = 0
        while i + 1 < len(path):
            if path[i + 1] not in self.adj_list[path[i]]:
                return False
            i += 1

        return True

    def dfs(self, v_start, v_end=None) -> []:
        """
        Performs a depth-first search (DFS) in the graph and returns a list of vertices
        visited during the search, in the order they were visited
        """
        if v_start not in self.adj_list:
            return []

        stack = [v_start]
        visited = []

        while len(stack) > 0:
            # get current by popping off stack
            cur = stack.pop()
            # visit
            visited.append(cur)
            # if current is the v_end, break
            if cur is v_end:
                break
            # push neighbors onto stack in alphabetical order
            for neighbor in sorted(self.adj_list[cur], reverse=True):
                if neighbor not in visited:
                    # if the neighbor is already in the stack, move it up
                    if neighbor in stack:
                        stack.remove(neighbor)
                    stack.append(neighbor)

        return visited

    def bfs(self, v_start, v_end=None) -> []:
        """
        TODO: Write this implementation
        """
        if v_start not in self.adj_list:
            return []
        queue = deque([v_start])
        visited = []

        while len(queue) > 0:
            # get current by dequeing
            cur = queue.popleft()
            # visit
            visited.append(cur)
            # if current is the v_end, break
            if cur is v_end:
                break
            # enqueue neighbors in alphabetical order
            #  if they have not been visited yet
            for neighbor in sorted(self.adj_list[cur]):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

        return visited

    def count_connected_components(self):
        """
        TODO: Write this implementation
        """


    def has_cycle(self):
        """
        TODO: Write this implementation
        """


if __name__ == '__main__':

    # print("\nPDF - method add_vertex() / add_edge example 1")
    # print("----------------------------------------------")
    # g = UndirectedGraph()
    # print(g)

    # for v in 'ABCDE':
    #     g.add_vertex(v)
    # print(g)

    # g.add_vertex('A')
    # print(g)

    # for u, v in ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', ('B', 'C')]:
    #     g.add_edge(u, v)
    # print(g)


    # print("\nPDF - method remove_edge() / remove_vertex example 1")
    # print("----------------------------------------------------")
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    # g.remove_vertex('DOES NOT EXIST')
    # g.remove_edge('A', 'B')
    # g.remove_edge('X', 'B')
    # print(g)
    # g.remove_vertex('D')
    # print(g)


    # print("\nPDF - method get_vertices() / get_edges() example 1")
    # print("---------------------------------------------------")
    # g = UndirectedGraph()
    # print(g.get_edges(), g.get_vertices(), sep='\n')
    # g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE'])
    # print(g.get_edges(), g.get_vertices(), sep='\n')


    print("\nPDF - method is_valid_path() example 1")
    print("--------------------------------------")
    g = UndirectedGraph(['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE'])
    test_cases = ['ABC', 'ADE', 'ECABDCBE', 'ACDECB', '', 'D', 'Z']
    for path in test_cases:
        print(list(path), g.is_valid_path(list(path)))


    # print("\nPDF - method dfs() and bfs() example 1")
    # print("--------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = 'ABCDEGH'
    # for case in test_cases:
    #     print(f'{case} DFS:{g.dfs(case)} BFS:{g.bfs(case)}')
    # print('-----')
    # for i in range(1, len(test_cases)):
    #     v1, v2 = test_cases[i], test_cases[-1 - i]
    #     print(f'{v1}-{v2} DFS:{g.dfs(v1, v2)} BFS:{g.bfs(v1, v2)}')


    # print("\nPDF - method count_connected_components() example 1")
    # print("---------------------------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print(g.count_connected_components(), end=' ')
    # print()


    # print("\nPDF - method has_cycle() example 1")
    # print("----------------------------------")
    # edges = ['AE', 'AC', 'BE', 'CE', 'CD', 'CB', 'BD', 'ED', 'BH', 'QG', 'FG']
    # g = UndirectedGraph(edges)
    # test_cases = (
    #     'add QH', 'remove FG', 'remove GQ', 'remove HQ',
    #     'remove AE', 'remove CA', 'remove EB', 'remove CE', 'remove DE',
    #     'remove BC', 'add EA', 'add EF', 'add GQ', 'add AC', 'add DQ',
    #     'add EG', 'add QH', 'remove CD', 'remove BD', 'remove QG',
    #     'add FG', 'remove GE')
    # for case in test_cases:
    #     command, edge = case.split()
    #     u, v = edge
    #     g.add_edge(u, v) if command == 'add' else g.remove_edge(u, v)
    #     print('{:<10}'.format(case), g.has_cycle())
