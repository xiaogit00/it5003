import sys
from heapq import heapify, heappop, heappush

'''
Here it's worth noting that the number of books that Anna has and that her friends
will give her is rather large - 100k for each. n and m are large. 
'''
n = m = k = 0
pile = []
gifts = []

for i, line in enumerate(sys.stdin):
    if line.strip() == '':
        break
    if i == 0:
        [n, m, k] = list(map(int, line.strip().split()))
    if 0 < i <= n:
        parts = line.strip().split()
        title = ' '.join(parts[:-1]).replace('"', '')
        pages = int(parts[-1])
        pile.append((title, pages))
    elif n < i <= n + m:
        parts = line.strip().split()
        giftTime = int(parts[0])
        title = ' '.join(parts[1:-1]).replace('"', '')
        pages = int(parts[-1])
        gifts.append((giftTime, title, pages))

time = 0

heapify(pile)
heappush(pile, ("Jane Eyre", k))
heapify(gifts)
# print(gifts[0][0])
res = (None, None)
while res[0] != 'Jane Eyre':
    while len(gifts)>0 and gifts[0][0] <= time:
        res = heappop(gifts)
        heappush(pile, (res[1], res[2]))
    res = heappop(pile)
    
    time += res[1]
print(time)

'''
What about a case where there are no more gifts? - it'll just keep popping until it reaches Jane Eyre
right. 
'''