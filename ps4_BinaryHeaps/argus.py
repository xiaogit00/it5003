from heapq import heappop, heappush, heapify

k = 0
pq = []
while True:
    line = input()
    if line == '#':
        k = int(input())
        break
    pq.append(line)

pq = [tuple(map(int, line.split()[:0:-1] + line.split()[:1:-1])) for line in pq]

heapify(pq)
i = 0

while i < k:
    res = heappop(pq)
    print(res[1])
    heappush(pq, (res[0]+res[2], res[1], res[2]))
    i+=1
