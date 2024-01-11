"""
Initial problem analysis
So first line takes the number of regions
Second line takes the population of the cities

So: I want the largest number of votes a party can receive and still lose the election. 
For that to happen, I need to maximize the regions with the highest votes, and have less than half of
the regions of the losing votes. 

The number of regions i 'need to win' is n//2 -> so for 3 regions, it'll be be 1, for 5 regions, it'll be 2. 
9 regions, it'll be 4. 
"""
import sys 

n: int = 0
populations: list = []
for i, line in enumerate(sys.stdin):
    if 'q' == line.rstrip():
        break
    if i == 0:
        n = int(line)
    if i == 1:
        populations = sorted([int(i) for i in line.split()], reverse=True)

maxVotes = 0

for i in range(n//2):
    maxVotes += populations[i]
for num in populations[n//2:]:
    maxVotes += num//2

print(maxVotes)

