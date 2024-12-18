class MonkeyAndBanana:
    def __init__(self):
        # Initial positions
        self.monkey_position = "ground"
        self.box_position = "floor"
        self.banana_position = "high"
        self.state = (self.monkey_position, self.box_position)
        
    def move_monkey(self):
        """Move the monkey from the ground to the box, or from the box to the bananas"""
        if self.monkey_position == "ground":
            self.monkey_position = "box"
            self.state = (self.monkey_position, self.box_position)
        elif self.monkey_position == "box":
            self.monkey_position = "bananas"
            self.state = (self.monkey_position, self.box_position)

    def move_box(self):
        """Move the box from the floor to the right position (if needed)"""
        if self.box_position == "floor":
            self.box_position = "under_bananas"
            self.state = (self.monkey_position, self.box_position)

    def is_goal_state(self):
        """Check if the monkey has reached the bananas"""
        return self.monkey_position == "bananas"
    
    def bfs(self):
        """Perform BFS to find the solution"""
        queue = []
        visited = set()
        
        # Start with the initial state
        queue.append((self.state, []))  # Queue of (state, actions)
        visited.add(self.state)
        
        while queue:
            state, actions = queue.pop(0)
            self.monkey_position, self.box_position = state
            
            # Check if the current state is a goal state
            if self.is_goal_state():
                return actions  # Return the sequence of actions to get the bananas
            
            # Add possible moves to the queue
            if self.monkey_position == "ground" and self.box_position == "floor":
                # Move the box under the bananas
                new_state = ("ground", "under_bananas")
                if new_state not in visited:
                    queue.append((new_state, actions + ["Move box under bananas"]))
                    visited.add(new_state)
            
            if self.monkey_position == "ground" and self.box_position == "under_bananas":
                # Move the monkey onto the box
                new_state = ("box", "under_bananas")
                if new_state not in visited:
                    queue.append((new_state, actions + ["Move monkey to the box"]))
                    visited.add(new_state)
            
            if self.monkey_position == "box" and self.box_position == "under_bananas":
                # Move the monkey to the bananas
                new_state = ("bananas", "under_bananas")
                if new_state not in visited:
                    queue.append((new_state, actions + ["Move monkey to the bananas"]))
                    visited.add(new_state)
        
        return None  # If no solution is found


# Running the problem
if __name__ == "__main__":
    problem = MonkeyAndBanana()
    solution = problem.bfs()  # Find the solution using BFS
    
    if solution:
        print("Solution found!")
        for step in solution:
            print(step)
    else:
        print("No solution found!")
