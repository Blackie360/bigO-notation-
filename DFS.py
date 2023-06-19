def dfs(graph, start_node, visited=None, path=None):
    if visited is None:
        visited = set()

    if path is None:
        path = []

    visited.add(start_node)
    path.append(start_node)

    print(start_node, end=" ")

    for neighbor in graph[start_node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, path)
        elif neighbor in path:
            print("\nCycle detected:", path[path.index(neighbor):])
    
    path.remove(start_node)


# Example usage
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': ['A']  # Adding a cycle: F -> A
}

start_node = 'A'

print("DFS traversal:")
dfs(graph, start_node)
