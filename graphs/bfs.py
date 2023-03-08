# https://www.educative.io/answers/how-to-implement-a-breadth-first-search-in-python
# https://www.geeksforgeeks.org/queue-in-python/ <- Use a queue instead of a list
# https://www.geeksforgeeks.org/deque-in-python/
# https://stackoverflow.com/questions/717148/queue-queue-vs-collections-deque

from collections import deque


def bfs(graph, starting_node, visited):
    queue = deque()
    visited.append(starting_node)
    queue.append(starting_node)

    while queue:
        node = queue.popleft()  # popleft() is FIFO and pop() is LIFO
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
