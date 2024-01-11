'''
**Higher level implementation**

'''

import sys
from collections import defaultdict

lines = sys.stdin.readlines()

n = int(lines[0])
variables = defaultdict(lambda: '')
dictsMap = defaultdict(lambda: None)
dictsMap['dictCount'] = [] # An array of dictionary Index at each level 
dictIndex = 0
level = 0

for line in lines[1:n+1]:
    line = line.split()
    
    if line[0] == 'TYPEOF':
        varName = line[1]
        if variables[varName] == '':
            print('UNDECLARED')
        else:
            print(variables[varName])
    elif line[0] == 'DECLARE':
        varName = line[1]
        varType = line[2]
        # Check which level our current state is on, and input into the appropriate 
        # program 
        if level == 3: 
            variables[dictIndex][dictIOndex][dictIndex]

        # if variables[varName] == '':
        #     variables[varName] = varType
        # else:
        #     print('MULTIPLE DECLARATION')
        #     exit()
    elif line[0] == '{':
        dictsMap['dictCount'].append(0) # initialize a new layer, layer 0
        dictIndex = dictsMap['dictCount'][level] # The int at position level
        variables[dictIndex] = {} # Create a new dictionary 
        level += 1 # Enter this new level
    elif line[0] == '}':
        print("closed bracket")
    
    