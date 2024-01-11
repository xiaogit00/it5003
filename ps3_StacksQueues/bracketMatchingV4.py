n = int(input())
seq = list(input())

def isOpen(i):
    return True if i == '(' or i == '[' or i == '{' else False
def isClosed(i):
    return True if i == ')' or i == ']' or i == '}' else False

def match(open, close):
    if open == '(' and close == ')': return True
    if open == '[' and close == ']': return True
    if open == '{' and close == '}': return True
    return False
s = []
for i in seq:
    if isOpen(i):
        s.append(i)
    if isClosed(i):
        if len(s) == 0:
            print("Invalid")
            exit()
        last = s.pop()
        if match(last, i): continue
        else: 
            print("Invalid")
            exit()
if len(s) == 0:
    print('Valid')
else: 
    print("Invalid")