from math import inf
from heapq import heappush, heappop
while True:
    V, E, q, s = map(int, input().split())
    if V == 1: break
    AL = [[] for _ in range(V)]
    dist = [inf for _ in range(V)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        AL[u].append((v, w)) 

    pq = [(-1, s)] # shorter than the two lines above
    while pq: # main loop
        d, u = heappop(pq) # shortest unvisited u
        print('value of u:', u)
        if d > dist[u]: continue # a very important check
        for v, w in AL[u]: # all edges from u
            if dist[u]+w >= dist[v]: continue # not improving, skip
            dist[v] = dist[u]+w # relax operation
            heappush(pq, (dist[v], v))
    for _ in range(q):
        t = int(input())
        print("Impossible" if dist[t] == inf else dist[t])
    print()
