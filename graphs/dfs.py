# https://www.educative.io/answers/how-to-implement-depth-first-search-in-python

def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)
