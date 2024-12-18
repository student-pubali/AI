graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = [] # List to track visited nodes
def dfs(visited,graph,node):
    if node not in visited:
        #Mark the node as visited then print it
        visited.append(node)
        print(node,end=" ")

        # Recur for all the neighbours of the current node
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

# Call DFS starting from node 'A'
dfs(visited,graph,'A')            
