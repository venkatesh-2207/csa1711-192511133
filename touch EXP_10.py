
import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('G', 2)],
    'F': [('G', 2)],
    'G': []
}

h = {'A': 4, 'B': 3, 'C': 4, 'D': 2, 'E': 1, 'F': 2, 'G': 0}

def astar(start, goal):
    queue = [(h[start], 0, start, [start])]
    visited = set()

    while queue:
        f, cost, node, path = heapq.heappop(queue)

        if node == goal:
            print("Path:", path)
            print("Total cost:", cost)
            return

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                new_cost = cost + weight
                heapq.heappush(
                    queue,
                    (new_cost + h[neighbor], new_cost,
                     neighbor, path + [neighbor])
                )

astar('A', 'G')
