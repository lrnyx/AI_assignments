# UGV Pathfinding and Search Algorithms

This project covers three different pathfinding problems that are commonly studied in AI:

1. Finding shortest paths between cities using Dijkstra’s algorithm  
2. Navigating a UGV in a grid with static obstacles using A*  
3. Handling dynamic obstacles using replanning  

---

## Part 1: Dijkstra’s Algorithm (Indian Cities)

In this part, cities are treated as nodes and road distances as weighted edges.

- The graph is built using a CSV file
- Dijkstra’s algorithm is used to compute shortest distances
- The user can:
  - Enter any starting city
  - Ask for distance to a specific city or all cities
- Input is handled in a case-insensitive way

This part demonstrates how shortest path algorithms work on real-world data.

---

## Part 2: UGV Navigation with Static Obstacles

Here, a battlefield is modeled as a grid (conceptually 70×70 km).

- Each cell can be:
  - 0 -> free
  - 1 -> obstacle
- Obstacles are generated randomly with different densities:
  - Low (0.1)
  - Medium (0.25)
  - High (0.4)

The A* algorithm is used to find the shortest path from a start point to a goal point.

### Features:
- User-defined start and goal coordinates
- Avoids obstacles while finding the shortest path
- Prints:
  - Path length
  - Nodes expanded
  - Execution time

### Observation:
As obstacle density increases, it becomes harder to find a valid path.

---

## Part 3: UGV Navigation with Dynamic Obstacles

In this part, obstacles are not fixed. They can appear while the robot is moving.

- The UGV starts moving along a path found by A*
- If a new obstacle appears:
  - The current path is no longer valid
  - A new path is computed from the current position

This simulates a more realistic environment where the robot has to continuously adapt.


