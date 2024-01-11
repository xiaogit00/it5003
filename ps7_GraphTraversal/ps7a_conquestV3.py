from heapq import heappush, heappop

from enum import Enum

class flag(Enum):
  UNEXPLORED = -1
  EXPLORED = -2
  VISITED = -3

def dfs(u):
    global AL
    global visited
    global weight
    global sum
    visited[u] = flag.VISITED.value
    for node in AL[u]:
        v = node
        if visited[v] == flag.UNEXPLORED.value:
            if sum > weight[v]:
                sum+=weight[v]
                dfs(v)
            else:
                visited[v] = flag.EXPLORED.value
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
visited = [flag.UNEXPLORED.value for _ in range(V + 1)]
sum = 0
AL[0] = visited[0] = None # Index 0 empty for 1-based indexing
sum+=weight[1]


for edge in edges:
    v, u = edge[0], edge[1]
    AL[v].append(u)
    AL[u].append(v)

dfs(1)
while True and unconquered:
    (w, v) = heappop(unconquered)
    if sum > w:
        sum+=w
        dfs(v)
    else: 
        break

print(sum)

'''
Test cases
10 10
1 2
2 3
3 4
3 5
4 5
2 6
6 7
6 8
8 9
9 10
4
3
5
6
80
11
50
13
14
15

3 3
1 2
1 3
2 3
2
4
4

7 6
1 2
2 3
1 4
4 5
5 6
6 7
4
5
7
3
2
20
100

4 3
1 2
2 4
1 3
4
5
5
3
'''