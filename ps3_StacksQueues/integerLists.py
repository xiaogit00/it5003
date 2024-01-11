'''
Seems relatively straightforward

Reverses the list; 
D is a popleft. 

Initial Problem Analysis:
1. Read the operations - loops through each operation
2. if op = R, reverse the list; if op = 'D', popLeft. 

The only thing to take note is that you'd want to convert this list into a deque 
because popleft is an expensive operation on lists of size 100k

'''
from collections import deque 
n = int(input())
tests = []
for _ in range(n):
    operations = input()
    numItems = int(input())
    if numItems > 0:
        lst = list(map(int, input().strip('][').split(',')))
    else:
        input()
        lst = []
    tests.append([operations, numItems, lst])
# print(tests)

for test in tests:
    isReversed = 0 # state of not reversed
    de = deque(test[2])
    operations = test[0]
    error = False
    for op in operations: 
        if op == 'R':
            isReversed = 1 - isReversed
        elif op == 'D':
            if len(de) == 0: 
                error = True
                continue
            de.pop() if isReversed else de.popleft()
    if error:
        print('error')
    else:
        if isReversed:
            print(list(de)[::-1])
        else:
            print(list(de))

'''
Ah, the problem lies in the reverse. It is an O(N) operation. The thing is, given 
that D is a popLeft, once you reverse, it becomes a pop operation. So to 'alter' the
list, you only have to recognize how many reverses there are and pop accordingly.

Then finally, you'll do a print of lst[1:3:-1]

What the - still don't pass. Ok move on. 
'''