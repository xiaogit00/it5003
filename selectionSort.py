'''
Selection sort is basically the most naive implementation of sorting. You pick a minimum, and if any item in the list is less than the minimum, set that as the minimum, and the move it to the last unsortedIndex. 

Notes on implementation:
1. Here, it's important to note the desired range to iterate through on your inner loop. 
- For each value of r, you want to iterate through the next value of r, all the way till the last. The correct range to create is range(r+1, n).
    - Illustration:
    Assume you have list of len 5. 
    [13, 12, 11, 10, 9]
    At r = 0, 
    range(r+1, n) = (1, 5) = 1, 2, 3, 4 -> you want to 'check' for the following indexes

    r = 1
    range(r+1, n) = (2, 5) = 2, 3, 4

    r = 3
    range(r+1, n) = (3, 5)= 3, 4

    r = 4
    range(r+1, n) = (4, 5) = 4
2. Note how the range differs from Bubble sort. For bubble sort, the length of the range decreases every time, but the start always starts at 0. For selection sort, we want the start to be the *next* item, which means it's positioned relative to the outer iterator, r. We also want to iterate through every single element till the end, thus the stop is n. 

'''
def selectionSort(lst):
    n = len(lst)
    for r in range(n-1): #again, the number of 'cycles'.
        minimum = lst[r]
        for i in range(r+1, n): # here, note the index.
            if lst[i] < minimum:
                minimum = lst[i]
                minimumIndex = i
        if minimum < lst[r]:
            lst[r], lst[minimumIndex] = lst[minimumIndex], lst[r]
    return lst
            
lst = [29,10,14,37,13]
lst2 = [4,3,2,1]
print(selectionSort(lst))

# This is another implementation which uses the min function:
def selectionSort2(lst):
    N = len(lst)
    for L in range(N-1):
        smallest = lst.index(min(lst[L:])) # BEWARE... this is O(N) not O(1)... we cannot find the smallest index of the minimum element of (N-L) items in O(1)
        lst[smallest], lst[L] = lst[L], lst[smallest] 
    return lst