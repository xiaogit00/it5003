import sys
from collections import defaultdict

sys.setrecursionlimit(200000)

def dfs(s):
    global AL
    global visited
    global order

    visited[s] = True
    for u in AL[s]:
        if not visited[u]:
            dfs(u)
    order.append(s)
n = int(input())

AL = defaultdict(list)
visited = defaultdict(list)

for _ in range(n):
    l = input().split()
    for u in l[1:]:
        AL[u].append(l[0][:-1])
s = input()
order = []
dfs(s)
order.reverse()
for i in order:
    print(i)