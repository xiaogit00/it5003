from collections import defaultdict 
from heapq import heappush, heappop
from math import inf

n = int(input())
locs = []
n = n+2

for _ in range(n):
    x, y = map(int, input().split())
    locs.append((x, y))

s = n-2
dest = n-1
dist = [inf] * n
dist[s] = 0
pq = []
parent = [-1] * n
visited = [False] * n
heappush(pq, (dist[s], s))

while pq:
    d, u = heappop(pq)
    visited[u] = True
    if d > dist[u]: continue
    neighbours = []
    for i, v in enumerate(locs):
        if i == u or visited[i]: continue
        x, y = locs[u][0], locs[u][1]
        x1, y1 = v[0], v[1]
        w = (x1-x)**2 + (y1-y)**2
        neighbours.append((w, i))
    for w, v in neighbours:
        if dist[u] + w < dist[v]:
            dist[v] = dist[u] + w
            parent[v] = u
            heappush(pq, (dist[v], v))

path = []
curr = parent[n-1] #index
while curr!=n-2:
    path.append(curr)
    curr = parent[curr]
path.reverse()

for i in path:
    print(i)
if not path: 
    print('-')