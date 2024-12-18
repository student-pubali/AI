def minimax_with_alpha_beta(node, depth, alpha, beta, is_maximizing_player):
    """
    Perform minimax with alpha-beta pruning.
    
    :param node: The current node in the tree (either a 'max' or 'min' node).
    :param depth: The current depth in the tree.
    :param alpha: The best value the maximizer can guarantee at the current level.
    :param beta: The best value the minimizer can guarantee at the current level.
    :param is_maximizing_player: A boolean representing whether it's the maximizing player's turn.
    :return: The score of the node after alpha-beta pruning.
    """
    # Base case: if we are at the leaf node, return the value
    if depth == 0 or isinstance(node, int):  # if it's a leaf (or an integer, leaf node has value)
        return node
    
    # Maximizing player's turn
    if is_maximizing_player:
        max_eval = float('-inf')
        for child in node:
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, False)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)  # Update alpha
            if beta <= alpha:  # Beta cut-off
                break
        return max_eval
    
    # Minimizing player's turn
    else:
        min_eval = float('inf')
        for child in node:
            eval = minimax_with_alpha_beta(child, depth - 1, alpha, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)  # Update beta
            if beta <= alpha:  # Alpha cut-off
                break
        return min_eval

# Example game tree for testing
# The leaf nodes are represented as integers (the evaluation values at the leaves).
game_tree = [
    # Maximizer node
    [
        # Minimizer nodes (level 2)
        [
            3,  # Leaf node
            5   # Leaf node
        ],
        [
            6,  # Leaf node
            9   # Leaf node
        ]
    ],
    # Maximizer node
    [
        # Minimizer nodes (level 2)
        [
            1,  # Leaf node
            2   # Leaf node
        ],
        [
            0,  # Leaf node
            8   # Leaf node
        ]
    ]
]

# Set depth of the tree and start the alpha-beta pruning process
depth = 3  # Maximum depth of the tree (for simplicity, the tree has depth 3)
alpha = float('-inf')  # Initial alpha (maximizing player's best score)
beta = float('inf')    # Initial beta (minimizing player's best score)
is_maximizing_player = True  # The root node is for the maximizer player

# Call the alpha-beta pruning function and get the result
result = minimax_with_alpha_beta(game_tree, depth, alpha, beta, is_maximizing_player)

print(f"Optimal value with Alpha-Beta Pruning: {result}")
