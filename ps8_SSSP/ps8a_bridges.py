from heapq import heappush, heappop
from math import inf
V, E = map(int, input().split())
AL = [[] for _ in range(V+1)]
AL[0] = None
d = [inf for _ in range(V+1)]
d[1] = 0
q = [(d[1], 1)]
for _ in range(E):
    a, b, w = map(int, input().split())
    AL[a].append((b, w))
    AL[b].append((a, w))
while q:
    (w, u) = heappop(q)
    if w > d[u]: continue
    for v, wuv in AL[u]:
        if d[u] + wuv < d[v]:
            d[v] = d[u] + wuv
            heappush(q, (d[v], v))
print(d[V])
