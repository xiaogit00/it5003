'''
Initial Problem analysis:
This question ultimately boils down to: you have list 2. How many times does each item in list 2 appear in list 1? 

THIS SOLUTION WORKS BUT IS AN O(N^3) SOLUTION?? FAILS many test cases. Would need to improve it in the second version. 


'''

n = int(input())
lst = list(map(int, input().split()))
r = int(input())
ranges = []
for _ in range(r):
    index = list(map(int, input().split()))
    lst2 = list(range(index[0], index[1] + 1))
    ranges.append(lst2)
'''
lst - first list. 
ranges - a list of lst2s
r - number of ranges
'''
for eachRange in ranges: # O(N)
    total = 0
    for num in eachRange: # O(N)
        total += lst.count(num) # O(N) - count is an O(N) operation
    print(total)


