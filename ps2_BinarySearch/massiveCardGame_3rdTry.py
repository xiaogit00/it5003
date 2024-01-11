def binarySearch(lst, key):
    def helper(low, high):
        mid = (high + low)//2
        if low > high:
            return False
        if lst[mid] == key:
            return True
        elif key < lst[mid]:
            return helper(low, mid-1)
        elif key > lst[mid]:
            return helper(mid+1, high)
    return helper(0, len(lst) - 1)

def binarySearchNextHighest(lst, key):
    def helper(low, high):
        mid = (high + low)//2
        if low > high:
            return False
        if lst[mid] < key < lst[mid+1]:
            return lst[mid+1]
        elif key < lst[mid]:
            return helper(low, mid-1)
        elif key > lst[mid]:
            return helper(mid+1, high)
    return helper(0, len(lst) - 1)

def binarySearchIndex(lst, key):
    def helper(low, high):
        mid = (high + low)//2
        if low > high:
            return False
        if lst[mid] == key:
            return mid
        elif key < lst[mid]:
            return helper(low, mid-1)
        elif key > lst[mid]:
            return helper(mid+1, high)
    return helper(0, len(lst) - 1)

n = int(input())
lst = list(map(int, input().split()))
r = int(input())
ranges = []
for _ in range(r):
    ranges.append(list(map(int, input().split())))
    
# lst1_sorted = sorted(lst)
# uniqueList = list(set(lst1_sorted))
# print(lst1_sorted)
# print('\n')

lst1_sorted = [2, 3, 7, 9, 13]
uniqueList = list(set(lst1_sorted))

for singleRange in ranges:
    r1 = singleRange[0]
    r2 = singleRange[1]
    r1_isFound = binarySearch(uniqueList, r1)
    r2_isFound = binarySearch(uniqueList, r2)
    l = uniqueList[0]
    h = uniqueList[-1]
    
    if not r1_isFound and not r2_isFound:
        if r1<l and r2>h: # Case 1: entire range
            print(n)
        elif r1>l and r2<h: # cast 2: in middle 
            r1_right = binarySearchNextHighest(uniqueList, r1)
            r2_right = binarySearchNextHighest(uniqueList, r2)
            r1_right_index = binarySearchIndex(lst1_sorted, r1_right)
            r2_right_index = binarySearchIndex(lst1_sorted, r2_right)
            print(r2_right_index-r1_right)


        





