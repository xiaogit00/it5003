r, c = map(int, input().split())

grid = []
locs = []
def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

def travel(loc):
    i, j = loc[0], loc[1]
    if i+1>=r or j-1<0 or j+1>=c: return

    if grid[i+1][j] == '.':
        grid[i+1][j] = 'V'
        travel((i+1, j))
    elif grid[i+1][j] == '#':
        if grid[i][j-1] == '.':
            grid[i][j-1] = 'V'
            travel((i, j-1))
        if grid[i][j+1] == '.':
            grid[i][j+1] = 'V'
            travel((i, j+1))
        

for _ in range(r):
    grid.append(list(input()))

for i in range(r):
    for j in range(c):
        if grid[i][j] == 'V':
            locs.append((i, j))

for loc in locs:
    travel(loc)

mTightPrint(grid)