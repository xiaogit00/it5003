'''
Improvements 
I think it reaches run time error
Perhaps I don't need to necessarily alter the list? 
And perhaps I can just use a pointer and a list?

For instance, for i in range(n/2)
- if match found in that way, increment i 
- if match found in another way, increment 2 times. 
- use a standard list? 
'''
n = int(input())

s = input()

def close(openBracket):
    if openBracket == '(':
        return ')'
    elif openBracket == '[':
        return ']'
    elif openBracket == '{':
        return '}'
    else: 
        return None

validity = True
i = 0
j = len(s) - 1

while i < n and i <= j:
    if i==j: 
        validity = False
        break
    first = s[i]
    second = s[i+1]
    last = s[j]

    if close(first) == second:
        i+=2
        continue
    elif close(first) == last:
        i+=1
        j-=1
        continue
    else:
        validity = False
        break
print("Valid") if validity else print("Invalid")

'''
[{}{}{}]]
012345678
n=9
i=0
j=8

first = last
i=1
j=7

first = second
i = 3
j=7

first = second
i = 5
j = 7

first = second
i = 7
j = 7


(())((()
01234567
i=0
j=7
close(first) = last
i=1
j=6
close(first) = second
i=3
j=6
none !

()()(())
01234567
i = 2
first = (
second = )
i = 4
j=7
first = (
last = )
i = 5
j = 6
i = 6
j = 5




'''
