'''
https://nus.kattis.com/courses/IT5003/IT5003_S1_AY2324/assignments/aa9x5h/problems/cocktail

Thoughts on solution:
Time
0 1 2 3 4 5 6 7 8 9 10
    4--------
        3------
            2----

Basically, I created an array counter time, where the indices map to the time in seconds. 

I then applied the potions at each time to the time counter. 

Finally, I checked if the time array contains any items where it's equal to the total number of potions (meaning all applied.)

I feel this is the simplest abstraction. First, I tried using an array of arrays to represent it, but then felt it's unnecessarily complicated, then I wanted to use a dictionary, but realized it's also a bit tedious to implement, so I finally decided upon an array counter. 

But idk. I still feel like the solution can be simpler. 

Okay implemented a while loop and a for loop inside, taking 2 counters. This is a way simpler abstraction I feel. Good. Damn it. I spent like 2 hours on this solution?

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
time = [0 for _ in range(t*len(sortedPotions) + sortedPotions[-1] + 1)]

timeIndex = t
potionIndex = 0
while timeIndex <= n*t:
    for j in range(sortedPotions[potionIndex]):
        time[timeIndex+j] +=1
    potionIndex+=1
    timeIndex+=t

if n in time: 
    print('YES')
else: 
    print('NO')
