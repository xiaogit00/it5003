'''
Initial problem analysis:
I am going to consume the string 1 character at once. 
From this requirements, seems like I will use a deque. 
Whenever a bracket is found, I'll take the middle elements of the bracket and 
appendLeft on the deque. Then, I'll continue appending the right elements.

while s[i] != '\n'
    If char is not [], 
        newList += char
    If char = [, curr goes to 0. last++
    s.insert(curr) s[last].remove 

abc[def]
0123456

defabc
0123456

'''

s = input()
txt = ''
beijuTxt = ''
sotMode = False

for char in s:
    if char == '[':
        sotMode = True
        continue
    elif char == ']':
        sotMode = False
        continue

    if sotMode:
        beijuTxt += char
    else:
        txt += char

print(beijuTxt + txt)

