from collections import deque
import sys

sys.setrecursionlimit(200000)
t, N, M = map(int, input().split())

grid = []
visited = [[False for _ in range(M)] for _ in range(N)]
s = None
paths = []
q = deque([])
explored = set()

def bfs(s):
    global grid
    global q
    # print('bfs is reached in:', s)
    r, c, d = s[0], s[1], s[2]
    visited[r][c] = True
    explored.add((r, c))
    if r == 0 or r == N-1 or c == 0 or c == M-1:
        if d <= t: 
            print(d)
            exit()
        else: return

    neighbours = [(r, c-1, 'R'), (r-1, c, 'D'), (r, c+1, 'L'), (r+1, c, 'U')] # Third variable is the direction coming from
    for pos in neighbours:
        v = grid[pos[0]][pos[1]]
        if (pos[0], pos[1]) in explored: continue
        if v  == '0':
            if not visited[pos[0]][pos[1]]: 
                q.append((pos[0], pos[1], d+1))
                explored.add((pos[0], pos[1]))
        elif (v in ['L', 'U', 'R', 'D']) and (v == pos[2]): # ..and if letter same as direction coming from
            if not visited[pos[0]][pos[1]]: 
                q.append((pos[0], pos[1], d+1))
                explored.add((pos[0], pos[1]))
    while q:
        bfs(q.popleft())
    
for i in range(N):
    line = list(input())
    grid.append(line)
    if s == None:
        if 'S' in line:
            s = (i,line.index('S'), 0)
# print(s)

bfs(s)

print("NOT POSSIBLE")

'''
Key Takeaway:
By using another set to track the nodes explored, you're avoiding a lot of duplicated work because you're not adding
those nodes that are already 'explored' into the queue. 
'''

'''
Test cases:
4 6 6
111111
100011
100S01
110011
110000
111111

2 4 4
1111
1S01
1011
0U11

4 6 6
111111
001011
111S0D
11RU11
110011
110111

'''