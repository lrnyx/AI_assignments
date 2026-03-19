import heapq
import random
import time

def generate_grid(size, density):
    return [[1 if random.random() < density else 0 for _ in range(size)] for _ in range(size)]


# A* Algorithm
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        x, y = current

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (priority, (nx, ny)))
                    parent[(nx, ny)] = current

    return None


# Dynamic Navigation
def dynamic_navigation(grid, start, goal):
    current = start
    steps = 0

    print("\nStarting Dynamic Navigation...")

    while current != goal:
        path = a_star(grid, current, goal)

        if not path:
            print("No path available. Mission failed.")
            return

        # Move along path
        for step in path[1:]:
            steps += 1

            # Simulate dynamic obstacle
            if random.random() < 0.1:
                grid[step[0]][step[1]] = 1
                print(f"Obstacle appeared at {step}! Replanning...")
                break

            current = step
            print("Moving to:", current)

            if current == goal:
                print("\nReached goal successfully!")
                print("Total steps taken:", steps)
                return

def run_simulation():
    size = 30
    density = 0.2

    grid = generate_grid(size, density)

    print("Dynamic UGV Navigation using Replanning")
    print(f"Grid Size: {size} x {size}")

    while True:
        try:
            start_x = int(input(f"Enter start x (0 to {size-1}): "))
            start_y = int(input(f"Enter start y (0 to {size-1}): "))
            goal_x = int(input(f"Enter goal x (0 to {size-1}): "))
            goal_y = int(input(f"Enter goal y (0 to {size-1}): "))

            if (0 <= start_x < size and 0 <= start_y < size and
                0 <= goal_x < size and 0 <= goal_y < size):
                break
            else:
                print("Coordinates out of bounds. Try again.")

        except ValueError:
            print("Invalid input! Please enter integers.")

    start = (start_x, start_y)
    goal = (goal_x, goal_y)

    # Ensure start and goal are free
    grid[start[0]][start[1]] = 0
    grid[goal[0]][goal[1]] = 0

    print(f"\nStart: {start}, Goal: {goal}")

    dynamic_navigation(grid, start, goal)

run_simulation() 