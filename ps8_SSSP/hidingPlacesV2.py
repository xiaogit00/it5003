'''
C++ Answer from online converted to python, for reference
'''

from collections import deque

inf = 1 << 15

def inrange(i, j):
    return 0 <= i < 8 and 0 <= j < 8

def bfs(dist, starti, startj):
    q = deque([(starti, startj)])
    dist[starti][startj] = 0

    dx = [1, 2, 2, 1, -1, -2, -2, -1]
    dy = [-2, -1, 1, 2, 2, 1, -1, -2]

    while q:
        curri, currj = q.popleft()

        for k in range(8):
            nexti = curri + dx[k] # This is something to be learned. 
            nextj = currj + dy[k]

            if not inrange(nexti, nextj): # this is very neat as well. 
                continue

            if dist[nexti][nextj] > dist[curri][currj] + 1: # Relax operation
                dist[nexti][nextj] = dist[curri][currj] + 1
                q.append((nexti, nextj))

def solve(): # this is one way of handling multiple test case input
    s = input()

    # Run BFS
    dist = [[inf for _ in range(8)] for _ in range(8)]
    bfs(dist, ord(s[0]) - ord('a'), int(s[1]) - 1) # Here, the i and j values are converted as c and r values, as they are 
    # i.e. no flipping. So d5 would be (3, 4). It's almost like using coordinates. Similarly, dist also refers to coordinates 
    # it seems. dist[i][j] would be like coordinates.Don't think of them as row/col values, they're coordinates. 

    # Find farthest dist, print it
    far = 0
    for i in range(8):
        for j in range(8):
            far = max(far, dist[i][j])
    print(far, end=" ") # Okay there's this trick for formatting

    # Find all at that dist
    for j in range(7, -1, -1): # A way of iterating from 7 to 0 inclusive ( again, treat it as coordinates); it's like
        #                       saying, I want to iterate from the top downwards (top is col 7), then left and right as normal.
        for i in range(8):
            if dist[i][j] == far:
                # print((i, j))
                here = chr(i + ord('a')) + str(j + 1)
                print(here, end=" ") # special IO trick here..
    print()

if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        solve()