from heapq import heappush, heappop

def search(u):
    global AL
    global visited
    global weight
    global sum
    visited[u] = True
    for node in AL[u]:
        v = node
        if visited[v] == False:
            if sum > weight[v]:
                sum+=weight[v]
                dfs(v)
            else:
                visited[v] = True
                heappush(unconquered, (weight[v], v))
                
V, E = map(int, input().split())
edges = []
weight = [None] # Index 0 empty to correspond with 1-based indexing
unconquered = []

for _ in range(E):
    edges.append(tuple(map(int, input().split())))
for _ in range(V):
    weight.append(int(input())) # Will contain V + 1 items, value node weight

AL = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
sum = 0
AL[0] = visited[0] = None # Index 0 empty for 1-based indexing
sum+=weight[1]


for edge in edges:
    v, u = edge[0], edge[1]
    AL[v].append(u)
    AL[u].append(v)

print(AL)
search(1)
# while True and unconquered:
#     (w, v) = heappop(unconquered)
#     if sum > w:
#         sum+=w
#         dfs(v)
#     else: 
#         break

print(sum)