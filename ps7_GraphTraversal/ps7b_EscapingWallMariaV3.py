from collections import deque 

t, n, m = map(int, input().split())
grid = []
s = (0, 0)
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def isOutOfBound(r, c):
    return True if r == 0 or c == 0 or r == n-1 or c == m-1 else False

def isValid(r, c, s):
    # Here, I'll return true if it's 0; 
    # Or, I'll check the source, and see if it fulfils the criteria 
    if grid[r][c] == '0': return True
    r1, c1 = s[0], s[1]
    if grid[r][c] == 'R' and c1 == c+1: return True
    if grid[r][c] == 'L' and c1 == c-1: return True
    if grid[r][c] == 'U' and r1 == r-1: return True
    if grid[r][c] == 'D' and r1 == r+1: return True
    return False

for i in range(n):
    line = input()
    if 'S' in line: 
        s = (i, line.index('S'))
    grid.append(list(line))

visited = [[False] * m for _ in range(n)]
q = deque([(0, s)])
visited[s[0]][s[1]] = 0
while q:
    d, u = q.popleft()
    if isOutOfBound(u[0], u[1]):
        if d <= t: 
            print(visited[u[0]][u[1]])
            exit()
        else: 
            print('NOT POSSIBLE')
            exit()
    neighbours = []
    for i in range(4):
        r = u[0] + dr[i]
        c = u[1] + dc[i]
        if visited[r][c] != False: continue
        neighbours.append((r, c))
    for r, c in neighbours:
        if not isValid(r, c, u): continue
        visited[r][c] = d + 1
        q.append((visited[r][c], (r, c)))

print('NOT POSSIBLE')