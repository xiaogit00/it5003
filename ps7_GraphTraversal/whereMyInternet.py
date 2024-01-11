import sys

sys.setrecursionlimit(200000)
def dfs(s):
    global visited
    global AL

    visited[s] = True
    
    for v in AL[s]:
        if not visited[v]:
            dfs(v)

V, E = map(int, input().split())

AL = [ [] for _ in range(V+1) ]
AL[0] = None
for _ in range(E):
    a, b = map(int, input().split())
    AL[a].append(b)
    AL[b].append(a)

# print(AL)
visited = [False] * (V+1)
visited[0] = -1

dfs(1)
connected = True
for i, flag in enumerate(visited):
    if flag == False:
        print(i)
        connected = False
if connected: print('Connected')