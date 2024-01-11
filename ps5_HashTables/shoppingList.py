from collections import defaultdict 

n, m = map(int, input().split())
d = defaultdict(lambda: 0)

for _ in range(n):
    items = input().split()
    items = set(items)
    for i in items:
        d[i] += 1
foundItems = []
for k, v in d.items():
    if v == n:
        foundItems.append(k)

foundItems.sort()
print(len(foundItems))
for i in foundItems:
    print(i)