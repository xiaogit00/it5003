
def dfs(s):
    global AL
    global visited

    visited[s] = True
    for u in AL[s]:
        if not visited[u]:
            dfs(u)

T = int(input())

for _ in range(T):
    V = int(input())
    E = int(input())
    AL = [[] for _ in range(V)]
    visited = [False]*V
    cc = 0
    for _ in range(E):
        a, b = map(int, input().split())
        AL[a].append(b)
        AL[b].append(a)
    
    for u in range(V):
        if not visited[u]:
            cc += 1
            dfs(u)
    
    print(cc-1)