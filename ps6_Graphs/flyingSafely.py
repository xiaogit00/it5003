def dfs(u):
    global AL
    global visited
    visited[u] = True # O(1)
    for i in AL[u]:
        if visited[i] == False:
            dfs(i)

def isConnected(a, b):
    global AL
    global visited
    dfs(a)
    if visited[a] and visited[b]:
        return True
    else:
        return False

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    AL = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    pilotCount = 0
    for i in range(m): 
        a, b = map(int, input().split())
        if isConnected(a, b):
            AL[a].append(b)
            AL[b].append(a)
            continue
        else:
            AL[a].append(b)
            AL[b].append(a)
            pilotCount += 1
    print(pilotCount)

'''
Alright, this solution works, but TLE. I think I know why. 

n is the number of cities. The upperbound is n = 1k. 
m is the number of pilots. 
m is also the number of edges. The upperbound is m = 10k. 

Let's examine the time complexity of my code. What is the number of nodes? 
V = 1k. 
E = 10k

When I create an AL, I am creating upwards of a list of 1001 lists. That's still ok. 

When I create visited, similarly, I am creating a list of 1001 False values. 
When I check for isConnected(a, b), I am calling dfs(a). Within dfs(a), visited[a] is O1. 
for i in AL[u] -> now here might be the offending operation. AL[u] could contain upwards of 10k items. 
for i in range(m) -> this is already O(m) which is 10k. 
Then, I run dfs, which contains for i in AL[u]

Basically, this method is very inefficient because *at every single input point, I am running an entirely
new DFS to check if the elements are connected. What if I 'memoize' the visited stamps, so that visited doesn't
have to be fresh every time? after all, if I visited one place, and I add the next element, it'll be visited too. 

Can I do it another way? Yes, I still need to check if the elements are connected. But why can't I just 
add something to the CC whenever I know it's connected? cc = set()
If input = (1, 2), then cc.add(1), cc.add(2)
if input = (2, 3), then cc.add(2), cc.add(3)  -> {1, 2, 3}
if input = (1, 3), if both 1 and 3 are in CC, then don't add. 

So maybe this qn don't even need dfs?? Is it possible? 



'''