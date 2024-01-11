'''
Initial problem analysis
I am supposed to look at a string, and if the string is '<', it'll pop one element
out of the string. It seems like I'll loop through the string again?
'''
from collections import deque

s = input()

res = deque([])

for char in s:
    if char == '<':
        if len(res) == 0: continue
        res.pop()
    else:
        res.append(char)

print(''.join(res))