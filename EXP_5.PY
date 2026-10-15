
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

def safe(m, c):
    if not (0 <= m <= 3 and 0 <= c <= 3):
        return False
    mr, cr = 3 - m, 3 - c
    return (m == 0 or m >= c) and (mr == 0 or mr >= cr)

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()
    if state == goal:
        for s in path:
            print(s)
        break

    m, c, boat = state
    for dm, dc in moves:
        if boat == 1:
            nxt = (m - dm, c - dc, 0)
        else:
            nxt = (m + dm, c + dc, 1)

        if safe(nxt[0], nxt[1]) and nxt not in visited:
            visited.add(nxt)
            queue.append((nxt, path + [nxt]))
