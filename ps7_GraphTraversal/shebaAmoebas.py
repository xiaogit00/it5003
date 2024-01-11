m, n = map(int, input().split())

grid = [list(input()) for _ in range(m)]
dx = [-1, -1, 0, 1, 1, 1, 0, -1] # W to SW clockwise 
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def outOfGrid(x, y):
    return True if x<0 or y<0 or x>=m or y>=n else False

def dfs(s):
    x, y = s[0], s[1]
    neighbours = []
    grid[x][y] = '.'
    for i in range(8):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if not outOfGrid(x1, y1):
            neighbours.append((x1, y1))
    for x1, y1 in neighbours:
        if grid[x1][y1] == '#':
            dfs((x1, y1))
            
def findFirstAmoeba(grid):
    # Given a grid, find first '#' character
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '#':
                return (i, j)
    return False

amoebaCount = 0

while findFirstAmoeba(grid):
    firstAmoeba = findFirstAmoeba(grid)
    dfs(firstAmoeba)
    amoebaCount+=1
print(amoebaCount)