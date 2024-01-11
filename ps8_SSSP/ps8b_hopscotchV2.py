from heapq import heappush, heappop
from collections import defaultdict
from math import inf

n, k = map(int, input().split())
nums = defaultdict(list)
grid = []

for i in range(n):
    line = list(map(int, input().split()))
    for j, item in enumerate(line): 
        nums[item].append((i, j))
    grid.append(line)

def SP(V, d):
    global minDistance

    if d > minDistance: return

    r, c = V[0], V[1]
    level = grid[r][c]
    if level < k and len(nums[level+1]) == 0:
        print(-1)
        exit()
    if level == k:
        if  d < minDistance: minDistance = d
        return
    AL = []
    for neighbour in nums[level+1]:
        r2, c2 = neighbour[0], neighbour[1]
        w = abs(r2-r) + abs(c2-c)
        if w > minDistance: return
        heappush(AL, (w, (r2, c2))) # AL sorted by min d first
    while AL:
        (w, U) = heappop(AL)
        SP(U, w+d)

globalShortest = []

for V in nums[1]:
    minDistance = inf
    SP(V, 0)
    if minDistance == k:
        print(k)
        exit()
    heappush(globalShortest, minDistance)

print(heappop(globalShortest))