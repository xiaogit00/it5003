'''
Each time I increase in a level, I'll want the following behavior:
1. if TypeOf var doesn't exist in current level (meaning, if the level and dictID of last var)
Is there a case where the var is in a previous level, but different dictId? 
'''

import sys
from collections import defaultdict
from dataclasses import dataclass 

lines = sys.stdin.readlines()

n = int(lines[0])
level = 0
v = defaultdict(list)
dictID = defaultdict(lambda: 0)

@dataclass
class Variable:
    type: str
    level: int
    dictID: int

for line in lines[1:n+1]:
    line = line.split()
    if line[0] == 'TYPEOF':
        varName = line[1]
        if len(v[varName]) > 0:
            # check that we're getting the level we want or less
            # print(v[varName])
            while (len(v[varName]) > 0) and level < v[varName][-1].level:
                # print("This is reached once, value of v[varName]", v[varName][-1][1])
                # print(v[varName][-1], ' popped')
                v[varName].pop()
            # IF same level but diff dictId, the previous dictID's value should be popped 
            if (len(v[varName]) > 0) and v[varName][-1].level == level and v[varName][-1].dictID < dictID[level]:
                v[varName].pop()
            if len(v[varName]) > 0 and v[varName][-1].dictID <= dictID[level]:
                print(v[varName][-1].type)
            else: 
                print('UNDECLARED')
        else:
            print('UNDECLARED')
    elif line[0] == 'DECLARE':
        varName = line[1]
        varType = line[2]
        # Check for multiple declarations
        if len(v[varName])>0 and v[varName][-1].level == level:
            print('MULTIPLE DECLARATION')
            exit()
        v[varName].append(Variable(type=varType, level=level, dictID=dictID[level]))
    elif line[0] == '{':
        level+=1
    elif line[0] == '}':
        dictID[level]+=1
        level-=1

'''
apple: {int, 0, 0}, {float, 1, 0}, {float, 3, 0}
banana: {double, 0, 0}
orange: {char, 1, 0}
***

x: {def, 0 , 0}, {abc, 1, 0}
y: {abc, 1, 1}
'''


