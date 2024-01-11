from heapq import heappush, heappop
from math import inf

n, s, t = map(int, input().split())
AM = [list(map(int, input().split())) for _ in range(n)]
dist = [inf] * n
dist[s] = 0
pq = []

heappush(pq, (dist[s], s))

while pq:
    d, u = heappop(pq)
    if d > dist[u]: continue
    for v, w in enumerate(AM[u]):
        if w == 0: continue 
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            heappush(pq, (dist[v], v))
print(dist[t])
'''


2. How do you run Dijkstra on AM? 

source = s
push((0, s))

while pq:
d, u = pop
for w, u in AM[
'''