n, m = map(int, input().split())
grids = [list(input()) for i in range(n)]

def mTightPrint(m):
    for i in range(len(m)):
        line = ''
        for j in range(len(m[0])):
            line += str(m[i][j])
        print(line)

for i in range(n-1):
    for j in range(m):
        if grids[i+1][j] == '#' and grids[i][j] == 'V':
            if j > 1 and grids[i][j-1] == '.': grids[i][j-1] = 'V'
            # print('value of j', j)
            if j < m-1 and grids[i][j+1] == '.': grids[i][j+1] = 'V'
    for j in range(m-1, 0, -1):
        if grids[i+1][j] == '#' and grids[i][j] == 'V':
            if j > 0 and grids[i][j-1] == '.': grids[i][j-1] = 'V'
            # print('value of j', j)
            if j < m-1 and grids[i][j+1] == '.': grids[i][j+1] = 'V'
    for j in range(m):
        if grids[i+1][j] == '.' and grids[i][j] == 'V':
            grids[i+1][j] = 'V'

mTightPrint(grids)

'''
...V...
...V...
..VVV..
...#VV.
..###V.
'''