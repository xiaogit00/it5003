from collections import deque, defaultdict

T = int(input())
input()

def outsideRange(x, y, n):
    return True if x < 0 or y < 0 or x >= n or y>=n else False

for _ in range(T):
    line = input()
    if line == '':
        break
    n, k = map(int, line.split())
    grid = [[] for _ in range(n)]
    for i in range(n):
        grid[i] = list(map(int, input().split()))
    
    dist = defaultdict(lambda: 0)
    dist[(0, 0)] = grid[0][0]
    max = 0
    q = deque([]) 
    q.append((0, 0))

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    max = 0
    while q:
        u = q.popleft()
        x, y = u[0], u[1]
        neighbours = []
        for i in range(4):
            x1 = x + dx[i]
            y1 = y + dy[i]
            if outsideRange(x1, y1, n): continue
            neighbours.append((grid[x1][y1], (x1, y1)))
        for w, v in neighbours:
            if w <= grid[x][y]: continue
            if dist[u] + w > dist[v]:
                dist[v] = dist[u] + w
                if dist[v] > max: max = dist[v]
                q.append(v)
    print(max)