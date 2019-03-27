
def dfs(graph, start):
    stack = [start]
    visited = []

    while stack:
        node = stack.pop()
        if node not in visited:
            for neighbor in graph[node]:
                stack.append(neighbor)
            visited.append(node)
    return visited
