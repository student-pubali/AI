from collections import defaultdict

# Define capacities of the jugs and the target amount
jug1, jug2, aim = 4, 3, 2

# Dictionary to keep track of visited states
visited = defaultdict(lambda: False)

def waterjugSolver(amt1, amt2):
    # Check if the current state meets the target
    if (amt1 == aim and amt2 == 0) or (amt2 == aim and amt1 == 0):
        print(amt1, amt2)
        return True

    # If this state has not been visited
    if not visited[(amt1, amt2)]:
        print(amt1, amt2)

        # Mark this state as visited
        visited[(amt1, amt2)] = True

        # Explore all possible moves
        return (
            waterjugSolver(0, amt2) or               # Empty Jug 1
            waterjugSolver(amt1, 0) or               # Empty Jug 2
            waterjugSolver(jug1, amt2) or            # Fill Jug 1
            waterjugSolver(amt1, jug2) or            # Fill Jug 2
            waterjugSolver(
                amt1 - min(amt1, jug2 - amt2),       # Pour Jug 1 -> Jug 2
                amt2 + min(amt1, jug2 - amt2)
            ) or
            waterjugSolver(
                amt1 + min(amt2, jug1 - amt1),       # Pour Jug 2 -> Jug 1
                amt2 - min(amt2, jug1 - amt1)
            )
        )

    return False

# Call the solver with initial state (0, 0)
print("Steps to solve:")
if not waterjugSolver(0, 0):
    print("No solution!")
