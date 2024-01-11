def dfs(u, parent):
  global AL
  global visited
  global p
  global counter

  visited[u] = True
  for v in AL[u]:
    if visited[v] and v != parent:
       # Backedge found at node u -> I'll need to find out cycle length and break
       i = u
       while True:
          if p[i] != v:
             i = p[i]
             counter += 1
          else:
             counter += 1
             if counter%2 == 1:
                print("impossible")
                exit()
             else:
                exit()
    elif visited[v] == False:
      p[v] = u
      dfs(v, u)

V = int(input()) #num vertices
E = int(input()) #num edges
AL = [[] for i in range(E)]
visited = [False for i in range(E)]
p = [-1 for i in range(V)]
counter = 1
for _ in range(E):
    v, u = map(int, input().split())
    AL[v].append(u) # AL is constructed. 
    AL[u].append(v)

parent = -1
for u in range(E):
    if visited[u] == False:
        dfs(u, parent)
print(counter)