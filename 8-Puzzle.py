class Solution:
    def solve(self, board):
        # Dictionary to track visited states and their distances
        state_dict = {}
        flatten = []
        # Flatten the 2D board into a 1D tuple
        for i in range(len(board)):
            flatten += board[i]
        flatten = tuple(flatten)
        state_dict[flatten] = 0

        # Check if the initial state is already the goal state
        if flatten == (0, 1, 2, 3, 4, 5, 6, 7, 8):
            return 0

        # Use BFS to find the shortest path to the goal state
        return self.get_paths(state_dict)

    def get_paths(self, state_dict):
        cnt = 0
        while True:
            # Get all nodes at the current level (distance = cnt)
            current_nodes = [x for x in state_dict if state_dict[x] == cnt]
            if len(current_nodes) == 0:
                return -1  # No solution

            for node in current_nodes:
                # Find all possible moves from the current node
                next_moves = self.find_next(node)
                for move in next_moves:
                    if move not in state_dict:  # If the state is new
                        state_dict[move] = cnt + 1
                    if move == (0, 1, 2, 3, 4, 5, 6, 7, 8):  # Goal state
                        return cnt + 1
            cnt += 1

    def find_next(self, node):
        # Define possible moves for each position of the empty tile (0)
        moves = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4, 6],
            4: [1, 3, 5, 7],
            5: [2, 4, 8],
            6: [3, 7],
            7: [4, 6, 8],
            8: [5, 7]
        }
        results = []
        pos_0 = node.index(0)  # Find the position of the empty tile (0)

        # Generate new states by swapping 0 with adjacent tiles
        for move in moves[pos_0]:
            new_node = list(node)  # Convert tuple to list for manipulation
            new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]
            results.append(tuple(new_node))  # Convert back to tuple and add to results

        return results


# Instantiate the solution and solve the puzzle
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]
]
print("Minimum moves to solve the puzzle:", ob.solve(matrix))
