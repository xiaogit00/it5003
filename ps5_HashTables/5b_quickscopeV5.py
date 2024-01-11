from collections import defaultdict
import sys

input = sys.stdin.readlines()
n = int(input[0])

vars = defaultdict(list)
level = 0
latestScopeStack = [{}]

for line in input[1:]:
    line = line.split()
    if line[0] == '{':
        level += 1
        latestScopeStack.append({})
    if line[0] == 'DECLARE':
        name, type = line[1], line[2]
        if vars[name] and vars[name][-1][0] == level:
            print('MULTIPLE DECLARATION')
            exit()
        else: 
            vars[name].append((level, type))
            latestScopeStack[-1][name] = type
    if line[0] == 'TYPEOF':
        name = line[1]
        if len(vars[name]) == 0:
            print('UNDECLARED')
            continue
        else:
            print(vars[name][-1][1])
            continue
    if line[0] == '}':
        level -= 1
        for key in latestScopeStack[-1]:
            vars[key].pop()
        latestScopeStack.pop()
        