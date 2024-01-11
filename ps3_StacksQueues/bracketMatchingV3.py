n = int(input())
s = input()

def close(openBracket):
    if openBracket == '(':
        return ')'
    elif openBracket == '[':
        return ']'
    elif openBracket == '{':
        return '}'

openBrackets = ['(', '[', '{']
stack = []
endOfStack = False
for bracket in s:
    if bracket in openBrackets:
        stack.append(bracket)
    else:
        if len(stack) == 0:
            endOfStack = True
            break
        if close(stack[-1]) == bracket:
            stack.pop()
        else:
            break

print("Valid") if (len(stack) == 0) and (not endOfStack) else print("Invalid")

# ()(())
# ([]{})
# (())((()
# ([}{])
# [{}{}]{}