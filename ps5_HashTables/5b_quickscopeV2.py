'''
Higher level implementation:


'''

import sys
from collections import defaultdict

lines = sys.stdin.readlines()

n = int(lines[0])
v = defaultdict(list)
level = 0
pos = defaultdict(lambda: None) # an array, of the index of dicts at each level 
pos[level] = 0 # simulate the first bracket opening 
parent = defaultdict(list)

class Variables():
    def __init__(self):
        self._dict = defaultdict(list)
    def addElement(self, level, pos, varName, varType):
        if len(self._dict[level]) < pos+1:
            self._dict[level].append(defaultdict(lambda: ''))
        self._dict[level][pos][varName] = varType
            

for line in lines[1:n+1]:
    line = line.split()
    
    if line[0] == 'TYPEOF':
        varName = line[1]
        res = v.searchInCurrentLevel()
        if len(res) > 0:
            print('found!,', res)
            break
        else:
            res = v.searchThroughAncestors()
            if len(res) > 0:
                print('found!', res)
                break
            else:
                print('UNDECLARED')
        # if v[level][pos[level]][varName] == '':
        #     print('UNDECLARED')
        # else:
        #     print(v[level][pos[level]][varName])
    elif line[0] == 'DECLARE':
        varName = line[1]
        varType = line[2]
        v.addElement(level, pos[level], varName, varType)

    elif line[0] == '{':
        level +=1
        if pos[level] == None:
            pos[level] = 0
        else:
            pos[level] += 1
        parent[level].append(v[level-1][pos[level-1]])
    elif line[0] == '}':
        level-=1