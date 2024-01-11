def insertionSort(A):
    for i in range(1, len(A)):
        e = A[i]
        j = i
        while j>0:
            if A[j-1] > e:
                A[j] = A[j-1]
            else:
                break
            j-=j
        A[j] = e




'''
****TRACING****
For insertion sort, what's happening at a high level is this. 

You select an element, e, which is 1 after your initial elem 0. 

You compare e with your first elem. If first elem bigger, set second elem as first elem. 
Then you break out of loop - > set your first elem as e. 

Then in the next iteration, you select the elem to the right of e (new elem)

You basically compare each elem to the left, 'overwriting' the position of elem each time by the preceding elem, if it is bigger. Your j decrement downwards until the smallest elem. Then finally, if you do reach there, you set your lowest elem to e. 

Take for instance [40, 13, 12, 8]

In first iteration, e=13. 
j=1
Compare A[0] with e - 40>30 true
A[1] = A[0] -> array becomes [40, 40, 12, 8] *note here, your first elem is not set yet
Since your j-- and j =0, doesn't go into while loop. 
Finally, A[0] = e = 13 -> array becomes [13, 40, 12, 8]

For second iteration, j = 2
e = 12

Compare 40 with 12 -> set A[2] as A[1] -> [13, 40, 40, 8]
Compare 13 with 12 -> set A[1] as A[0] -> [13, 13, 40, 8]
Finally, set A[0] as e -> [12, 13, 40, 8]

There, your elements are sorted. In this implementation, swaps are not taking place. 
'''