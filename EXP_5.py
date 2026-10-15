
from collections import deque

start = (3, 3, 1)
goal = (0, 0, 0)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]

queue = deque([(start, [start])])
visited = {start}

while queue:
    state, path = queue.popleft()
    m, c, boat = state

    if state == goal:
        print("Solution:")
        for step in path:
            print(step)
        break

    for dm, dc in moves:
        if boat == 1:
            nm, nc, nb = m - dm, c - dc, 0
        else:
            nm, nc, nb = m + dm, c + dc, 1

        if 0 <= nm <= 3 and 0 <= nc <= 3:
            rm, rc = 3 - nm, 3 - nc

            if (nm == 0 or nm >= nc) and (rm == 0 or rm >= rc):
                nxt = (nm, nc, nb)

                if nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, path + [nxt]))
