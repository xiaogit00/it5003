from heapq import heappush, heappop

k, n = map(int, input().split())

karl_year, karl_str = map(int, input().split())

contestants = []

for _ in range(n+k-2):
    yr, str = map(int, input().split())
    contestants.append((yr, str))

contestants.append((karl_year, karl_str))

contestants.sort(reverse = True)
pq = []

for _ in range(k):
    yr, str = contestants.pop()
    heappush(pq, (-str, yr))
    
while contestants:
    str, yr = heappop(pq)
    if -str == karl_str and yr == karl_year:
        print(yr)
        exit()
    yr2, str2 = contestants.pop()
    heappush(pq, (-str2, yr2))

print('unknown')

    