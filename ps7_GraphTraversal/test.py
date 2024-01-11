import heapq
c = list(map(int, input().split()))
m = c[1]
n = c[0]
first = {}

for i in range(m):
    k = list(map(int, input().split()))
    if not first.get(k[0], 0):
        first[k[0]]=[]
    if not first.get(k[1], 0):
        first[k[1]]=[]
    first[k[0]].append(k[1])
    first[k[1]].append(k[0])

army = {}
for j in range(n):
    army[j+1] = int(input())

s = set()

def con(first, start, s):
    s.add(start)
    for co in first.get(start, []):
        if co not in s:
            con(first, co, s)
    return s

m1 = con(first, 1, s)
# print(m1)
m1.remove(1)
# print(m1)
l=[]

for fi in m1:
    l.append((army[fi], fi))
# print(l)
heapq.heapify(l)
if l:
    ini = army[1]
    t=heapq.heappop(l)
    while l:
        ini = ini+t[0]
        t = heapq.heappop(l)
    if ini>t[0]:
        ini = ini+t[0]
    print(ini)
    #     t = heapq.heappop(l)
    #     if ini>t[0]:
    #         ini = ini+t[0]
    #     else: break
    # print(ini)
else: 
    print(army[1])