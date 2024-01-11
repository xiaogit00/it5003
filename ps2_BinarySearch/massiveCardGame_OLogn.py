'''
How do I convert my O(N^3) algorithm to an nLogn algorithm? 

I have a hunch that the solution lies in indexing. 

The core idea is still how i count the total number of elements of lst2 that's found in lst1. 

let's say lst1_unique = set(lst1)

And assuming that lst1 is sorted. 

If I want to find p in lst1, instead of searching through the entire lst1, I'll need to find the first index of p: lst1.index(p), and then find the index of the next item in the lst1_unique -> nxtNum = lst1_unique[lst1_unique.index(p) + 1]

Then, to find out many ps there are in lst1, I'll just need to take index(nextNum) - index(p)

for instance, [1, 1, 2, 3, 4]
1 = 0
2 = 2
How many 1s? 2 - 1
Add that to total
'''
def binarySearch(lst, key):
    low = 0
    high = len(lst) - 1
    def helper(low, high):
        mid = (high + low)//2
        if low > high:
            return None
        if lst[mid] == key:
            return mid
        elif key < lst[mid]:
            return helper(low, mid-1)
        elif key > lst[mid]:
            return helper(mid+1, high)
    return helper(low, high)

n = int(input())
lst = list(map(int, input().split()))
r = int(input())
ranges = []
for _ in range(r):
    ranges.append(list(map(int, input().split())))
    
lst1_sorted = sorted(lst)


# print(lst1_sorted)
# print('\n')

for singleRange in ranges:
    total = 0
    startIndex = binarySearch(lst1_sorted, singleRange[0])
    endIndex = binarySearch(lst1_sorted, singleRange[1])
    if startIndex is not None:
        while startIndex > 0 and lst1_sorted[startIndex] == lst1_sorted[startIndex-1]:
                startIndex-=1
    if endIndex is not None:
        while endIndex < n-1 and lst1_sorted[endIndex] == lst1_sorted[endIndex+1]:
                endIndex+=1
    if startIndex == endIndex == None:
        # the other case I need to capture is if startIndex is None, but FALLS to the left of lst1_sorted[0], and
        # endIndex is None, and Falls to the right of lst1_sorted[-1]
        if singleRange[0] < lst1_sorted[0] and singleRange[1] > lst1_sorted[-1]:
            print(n)
            continue
        # Alrigght - so in  this case, 4 and 10 both return NONe! but there's sth in th emiddle. 
        # The r/s is defined by: if 
        # lst1_sorted[0] < startIndex < lst1_sorted[-1] and endIndex > lst1_sorted[-1]
        # So I'll need the index of the element after the value 4
        print(0)
        continue
    elif startIndex is not None and endIndex is None: # ending index outside of range of lst
        for i in range(startIndex, n): # count from start to end
            total+=1 
        print(total)
        continue
    elif startIndex is None and endIndex is not None: # starting index outside of range of lst
        for i in range(endIndex + 1):
            total+=1
        print(total)
        continue
    else:
        total = endIndex + 1 - startIndex
        print(total)
        continue
        








# There's a couple of cases to consider. 
# If start and end index cannot be found, returns 0
# If start range is found, and end range is not found:
#   For instance, we search for range (5, 8) in 123456
#       Then, can we still sum up the items in the range? 
#       How do we sum them? In this case, for i in range(start, len(lst1)): total += lst[i]
# If start range not found, end range is found:
#   For instance, range (1, 4) in 345667: (end=1)
#       for i in range(end+1) -> 0, 1
#           total+=lst[i]

#     while lst[end + 1] == lst[end]:
#         total+=1
#         end+=1
#     print(total)

# for lst2 in ranges: # O(N)
#     total = 0
#     for num in lst2: # Search lst1 for num
#         targetIndex = lst1_sorted.index(num)
#         nxtNum = lst1_unique[targetIndex+1]
#         countNum = lst1_sorted.index(nxtNum) - targetIndex
#         total += countNum
#     print(total)



'''
Right - so my set method doesn't work because it's not subscriptable. 

Maybe I can try this method: 
Let the low and high of the range be l and h. 

I'll find the index of the l: 
start = lst.index(l)
end = lst.index(h)

total += end - start 

while lst[end + 1] == lst[end]:
    total+=1
    end+=1
hmm and maybe that'll return me the total? without the need to convert it to a list..
    

lst[l:]
'''