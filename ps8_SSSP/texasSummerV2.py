'''
This is the chatGPT answer
'''
import heapq

n = int(input())

n += 2

locs = []
for _ in range(n):
    x, y = map(int, input().split())
    locs.append((x, y))

adjlist = [[] for _ in range(n)]
dist = [float('inf')] * n
parent = [-1] * n
pq = []

for u in range(n):
    for v in range(n):
        if u == v:
            continue
        (x1, y1) = locs[u]
        (x2, y2) = locs[v]
        w = (x1 - x2) ** 2 + (y1 - y2) ** 2
        adjlist[u].append((w, v))

dist[n - 2] = 0
heapq.heappush(pq, (0, n - 2))
while pq:
    d, u = heapq.heappop(pq)
    if d > dist[u]: continue
    for w, v in adjlist[u]:
        if dist[u] + w >= dist[v]:
            continue
        dist[v] = dist[u] + w
        parent[v] = u
        heapq.heappush(pq, (dist[v], v))

path = []
cur_node = parent[n - 1]
while cur_node != n - 2:
    path.append(cur_node)
    cur_node = parent[cur_node]
path.reverse()

for i in path:
    print(i)
if not path:
    print('-')