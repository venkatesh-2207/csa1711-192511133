
# Map Coloring using CSP

colors = ["Red", "Green", "Blue"]

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "D"],
    "C": ["A", "B", "D"],
    "D": ["B", "C"]
}

color = {}

def solve(node):
    if node == len(graph):
        return True

    region = list(graph.keys())[node]

    for c in colors:
        valid = True

        for neighbor in graph[region]:
            if color.get(neighbor) == c:
                valid = False
                break

        if valid:
            color[region] = c

            if solve(node + 1):
                return True

            del color[region]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for region in color:
        print(region, ":", color[region])
else:
    print("No solution found")
