# BFS and DFS intro: https://youtu.be/9gOljeZlCAs

from bfs import bfs
from dfs import dfs
from dijkstra import Dijkstra

if __name__ == '__main__':
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    visited = []
    bfs(graph, 'A', visited)
    print("\n")

    visited = set()
    dfs(graph, 'A', visited)
    print("\n")

    # Example from https://youtu.be/LT6dBbdotto
    # representation of the graph with an adjacency list
    graph = {
        'A': [('B', 1), ('F', 3)],
        'B': [('A', 1), ('C', 8), ('D', 7), ('E', 4), ('F', 1)],
        'C': [('B', 8), ('D', 3), ('E', 3)],
        'D': [('B', 7), ('C', 3), ('E', 5)],
        'E': [('A', 5), ('B', 4), ('C', 3), ('D', 5), ('F', 2)],
        'F': [('A', 3), ('B', 1), ('E', 2)]
    }
    # representation of the same graph but with an adjacency matrix
    # https://graphonline.ru/en/create_graph_by_matrix
    graph2 = [
        [0, 1, 0, 0, 0, 3],
        [1, 0, 8, 7, 4, 1],
        [0, 8, 3, 3, 0, 0],
        [0, 7, 3, 0, 5, 0],
        [5, 4, 3, 5, 0, 2],
        [3, 1, 0, 0, 2, 0],
    ]

    dijkstra = Dijkstra(6)
    dijkstra.graph = graph2
    dijkstra.dijkstra(0)

    # Example from https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/
    dijkstra = Dijkstra(9)
    dijkstra.graph = [
        [0, 4, 0, 0, 0, 0, 0, 8, 0],
        [4, 0, 8, 0, 0, 0, 0, 11, 0],
        [0, 8, 0, 7, 0, 4, 0, 0, 2],
        [0, 0, 7, 0, 9, 14, 0, 0, 0],
        [0, 0, 0, 9, 0, 10, 0, 0, 0],
        [0, 0, 4, 14, 10, 0, 2, 0, 0],
        [0, 0, 0, 0, 0, 2, 0, 1, 6],
        [8, 11, 0, 0, 0, 0, 1, 0, 7],
        [0, 0, 2, 0, 0, 0, 6, 7, 0]
    ]
    dijkstra.dijkstra(0)
    print("\n")
