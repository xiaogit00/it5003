from collections import defaultdict

n = int(input())

vars = defaultdict(lambda: False)
multiples = defaultdict(lambda: 1)
print()
for _ in range(n):
    x = int(input())
    if vars[x] == False:
        vars[x] = True
        print(x)
        continue
    if vars[x]:
        while True:
            nextMultiple = x * (multiples[x]+1)
            if vars[nextMultiple] == False:
                vars[nextMultiple] = True
                print(nextMultiple)
                multiples[x] += 1
                break
            else:
                multiples[x] += 1
                continue
