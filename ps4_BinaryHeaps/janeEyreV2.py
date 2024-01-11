from heapq import heappush, heappop

n, m, k = map(int, input().split())
unread = []
gifts = []

for _ in range(n):
    line = input().split()
    title, page = line[:-1], int(line[-1])
    title = ' '.join(title).replace('"', '')
    heappush(unread, (title, page))
heappush(unread, ('Jane Eyre', k))

for _ in range(m):
    line = input().split()
    time, title, page = int(line[0]), line[1:-1], int(line[-1])
    title = ' '.join(title).replace('"', '')
    heappush(gifts, (time, title, page))

time = 0

while gifts[0][0]==0:
    newbook = heappop(gifts)
    heappush(unread, (newbook[1], newbook[2]))

while unread:
    title, page = heappop(unread)
    if title == 'Jane Eyre':
        print(time + page)
        exit()
    time += page
    while len(gifts)>0 and time >= gifts[0][0]:
        newbook = heappop(gifts)
        heappush(unread, (newbook[1], newbook[2]))
