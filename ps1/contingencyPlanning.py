'''
https://nus.kattis.com/courses/IT5003/IT5003_S1_AY2324/assignments/aa9x5h/problems/contingencyplanning

Initial problem analysis: 
This problem can be reduced to a summation of nPr problem - where nPr is the number of ways of arranging n zombies in r positions. 

For instance, given 4 zombies, we want to find: nPr(4, 4) + nPr(4, 3) + nPr(4, 2) + nPr(4,1)

And that'll be the solution to this problem. 
'''
n = int(input())

def factorial(n):
    if n == 1:
        return 1
    return factorial(n-1) * n

def nPr(n, r):
    # So for this function, I know the formula is: nPr = n!/(n-r)!
    if n-r <= 0:
        return int(factorial(n))
    else:
        return int(factorial(n)/factorial(n-r))

orderings = 0
for i in range(1, n+1):
    orderings += nPr(n, i)

if orderings > 10**9:
    print("JUST RUN!!")
else: 
    print(orderings)
