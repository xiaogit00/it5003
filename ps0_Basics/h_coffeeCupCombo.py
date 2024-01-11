"""
Initial problem analysis
Okay - so every '1' is a pit stop for Joanna to refill. 

If she enters a lecture without a coffee, she will just sleep. And that's fine. 

She can leave the lecture with 2 cups of coffee, which is enough to sustain her for the 
next 2 lectures without sleeping. 
Let's think about how I can approach this problem. 

I am given a string. everything on the left, if it's 0, she will sleep. We remove the 
0s on the left. 

awakeCount

If it's 1, awakeCount++ 
supplyCoffee = 2
if 0 & supplyCoffee
-awakeCount++
-supplyCoffee--

Hmm I think this should be it. 

Pseudocode
1. Get the second line of the input 
2. Define awakeCount = 0, supplyCount = 0
3. Loop through the array
4. If 0 & supplyCoffee == 0: continue
5. If 1: awakeCount ++, supplyCoffee = 2
6. If 0 & supplyCoffee -> awakeCount++, supplyCoffee--


"""
import sys 

lectures = ''
for i, line in enumerate(sys.stdin):
    if 'q' == line.rstrip('\n'):
        break
    if i == 1:
        lectures = line.rstrip('\n')

awakeCount = 0
supplyCount = 0

for digit in lectures:
    if digit == '1':
        awakeCount += 1
        supplyCount = 2
    elif digit == '0' and supplyCount:
        awakeCount += 1
        supplyCount -= 1
        continue 

print(awakeCount)


'''
A better solution:

n = int(input())
s = input()

awake = ['0']*(n+2)

for i in range(n):
    if s[i] == '1':
        awake[i] = '1'
        awake[i+1] = '1'
        awake[i+2] = '1'

print(awake[:-2].count('1'))
'''