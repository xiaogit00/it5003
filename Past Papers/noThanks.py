n = int(input())
L = list(map(int, input().split()))

L.sort()
ans = L[0]
for i in range(1, n):
    if L[i-1]+1 == L[i]:
        continue
    ans += L[i]


print(ans)