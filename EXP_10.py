
import heapq

graph = {
    "A": [("B", 1), ("C", 4)],
    "B": [("C", 2), ("D", 5)],
    "C": [("D", 1)],
    "D": []
}

h = {"A": 4, "B": 3, "C": 1, "D": 0}

queue = [(h["A"], 0, "A", ["A"])]
visited = set()

while queue:
    f, cost, node, path = heapq.heappop(queue)

    if node == "D":
        print("Path:", path)
        print("Cost:", cost)
        break

    if node in visited:
        continue

    visited.add(node)

    for next_node, edge_cost in graph[node]:
        new_cost = cost + edge_cost
        priority = new_cost + h[next_node]
        heapq.heappush(
            queue,
            (priority, new_cost, next_node, path + [next_node])
        )
