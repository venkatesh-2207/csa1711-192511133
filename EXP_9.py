
from itertools import permutations

cities = ["A", "B", "C", "D"]

cost = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

min_cost = float("inf")
best_route = []

for p in permutations(range(1, 4)):
    route = (0,) + p + (0,)
    total = 0

    for i in range(len(route) - 1):
        total += cost[route[i]][route[i + 1]]

    if total < min_cost:
        min_cost = total
        best_route = route

print("Best Route:")
print(" -> ".join(cities[i] for i in best_route))
print("Minimum Cost:", min_cost)
