V = 4  # Number of vertices (cities)
answer = []  # List to store the answer

# Function to solve TSP using Backtracking
def tsp(graph, v, currPos, n, count, cost):
    # If all cities are visited and there is a path from current city to the start city
    if count == n and graph[currPos][0]:
        answer.append(cost + graph[currPos][0])
        return

    # Backtracking step
    for i in range(n):
        # If the city i is not yet visited and there is a path from the current city to city i
        if not v[i] and graph[currPos][i]:
            v[i] = True  # Mark the city as visited
            tsp(graph, v, i, n, count + 1, cost + graph[currPos][i])  # Recur for the next city
            v[i] = False  # Backtrack and unmark the city

# Main block
if __name__ == '__main__':
    n = 4  # Number of cities
    graph = [[0, 10, 15, 20],  # Distance matrix
             [10, 0, 35, 25],
             [15, 35, 0, 30],
             [20, 25, 30, 0]]

    v = [False] * n  # To keep track of visited cities
    v[0] = True  # Mark the starting city as visited
    tsp(graph, v, 0, n, 1, 0)  # Start TSP from the first city with count 1 and cost 0

    print("Minimum cost:", min(answer))  # Print the minimum cost
