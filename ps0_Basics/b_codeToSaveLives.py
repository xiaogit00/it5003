
import sys 

lines = []
for line in sys.stdin:
    if 'q' == line.rstrip():
        break
    line = line.rstrip() # Remove newline char
    line = line.replace(" ", "") # Removes space between chars
    lines.append(int(line))

answers = []

for i in range(1, lines[0]*2, 2):
    ans = str(lines[i] + lines[i+1]) # Add numbers up and convert into string: 938 to "938"
    answers.append(' '.join(ans)) # Add whitespace between numbers

print('\n'.join(answers)) # Join all the numbers into 1 string, separated by newline

"""
Input: 
2
3 4 5
5 6 7
6 1
3 2 5

Output: 
9 1 2
3 8 6

"""

"""
Learned: 
.rstrip() -> strips trailing whitespace characters from string
.replace() -> removes white space characters in the middle of a string
''.join(arr) -> joins 
sys.stdin -> you have to iterate through it to get each line 
if 'q' : break -> terminating out of stdin. 
"""