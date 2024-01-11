'''
Initial Problem Analysis
Im giving a list of integers, around 1k of them only. 

My job is to find the odd one out. 

So my initial hunch is that this problem can easily be 
solved using a dictionary, in the following manner

Let's say x is a number. 
dict[x] = True -> when x is found. 
if dict[x] = True:
    and x is found again: 
    dict[x] = False
In this way, all the numbers that are even will 
cancel each other out, and at the end of the day, 
we just need to identify the remaining element in the
dict. We'll loop through the dict. Simple enough?
'''
from collections import defaultdict
n = int(input())

for i in range(n):
    d = defaultdict(lambda: False)
    g = int(input())
    coupons = list(map(int, input().split()))

    for coupon in coupons:
        if d[coupon]:
            d[coupon] = False
        else:
            d[coupon] = True
    for k,v in d.items():
        if v==True:
            print(f'Case #{i+1}: {k}')

# print(d)