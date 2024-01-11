from collections import defaultdict

n = int(input())

d = defaultdict(lambda: False)

def allAssumptionsTrue(l):
    for i in l:
        if not d[i]: return False
    return True

for i in range(n):
    line = input().split()
    conclusion = line[-1]
    assumptions = line[:-2]
    if not assumptions:
        d[conclusion] = True
        continue
    
    if allAssumptionsTrue(assumptions):
        d[conclusion] = True
    else: 
        print(i+1)
        exit()

print('correct')
    