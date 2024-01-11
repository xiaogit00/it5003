import random 

# def quickSort(lst):

# def quickSort(A, low, high):
#     if low<high:
#         r = low + random.randrange(high-low+1) # a random index between [low..high]
#         A[low], A[r] = A[r], A[low] # tada

#         p = A[low] # p is the pivot
#         m = low # S1 and S2 are initially empty
#         for k in range(low+1, high+1): # expore the unknown region
#             # case 2 (PATCHED solution to avoid TLE O(N^2) on input list with identical values)
#             if A[k] < p or (A[k] == p and random.randrange(2) == 0):
#                 m += 1
#                 A[k], A[m] = A[m], A[k]
#             # notice that we do nothing in case 1: A[k] > p
#         A[low], A[m] = A[m], A[low] # final step, swap pivot with A[m]
#         quickSort(A, low, m-1)

#         quickSort(A, m+1, high)
#     return A

def quickSort(A, low, high):
    if low<high:
        m = partition(A, low, high)
        quickSort(A, low, m-1)

        quickSort(A, m+1, high)
    return A
        

def partition(A, low, high):
    p = A[low]
    m = low
    for k in range(low+1, high+1):
         if A[k] < p or (A[k] == p and random.randrange(2) == 0):
              m+=1
              A[k], A[m] = A[m], A[k]  # Effect: bring all terms < pivot to left of m
    A[low], A[m] = A[m], A[low]
    return m
    
# lst = [5, 2, 4, 6, 1, 9, 113, 12, 1]
lst = [1, 2, 3, 4]

print(quickSort(lst, 0, len(lst)-1))


'''
*** TRACING FOR LIST [1, 2, 3, 4] ***
r = low + random.randrange(high-low+1)       r = 2
A[low], A[r] = A[r], A[low]                  A[0], A[2] = A[2], A[0]
lst                                          [3, 2, 1, 4]

p = A[low]                                   p = 3
m = low                                      m = 0

for k in range(low+1, high+1):              range(1, 4) -> [1, 2, 3]
                                                            *
    if A[k] < p or 
    (A[k] == p and random.randrange(2) == 0): A[1] < 3
                                                2    3
    m+= 1                                    m = 1
   A[k], A[m] = A[m], A[k]                  A[1], A[1] = A[1], A[1]

                                            range(1, 4) -> [1, 2, 3]
                                                               *
    if A[k] < p or                          A[2] < 3
    m+=1                                    m = 2
    A[k], A[m] = A[m], A[k]                  A[2], A[2] = A[2], A[2]

                                            range(1, 4) -> [1, 2, 3]
                                                                  *
    if A[k] < p or                          A[3] !< 3
    A[low], A[m] = A[m], A[low]             A[0], A[2] = A[2], A[0]
                                            [1, 2, 3, 4]
'''
    

### WHILE LOOP PARTITION FROM YOUTUBE####
# def partition(lst, l, h):
#     pivot = lst[l]
#     i, j = l, h
#     while i<j:
#         while lst[i] <= pivot: 
#             i+=1
#         while lst[j] >= pivot and j>0: #*
#             j-=1
#         if i<j:
#             lst[i], lst[j] = lst[j], lst[i]
#     lst[l], lst[j] = lst[j], lst[l]
#     return j  


'''
**TRACING***
lst = [3, 2, 4, 1]
             i  j
partition(lst, 0, 3)

pivot = 3

i = 0
j = 3

While i<j: 
      0<3  
        while lst[i] <= pivot: 3<=3; i++; i=1
                               2<=3; i++; i=2
                               4!<=3; i=2
        while lst[j] >= pivot: 1!>=3; j=3

        i<j:
            lst[2] swap with lst[3]
               4                1 
        lst = [3 ,2, 1, 4]
while i<j:
      2<3:

      while lst[i] <= pivot: 1<3; i++; i=3 
                             4!<=3; i=3
      while lst[j] >= pivot: 4>=3; j--; j=2
                             1!>=3; j=2
        i=3;j=2
        i!<j:
            don't swap
i!<j -> break out of while loop

lst[l], lst[j] = lst[j], lst[l]
l=0;j=2

lst = [1, 2, 3, 4]
3 is now sorted. 

return j
       2 -> the partition. 

Great!

*** Thoughts after tracing***
Basically this function uses 2 counters - i to find the elements greater than pivot and swap to the right, and j to find the elements smaller than pivot and swap it to the left. Once i and j criss-cross, we can say that all elements to the left of i are smaller than pivot, and all elements to the right of j are greater than pivot. This is essentially the *criteria we want* to definitively insert pivot into this element, where j now resides. 
        
An interesting behavior on the counter movements is that j will always terminate at the LHS of i. Why? That's because everything to the left of i, by definion, are smaller than your pivot. That's how they pass through i -> rmb, i is the greater than pivot filter. It catches all the big terms and throws them to the right. So anything that's on the left is smaller than pivot - which j will ultimately tumble upon. At this point, your i>j, so you don't swap and break out of the while loop. You've found the terminating condition for j, which is your partition. 
                            
lst = [3, 2, 4, 1]
             i  j
      [3 ,2, 1, 4]
             j
                i
      [1 ,2, 3, 4]
             j



'''