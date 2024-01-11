from heapq import heappush, heappop
from collections import defaultdict
from math import inf

n, k = map(int, input().split())
nums = defaultdict(list)
order = []
d = defaultdict(lambda: inf)

for r in range(n):
    line = list(map(int, input().split()))
    for c, item in enumerate(line): 
        nums[item].append((r, c)) # A dict of list of values of each num
        heappush(order, (item, (r, c))) # (k, (x, y))
if k == 1: 
    print(0)
    exit()
min = inf
while order:
    (level, U) = heappop(order) 
    if level < k and len(nums[level+1]) == 0:
        print(-1)
        exit()
    if level == k:
        if d[U] < min:
            min = d[U]
        continue
    for V in nums[level+1]:
        wuv = abs(V[0] - U[0]) + abs(V[1] - U[1])
        if level == 1: d[U] = 0
        if d[U] + wuv < d[V]:
            d[V] = d[U] + wuv

print(min)

# This is an implementation of DP for DAGs