from collections import defaultdict
from heapq import heappush, heappop
import sys

input = sys.stdin.readlines()
n, k = map(int, input[0].split())
nums = list(map(int, input[1].split()))
d = defaultdict(lambda: 0)
for num in nums:
    d[num] += 1

pq = []

for key, value in d.items():
    heappush(pq, (-value, key))

for _ in range(k):
    m, i = heappop(pq)
    heappush(pq, (m+1, i))
print(-pq[0][0])
