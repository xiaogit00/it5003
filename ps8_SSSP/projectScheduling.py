from collections import defaultdict, deque

def dfs(s):
    global AL
    global visited
    global order

    visited[s] = True

    for v, w in AL[s]:
        if not visited[v]:
            dfs(v)
    order.append(s)

T = int(input())
input()
for i in range(T):
    AL = defaultdict(list)
    visited = defaultdict(lambda: False)
    order = []
    AL[0] = [] # dummySource    
    n = 0
    while True:
        line = input()
        if line == '':
            break
        n+=1
        line = line.split()
        if len(line) == 2: # no inbound = source
            v, w = line[0], int(line[1])
            AL[0].append((v, w))
        if len(line) == 3: # have inbound
            v, w, U = line[0], int(line[1]), line[2]
            for u in U:
                AL[u].append((v, w))
    dfs(0)
    order.reverse()
    
    dist = defaultdict(lambda: 0)
    dist[0] = 0
    q = deque([])
    q.append(0)

    max = 0
    while q:
        u = q.popleft()
        for v, w in AL[u]:
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                if max < dist[v]:
                    max = dist[v]
                q.append(v)
    print(max)

'''
DP into source to find  the *longest path* -> how do I find longest path? 
I think this is just a reverse in logic: if d + w > dv, set dv to d+w ; subtlety: 
set default dist to 0 for each node. 

So to implement DP, I just need a dist variable, a pq which begins at 0, that's it
'''