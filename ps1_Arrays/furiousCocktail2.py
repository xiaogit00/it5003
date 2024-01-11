'''
SOLUTION 2 BY NGA
Thoughts on solution:
Time
0 1 2 3 4 5 6 7 8 9 10
    4--------
        3------
            2----

Current drink effect 4
timeTillLastEffect = t + (n-1)*t
t + (n-1)*t
2 + 2*2
6
if 4<6
return NO

Outside: If none of them return No, 
Return 'YES'
'''

import sys

lines = []
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    line = line.rstrip() # Remove newline char
    lines.append(line)

t = int(lines[0][-1])
n = int(lines[0][0])
potions = [int(i) for i in lines[1:]]
sortedPotions = sorted(potions, reverse=True)

for i in range(n):
    timeTillLastEffect = t + (n-i-1)*t
    if sortedPotions[i] < timeTillLastEffect:
        print("NO")
        break
    if i==n-1:
        print("YES")


