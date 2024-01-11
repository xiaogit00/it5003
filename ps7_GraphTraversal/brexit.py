from collections import deque
from copy import deepcopy
    
V, E, x, l = map(int, input().split())

AL = [[] for _ in range(V+1)]
AL[0] = None
neighbourCount = [0] * (V+1)
for _ in range(E):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)
    neighbourCount[a] += 1
    neighbourCount[b] += 1
originalNeighbourCount = deepcopy(neighbourCount)
q = deque([l])
left = [False]*(V+1)
left[l] = True

while q:
    u = q.popleft()
    for v in AL[u]:
        if left[v]: continue
        neighbourCount[v] -=1
        if neighbourCount[v]*2 <= originalNeighbourCount[v]:
            q.append(v)
            left[v] = True
print('leave') if left[x] else print('stay')
