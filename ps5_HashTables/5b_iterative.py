'''
Higher level implementation:


'''

from collections import defaultdict


# n = int(input())
v = defaultdict(list)
level = 0
pos = defaultdict(lambda: None) # an array, of the index of dicts at each level 
pos[level] = 0 # simulate the first bracket opening 

class Variables:
    def __init__(self):
        self._dict = defaultdict(list)
    def addElement(self, level, pos, varName, varType):
        if len(self._dict[level]) < pos+1:
            self._dict[level].append(defaultdict(lambda: ''))
        self._dict[level][pos][varName] = varType
v = Variables()
# print(v._dict)
while True:
    line = input().split()
    
    if line[0] == 'TYPEOF':
        varName = line[1]

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
    elif line[0] == '}':
        level-=1
    print(v._dict)