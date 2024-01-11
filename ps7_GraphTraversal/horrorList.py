from math import inf 
from collections import deque

V, H, E = map(int, input().split())

horrors = list(map(int, input().split()))
AL = [[] for _ in range(V)]

for _ in range(E):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)

dist = [inf] * V
visited = [False] * V
for u in horrors:
    dist[u] = 0

q = deque(horrors)

while q:
    u = q.popleft()
    visited[u] = True
    for v in AL[u]:
        if visited[v]: continue
        if dist[u] + 1 < dist[v]:
            dist[v] = dist[u] + 1
        q.append(v)
print(dist.index(max(dist)))

