n, m = map(int, input().split())
if m > 2*n-3 or m < n-1: 
    print(-1)
    exit()
counter = 0
for i in range(1, n):
    if counter < m:
        print(i, i+1)
        counter +=1
    else: exit()
for i in range(1, n-1):
    if counter < m:
        print(i, i+2)
        counter +=1
    else: exit()