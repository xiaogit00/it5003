n = int(input())

def dfs(u):
  global AL
  global visited

  visited[u] = True
  for v in AL[u]:
    if visited[v] == False:
      dfs(v)

for _ in range(n):
    m = int(input()) #nodes
    r = int(input()) #edges
    AL = [[] for i in range(m)]
    visited = [False for i in range(m)]
    for _ in range(r):
       v, u = map(int, input().split())
       AL[v].append(u) # AL is constructed. 
       AL[u].append(v)
    # print(AL)
    numCC = 0
    for i in range(m):
       if visited[i] == False:
          numCC+=1
          dfs(i)
    print(numCC-1)

'''
What's the basic idea of creating an AL? 
It's a list with m items. 

What's the basic idea of dfs? Can I try to implement from scratch? =/ Should I? 
Nah maybe I'll use what I have and modify. 

Okay that was simple. 
Now
'''