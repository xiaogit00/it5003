from collections import deque
from math import inf
from pprint import pprint
from collections import defaultdict

n = int(input())

def convertToChess(pos):
    r = 8 - pos[0]
    c = chr(97 + pos[1])
    return f'{c}{r}'

for _ in range(n):
    pos = input()
    grid = [[inf for _ in range(8)] for _ in range(8)]
    r = 8 - int(pos[1]) # Using 0-based index for row num. Rmb to switch back when outputing ans
    c = ord(pos[0]) - 97 
    grid[r][c] = 0
    max = 0
    maxCoor = defaultdict(list)
    
    q = deque()
    q.append((r, c))

    while q:
        (r, c) = q.popleft()
        neighbours = [(r-1, c-2), (r-2, c-1), (r-2, c+1), (r-1, c+2), (r+1, c+2), (r+2, c+1), (r+2, c-1), (r+1, c-2)] # from left most move, clockwise.
        # So here, I'll only retain those that are still within the board:
        for pos in neighbours:
            if pos[0] < 0 or pos[1] < 0 or pos[0] > 7 or pos[1] > 7: continue # outside of board
            if grid[r][c]+1 < grid[pos[0]][pos[1]]:
                grid[pos[0]][pos[1]] = grid[r][c]+1
                maxCoor[grid[r][c]+1].append((pos[0], pos[1]))
                if grid[pos[0]][pos[1]] > max:
                    max = grid[pos[0]][pos[1]]
                q.append((pos[0], pos[1]))

    cleaned = ' '.join(list(map(convertToChess, sorted(maxCoor[max]))))
    print(f'{max} {cleaned}')
