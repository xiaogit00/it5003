'''
Initial Problem Analysis:
Okay - given a string, format them, add to a set, and 
generate the unique set. 

Seems pretty simple. 
'''
n = int(input())
keywords = set()

for _ in range(n):
    s = input()
    s = s.replace('-', ' ')
    s = s.lower()
    keywords.add(s)

print(len(keywords))
