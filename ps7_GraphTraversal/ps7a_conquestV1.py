def dfs(u):
  global AL
  global visited
  global weight
  global sum

  visited[u] = True
  sum += weight[u]
  for node in AL[u]:
    v = node
    if visited[v] == False:
        if sum > weight[v]:
            dfs(v)
        else:
            visited[v] = True
      

V, E = map(int, input().split())
edges = []
weight = [None] # Index 0 empty to correspond with 1-based indexing
for _ in range(E):
    edges.append(tuple(map(int, input().split())))
for _ in range(V):
    weight.append(int(input())) # Will contain V + 1 items, value node weight

AL = [[] for _ in range(V + 1)]
visited = [False for _ in range(V + 1)]
sum = 0
AL[0] = visited[0] = None # Index 0 empty for 1-based indexing


for edge in edges:
    v, u = edge[0], edge[1]
    AL[v].append(u)
    AL[u].append(v)

for i in range(1, V+1):
    if visited[i] == False:
        dfs(i)

print(sum)