N = int(input())
L = list(map(int, input().split()))

L.sort()
sum = L[0]
costs = 0
for i in range(1, N):
    sum+=L[i]
    costs+=sum

print(costs)