import heapq
import random
import time


def generate_grid(size, density):
    return [[1 if random.random() < density else 0 for _ in range(size)] for _ in range(size)]


# A* Algorithm
def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    def heuristic(a, b):
        # Manhattan distance
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_list = [(0, start)]
    g_cost = {start: 0}
    parent = {}
    nodes_expanded = 0

    while open_list:
        _, current = heapq.heappop(open_list)
        nodes_expanded += 1

        if current == goal:
            # Reconstruct path
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1], nodes_expanded

        x, y = current

        # Possible movements
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_cost = g_cost[current] + 1

                if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                    g_cost[(nx, ny)] = new_cost
                    priority = new_cost + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (priority, (nx, ny)))
                    parent[(nx, ny)] = current

    return None, nodes_expanded


def run_simulation():
    size = 30  

    densities = {
        "Low": 0.1,
        "Medium": 0.25,
        "High": 0.4
    }

    print("UGV Navigation using A* Algorithm")
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

    print(f"\nStart: {start}, Goal: {goal}")

    for level, density in densities.items():
        print(f"\n--- {level} Density ({density}) ---")

        grid = generate_grid(size, density)

        # Ensure start and goal are not blocked
        grid[start[0]][start[1]] = 0
        grid[goal[0]][goal[1]] = 0

        start_time = time.time()
        path, nodes = a_star(grid, start, goal)
        end_time = time.time()

        if path:
            print("Path found!")
            print("Path length:", len(path))
            print("Sample path (first 10 steps):", path[:10], "...")
        else:
            print("No path found")

        print("Nodes expanded:", nodes)
        print("Execution time:", round(end_time - start_time, 5), "seconds")


run_simulation()


