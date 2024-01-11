'''
First, I'll need to count the number of occurence of an array of numbers.
{
    1: 3
    2: 5
    3: 7
}

I'll iterate through the values and add them by key
'''
import sys
from heapq import heappop, heappush, heapify

nums = []
for i, line in enumerate(sys.stdin):
    if line.strip() == '':
        break
    if i == 0:
        [n, k] = list(map(int, line.split()))
    elif i == 1:
        nums = list(map(int, line.split()))

counts = {}
for num in nums:
    counts[num] = counts.get(num, 0) + 1

pq = [(-x[1], -x[0]) for x in list(counts.items())]

# print(pq)
heapify(pq)

i=0
while i < k:
    res = heappop(pq)
    heappush(pq, (res[0]+1, res[1]))
    i+=1
print(-heappop(pq)[0])