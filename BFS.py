graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []  # List to track visited nodes
queue = []    # Queue for BFS

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        # Dequeue a node
        s = queue.pop(0)
        print(s, end=" ")

        # Enqueue all unvisited neighbors of the dequeued node
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# Call BFS starting from node 'A'
bfs(visited, graph, 'A')
