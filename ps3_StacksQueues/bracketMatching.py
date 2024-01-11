'''
You're supposed to check whether a bracket is valid or not. 

A bracket contains the following: (), [], {}. 

Wa you can imagine how these things form the underlying engines of a software like 
vscode even. 

Initial Problem analysis:
1. Given a string. This can somewhat be considered a stack problem. 
2. Where, closing a bracket is a last in first out (LIFO) problem. 
3. I will read a string. for every open bracket, I will add it to the stack. 
4. If a matching closing bracket is found, I'll pop it from the stack. 
5. A sequence is valid if everything is popped properly from the stack. 

Deeper questions:
1. What are the advantages of using a stack to solve this problem? Can it be done 
using a simple list?
- ok apparently if the input is large, some append operations might take longer

Higher level implementation:
1. Get the input
2. Convert into a deque. 
3. A match is found if either the closing bracket is found at start of list, or 
next to the item (n-1). If not, invalid. 
4. If len(de) becomes 0, then valid
'''
from collections import deque 

n = int(input())

if n%2 != 0: print('Invalid')

stack = deque(input())

def close(openBracket):
    if openBracket == '(':
        return ')'
    elif openBracket == '[':
        return ']'
    elif openBracket == '{':
        return '}'

openingBrackets = ['(', '[', '{']
validity = True
while len(stack)>0:
    first = stack[0]
    second = stack[1]
    last = stack[-1]

    if close(first) == second:
        stack.popleft()
        stack.popleft()
        continue
    elif close(first) == last:
        stack.popleft()
        stack.pop()
        continue
    else:
        validity = False
        break
print("Valid") if validity else print("Invalid")

# [{}]{}

'''
How about I traverse through the deque? Or LL? 
I'll save 3 states: round, square, curly
This is a stack kind of operation

Let's say each is a node. 
I'll construct it as a stack of plates: ((
The bottom of the stack are open brackets. 
As long as the top meets a closing bracket, pop top. Go to next. 
By the end, I sohuld have nothing in the stack because everything is popped. 

How would I implement this? Can I 'consume' the list 1 by 1? 

for i,item in enumerate(stack):
    if item in openBrackets:
        continue
    if item in closeBrackets:
        stack[i-1]

for char in input:
    
'''