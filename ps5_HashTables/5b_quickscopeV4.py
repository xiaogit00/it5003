import sys
from collections import defaultdict
lines = sys.stdin.readlines()

n = int(lines[0])
level = 0

class VarDict:
    def __init__(self):
        self._underlyingDict = defaultdict(list)
        self.latestScopeStack = []
        self.latestScopeStack.append({})
    
    def checkAndAppend(self, varName, varType, level):
        if varName in self.latestScopeStack[-1].keys():
            print('MULTIPLE DECLARATION')
            exit()
        else: 
            self._underlyingDict[varName].append((varType, level))
            self.latestScopeStack[-1][varName] = True

    def checkType(self, varName, level):
        if len(self._underlyingDict[varName])<=0:
            print("UNDECLARED")
        else:
            if self._underlyingDict[varName][-1][1] <= level:
                print(self._underlyingDict[varName][-1][0])
        

    def openLatestScope(self):
        self.latestScopeStack.append({})

    def popLatestScope(self):
        for key in self.latestScopeStack[-1]:
            self._underlyingDict[key].pop()
        self.latestScopeStack.pop()


vars = VarDict()

for line in lines[1:n+1]:
    line = line.split()
    if line[0] == 'TYPEOF':
        varName = line[1]
        vars.checkType(varName, level)
    elif line[0] == 'DECLARE':
        varName = line[1]
        varType = line[2]
        vars.checkAndAppend(varName, varType, level)
    elif line[0] == '{':
        level+=1
        vars.openLatestScope()
    elif line[0] == '}':
        level-=1
        vars.popLatestScope()