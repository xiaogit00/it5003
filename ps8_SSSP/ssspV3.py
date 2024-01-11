from math import inf
from heapq import heappush, heappop
def runQuery(AL, s, dist, q):
    pq = []
    heappush(pq, (0, s)) 
    while pq:
        d, u = heappop(pq)
        #Notes on d vs dist[u] -> while dist[u] is the bona fide shortest path, d 
        # can contain stale neighbour weights that were added to PQ but got pushed back
        # to the queue as we updated node u with a shorter dist[u] + wuv
        if d>dist[u]: continue # this is important for modified dijkstra - lazy deletion! 
        #^ above line reads: if stale, delete. 
        
        for v, wuv in AL[u]:
            if dist[u] + wuv < dist[v]:
                dist[v] = dist[u] + wuv
                heappush(pq, (dist[v], v))
    if dist[q] != inf:
        print(dist[q])
    else: 
        print('Impossible')

while True:
    line = input()
    if line == '0 0 0 0': exit()
    n, m, q, s = map(int, line.split())
    AL = [[] for _ in range(n)]
    dist = [inf] * n
    dist[s] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        AL[u].append((v, w))
        
    for _ in range(q):
        runQuery(AL, s, dist, int(input()))

'''
So I've got an AL, the source, and q - I'll need to construct a dist[] variable

'''