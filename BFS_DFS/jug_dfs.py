capacity1 = 4
capacity2 = 3
goal = 2

visited = set()

def dfs(a,b):

    if (a,b) in visited:
        return

    print("State:",(a,b))
    visited.add((a,b))

    if a == goal or b == goal:
        print("Goal Reached!")
        return

    next_states = [
        (capacity1,b),
        (a,capacity2),
        (0,b),
        (a,0)
    ]

    pour = min(a, capacity2-b)
    next_states.append((a-pour, b+pour))

    pour = min(b, capacity1-a)
    next_states.append((a+pour, b-pour))

    for state in next_states:
        dfs(state[0],state[1])

dfs(0,0)
