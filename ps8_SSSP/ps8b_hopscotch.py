from dataclasses import dataclass
from heapq import heappush, heappop

@dataclass
class Node:
    coordinate: (int, int)
    level: int
    totalDistance: int
    distFromPred: int

n, k = map(int, input().split())
ones = []
grid = []


for i in range(n):
    line = list(map(int, input().split()))
    for j, item in enumerate(line): 
        if item == 1:
            ones.append((i, j))
    grid.append(line)

for s in ones:
    S = Node(s, 1, 0, 0)
    pq = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    latestLevel = 1
    heappush(pq, (S.totalDistance, S.level, S))
    while pq:
        N = heappop(pq) # Predecessor, smallest totalDistance node. 
        r, c = N.coordinate[0], N.coordinate[1]
        visited[r][c] = True
        if N.level <= latestLevel: continue #Lazy Deletion of PQ for the levels less than latest e.g. if ur looking for 2, the 1s don't matter anymore
        neighbours = [(r, c-1), (r-1, c), (r, c+1), (r+1, c)] # L, U, R, D
        for (r2, c2) in neighbours:
            if r2<0 or r2>n-1 or c2<0 or c2>n-1: continue # Eliminate out of bound 'neighbours'
            if visited[r2][c2]: continue # Don't add visited neighbours
            distanceFromPred = abs(r2-r) + abs(c2 - c) # Distance of neighbour from predecessor
            V = Node((r2, c2), grid[r2][c2], N.totalDistance + 1, distanceFromPred) # Neighbour node
            heappush(pq, (V.totalDistance, V.level, V))
