
# Experiment 25: 8 Puzzle Problem using A* Search

import heapq

start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def heuristic(state):
    """Count tiles that are not in their goal positions."""
    return sum(
        1 for i, tile in enumerate(state)
        if tile != 0 and tile != goal[i]
    )


def get_neighbors(state):
    """Generate valid states by moving the blank tile."""
    zero = state.index(0)
    row, col = divmod(zero, 3)
    neighbors = []

    moves = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1)    # Right
    ]

    for dr, dc in moves:
        nr, nc = row + dr, col + dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            pos = nr * 3 + nc
            new_state = list(state)
            new_state[zero], new_state[pos] = (
                new_state[pos], new_state[zero]
            )
            neighbors.append(tuple(new_state))

    return neighbors


def solve(start, goal):
    queue = [(heuristic(start), 0, start)]
    parent = {start: None}
    cost = {start: 0}

    while queue:
        _, g, current = heapq.heappop(queue)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return path[::-1]

        if g != cost[current]:
            continue

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if new_cost < cost.get(neighbor, float("inf")):
                cost[neighbor] = new_cost
                parent[neighbor] = current
                priority = new_cost + heuristic(neighbor)
                heapq.heappush(
                    queue, (priority, new_cost, neighbor)
                )

    return None


def display(state):
    for i in range(0, 9, 3):
        print(*("." if x == 0 else x for x in state[i:i + 3]))
    print()


print("8 Puzzle Problem - A* Search")
solution = solve(start, goal)

if solution:
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        display(state)

    print("Total moves:", len(solution) - 1)
else:
    print("No solution found.")
