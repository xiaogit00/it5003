from math import inf 
from heapq import heappush, heappop

n = int(input())
if n==0:
    print('-')
    exit()

n = n+2
locs = []

for _ in range(n):
    x, y = map(int, input().split())
    locs.append((x, y))

AL = [[] for _ in range(n)]
dist = [inf] * n
parent = [-1] * n
visited = [False] * n

for u in range(n):
    for v in range(n):
        if u==v: continue
        (x1, y1) = locs[u]
        (x2, y2) = locs[v]
        w = (x1-x2)**2 + (y1-y2)**2
        AL[u].append((w, v)) # w is the sweat produced
pq = []
# print(AL)
dist[n-2] = 0 
visited[n-2] = True
heappush(pq, (0, n-2))
while pq:
    d, u = heappop(pq)
    visited[u] = True
    if d > dist[u]: continue
    for w, v in AL[u]:
        if visited[v]: continue
        # print('exploring v: ', v, 'from u: ', u)
        if dist[u] + w < dist[v]: 
            dist[v] = dist[u] + w
            parent[v] = u
            heappush(pq, (dist[v], v))
print(dist[n-1])
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

# # '''
# # 1. Creating the AL
# # 2. Push source (n-2) into pq, distance 0
# # 3. Run dijkstra from source
# # - For every neighbour, check its distance 
# # - I should have an early termination: if d >= dist[n-1]: continue
# # - the result of this is a dist[] variable with the shortest distance, along with parent 
# # - dist[n-1] currently stores shortest distance. 
# # 4. I've got the parent - I'll need to print the path
# # '''