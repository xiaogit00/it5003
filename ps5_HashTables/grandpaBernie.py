from collections import defaultdict
n = int(input())
countries = defaultdict(list)
for _ in range(n):
    s, y = input().split()
    countries[s].append(int(y))
q = int(input())
for k, v in countries.items():
    v.sort()
for _ in range(q):
    s, q = input().split()
    print(countries[s][int(q)-1])