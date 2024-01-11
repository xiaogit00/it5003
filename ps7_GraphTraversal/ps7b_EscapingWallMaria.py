import sys

sys.setrecursionlimit(200000)

t, N, M = map(int, input().split())

grid = []
d = [[0 for _ in range(M)] for _ in range(N)]
s = None
prev = (-1, -1)
paths = []

def dfs(s):
    global grid
    global d 
    
    r, c = s[0], s[1]
    print('value of s', s, 'value of d: ', d[r][c])
    if r == 0 or r == N-1 or c == 0 or c == M-1:
        if d[r][c] <= t: 
            paths.append(d[r][c])
            return 

    neighbours = [(r, c-1, 'R'), (r-1, c, 'D'), (r, c+1, 'L'), (r+1, c, 'U')] # Third variable is the direction coming from
    for pos in neighbours:
        if (d[pos[0]][pos[1]]) != 0 or (pos[0], pos[1]) == s:
            continue
        elif grid[pos[0]][pos[1]]  == '0':
            d[pos[0]][pos[1]] += d[r][c] + 1
            dfs((pos[0], pos[1]))
        elif (grid[pos[0]][pos[1]] in ['L', 'U', 'R', 'D']) and grid[pos[0]][pos[1]] == pos[2]: # ..and if letter same as direction coming from
            d[pos[0]][pos[1]] += d[r][c] + 1
            dfs((pos[0], pos[1]))
    
for i in range(N):
    line = list(input())
    grid.append(line)
    if s == None:
        if 'S' in line:
            s = (i,line.index('S'))
# print(s)
dfs(s)
if len(paths) == 0: 
    print('NOT POSSIBLE')
else:
    print(min(paths))


'''
Learnings: there are many issues if I try to do this with dfs instead of bfs. One of them is the following test case:

5 6 6
111111
100011
100S01
110011
110000
111111

For instance, using the implementation above, I will go left from S, down, and then right. The 'distance' at (3, 3) will then
be 3, even though a quicker path is directly below S! And when I finally recurse back to S, (3, 3) will not be visited again
because it's already visited!

So it's super tricky. I shall try to implement it with BFS instead, as it should. 
'''