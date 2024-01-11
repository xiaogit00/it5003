# https://nus.kattis.com/courses/IT5003/IT5003_S1_AY2324/assignments/mmyspc/problems/massivecardgame
def modifiedBinarySearch(lst, key):
    def helper(low, high):
        mid = (high + low)//2
        if low > high: 
            return low
        if lst[mid] == key:
            return helper(low, mid-1)
        elif key < lst[mid]:
            return helper(low, mid-1)
        elif key > lst[mid]:
            return helper(mid+1, high)
    return helper(0, len(lst) - 1)

'''
What I discovered above is that line 4 and 5 has the magical property of returning the index of the next highest element
if a number is not found. See below: "Creating the Property of returning the next item if an item"
'''
n = int(input())
lst = list(map(int, input().split()))
r = int(input())
ranges = []
for _ in range(r):
    ranges.append(list(map(int, input().split())))
    
lst1_sorted = sorted(lst)

for singleRange in ranges:
    l = singleRange[0]
    h = singleRange[1]
    lowIndex = modifiedBinarySearch(lst1_sorted, l)
    highIndex = modifiedBinarySearch(lst1_sorted, h+1)
    print(highIndex - lowIndex)

# [2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 6, 6, 6, 10, 10]
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13  14  15

# lst = [2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 6, 6, 6, 10, 10]

# print(modifiedBinarySearch(lst, 6))
'''
Let's say for above list. 
low = 1
high = 10

lowIndex = 0
highIndex = 14
Just nice

low = 3
high = 5
lowIndex = 5
highIndex = 5
WRONG!

BUT if I modify MBS to h+1 for key, 
then I'll get the desired results. 
What if high is 2? THen no problem - search for 3. Which is 5

'''

'''
Okay right now, I m not processing one single list. I am processing multiple lists, 
from the ranges variable. 
'''

'''
Creating the Property of returning the next item if an item 
is not found->


In the case that the item is not found, I would want to return the index of the next 
search item. How can I do that? I feel like this happens in the case where low > high

So instead of returning False, maybe I can return...the index of either low or high?

Let's trace again. 

[1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 5, 5, 5, 6, 6, 6]
 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16

Key = 4
(0, 16)
mid = 8 
(9, 16) --(1)
mid = 12
(9, 11) --(2)
mid = 10
(10, 11) --(3)
mid = 10
(11, 11) --(4)
mid = 11
(11, 10) --(5)
mid = 10
return 11 -> low? 
Will low here always be the index of an element that our key is between of? 

Let's examine the logic. From steps 1 to 2, we see great halvings. Step 3 is already 
checking for a very tight range of 2 numbers. Producing a mid of 10 - Basically, our 
low and high pointers are decreasing their range 1 by 1 at this point, checking for mid
Step 3 - is mid 10? No. Higher. Look for 11. Is it 11? No. Lower. Shift high down. 
Now, we're entering negative terrain. Mid *must* be in between these 2. If it's not, 
then we can't find it already. Now, here is where my modified magic is. I am saying - 
yes, mid is not within these 2. But, it's alright to return the higher element here. 
Which is 'low' variable.  

Okay! Excellent. 

However, my modifiedBinarySearch has this additional behavior. If the key is outside 
the range of the list, it'll return me n, which is the len of the input.

Let's put this to the test....
'''