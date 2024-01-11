from collections import deque 
from collections import defaultdict 
from math import inf

n, m = map(int, input().split())
nums = defaultdict(list)
grid = [[] for _ in range(n)]
dist = defaultdict(lambda: inf) # distance shortest distance of each coord
for i in range(n):
    numbers = list(map(int, input().split()))
    for j, num in enumerate(numbers):
        grid[i].append(num)
        nums[num].append((i, j))
# The AL for each item in 1 is simply all of the 2s; the AL for each item in 2 is 
# simply all of the 3s, so on. 

ordering = deque([])
# Add all the sequences in order
for i in range(1,m+1):
    for item in nums[i]:
        ordering.append(item)
min = inf
if m == 1: 
    print(0)
    exit()
while ordering:
    U = ordering.popleft()
    x, y = U[0], U[1]
    level = grid[x][y]
    if level < m and len(nums[level+1]) == 0:
        print(-1)
        exit()
    if level == m: continue
    if level == 1: dist[U] = 0
    for V in nums[level+1]:
        x1, y1 = V[0], V[1]
        d = abs(x1 - x) + abs(y1 - y)
        if dist[U] + d < dist[V]:
            dist[V] = dist[U] + d
            if level == m-1 and dist[V] < min:
                min = dist[V]
print(min)
