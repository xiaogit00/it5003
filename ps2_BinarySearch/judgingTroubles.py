'''
Initial problem Analysis:
This problem seems to be: find the maximum number of common items, ignoring order, between 2 arrays. 
So one way is to sort it first. 

[a, a, a, b, c]
[a, b, c]
3

[a, a, a, b, c]
[c, c]
1

So I need to pay attention to what is the most efficient way to do this kind of comparison. 

Divide and conquer? 

[d, d, e, f]
[a, a, f]
1

This is a kind of problem with a lot of duplicates. We're essentially matching the number of duplicates. 

Solution discussed: 
- the logic is kind of like merge sort
- where you're matching with 2 pointers, and if not a match, the smaller pointer advances and we check again

'''

n = int(input())
DOM = sorted([input() for _ in range(n)]) #tim merge sort variant
KAT = sorted([input() for _ in range(n)])

total = 0
for i in range(n):
    if DOM[i] == KAT[i]:
        total+=1
print(total)

