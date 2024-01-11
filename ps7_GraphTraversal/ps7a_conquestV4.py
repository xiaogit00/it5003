from heapq import heappush, heappop

V, E = map(int, input().split())

AL = [[] for _ in range(V)]
size = []
visited = [False] * V

for _ in range(E):
    a, b = map(lambda x: int(x)-1, input().split())
    AL[a].append(b)
    AL[b].append(a)

for _ in range(V):
    size.append(int(input()))

pq = []

sum = size[0]
visited[0] = True

for u in AL[0]:
    heappush(pq, (size[u], u))

while pq:
    n, u = heappop(pq)
    visited[u] = True
    if sum > n:
        sum += n
        for v in AL[u]:
            if not visited[v]:
                heappush(pq, (size[v], v))
    else: 
        print(sum)
        exit()