from heapq import heappush, heappop
from math import inf


n, m = map(int, input().split())
AL = [[] for _ in range(n+1)]
AL[0] = None
dist = [inf] * (n+1)
dist[0] = None
dist[1] = 0

for _ in range(m):
    a, b, w = map(int, input().split())
    AL[a].append((b, w))
    AL[b].append((a, w))

pq = []
heappush(pq, (dist[1], 1))

while pq:
    d, u = heappop(pq)
    if d > dist[u]: continue
    for v, w in AL[u]:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))

print(dist[n])