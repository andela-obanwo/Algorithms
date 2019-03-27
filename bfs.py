from collections import deque

def bfs(graph, start):
    visited = []
    nodes_to_visit = deque(start)

    while nodes_to_visit:
        node = nodes_to_visit.popleft()
        if node not in visited:
            neighbours = graph[node]

            for neighbour in neighbours:
                nodes_to_visit.append(neighbour)
            visited.append(node)
    return visited