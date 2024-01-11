'''
The question here is: could I try to implement Djikstra? What's the main idea of djikstra?
I think the main idea is, to make use of a priority queue. 
Modified Djikstra, that is. I'll iterate through the neighbours of s. 

For each neighbour, add to PQ. Then, I'll pop the smallest in terms of weight. I'll visit
all its neighbous, and if d[u] + w < d[v], then relax(v, u, w). Hmm pretty intuitive
'''
from heapq import heappop, heappush 
from math import inf

while True:
    n, m, q, s = map(int, input().split())
    if n == 0: break
    AL = [[] for _ in range(n)]
    d = [inf for _ in range(n)]
    d[0] = 0
    pq = []
    heappush(pq, (d[0], 0))

    for _ in range(m):
        u, v, w = map(int, input().split())
        AL[u].append((v, w)) 
    
    while pq:
        (w, u) = heappop(pq)
        if w > d[u]: continue
        for (v, wuv) in AL[u]: # for each neighbour v in u
            if d[u] + wuv < d[v]:
                d[v] = d[u] + wuv
                heappush(pq, (d[v], v))
    for _ in range(q):
        v = int(input())
        if d[v] < inf:
            print(d[v])
        else: 
            print('Impossible')
    print()
