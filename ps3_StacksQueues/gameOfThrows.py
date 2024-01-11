n, k = map(int, input().split())
cmds = input().split()
newCmds = []
for i, cmd in enumerate(cmds):
    if cmd == 'undo':
        numToPop = int(cmds[i+1])
        for _ in range(numToPop): newCmds.pop()
    elif cmds[i-1] == 'undo': continue
    else:
        newCmds.append(cmd)

newCmds = list(map(int, newCmds))

pos = 0
for i in newCmds:
    pos = (pos+i)%n
print(pos)