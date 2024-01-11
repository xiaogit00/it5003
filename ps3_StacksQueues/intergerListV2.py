from collections import deque 

T = int(input())
for _ in range(T):
    cmds = input()
    reversed = 0
    error = False
    n = int(input())
    if n>0:
        l = list(map(int, input().strip('][').split(',')))
        l = deque(l)
    else: 
        input()
        l = []
    for cmd in cmds:
        if cmd == 'R':
            reversed = 1 - reversed
        if cmd == 'D':
            if len(l) == 0: 
                error = True
                continue
            if reversed: 
                l.pop()
            else:
                l.popleft()
    if error: 
        print('error')
        continue
    if reversed: l.reverse()
    print(list(l))
