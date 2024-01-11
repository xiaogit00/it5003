'''
The idea is to iterate through every element in an array, and if l[i] > l[i+1], then swap their indexs. Every loop will float the biggest number to the end of the array.

Notes on implementation:
1. It's key to note what the outer and inner loop does. The outer loop defines the 'cycles' in which this loop will run. Bubbling 1 number up is 1 cycle. For an array with N terms, you'll need to run N-1 cycles. This is because your last unsorted term will alwys be sorted once the remaining N-1 are sorted. 
2. The inner loop indicates the actual bubbling swaps. This is a decreasing range: once you've successfully bubbled up 1, the range decreases by 1. In the first place, you'll need to do N-1 bubbling. (For instance, an array of 3 requires 2 bubbles on first run). Then, it becomes N-2 times, and so on, until it reaches 1. The way to decrement is to use your outer loop iterator, setting the range to range(n-1-r). Tracing example:
    n = 5
    r  range(n-1-r)    i  
    0  4               0 1 2 3 
    1  3               0 1 2 
    2  2               0 1 
    3  1               0 

'''

def bubbleSort(lst):
    n = len(lst)
    for r in range(n-1): 
        for i in range(n-1-r): 
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                print(lst)
    return lst

bubbleSort([2,1,5,3,4])

'''
Notes on time and space complexity:
- Number of iterations of inner loop: (n-1) + (n-2) +... 1 = n(n-1)/2
Taking the leading term and dropping the coefficient:
Order of growth: O(N^2)

IF it's already sorted: 
then basically inner loop is skipped: you're left with the outer loop, which runs n times. 

Bubble sort can terminate in O(N) time. THis is the best case. 
But it doesn't change the O(N^2) time complexity of bubble sort. 
'''