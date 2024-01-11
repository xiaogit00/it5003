n, m = map(int, input().split())

if m > 2*n-3 or m < n-1:
    print(-1)
else:
    totalEdges = 1
    i = 1
    while totalEdges <= m and i <= n-1:
        print(i, ' ', i+1)
        totalEdges +=1
        i+=1
    i = 1
    while totalEdges <= m and i <= n-2:
        print(i, ' ', i+2)
        totalEdges +=1
        i+=1
