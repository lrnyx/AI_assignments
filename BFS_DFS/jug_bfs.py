from collections import deque

capacity1 = 4
capacity2 = 3
goal = 2

def bfs():

    visited = set()
    queue = deque([(0,0)])

    while queue:

        a,b = queue.popleft()

        if (a,b) in visited:
            continue

        print("State:", (a,b))
        visited.add((a,b))

        if a == goal or b == goal:
            print("Goal Reached!")
            return

        next_states = [
            (capacity1,b),   # fill jug1
            (a,capacity2),   # fill jug2
            (0,b),           # empty jug1
            (a,0)            # empty jug2
        ]

        pour = min(a, capacity2-b)
        next_states.append((a-pour, b+pour))

        pour = min(b, capacity1-a)
        next_states.append((a+pour, b-pour))

        for state in next_states:
            if state not in visited:
                queue.append(state)

bfs()