"""
Initial Problem analysis:
Every day - the baby Panda may sneeze out 1 or 0 slimes. 
Every night - the numSlimes will double. 

The growth rate of a slime is 2**n. If, on the first day, the baby panda sneezes out 1 slime, by day 2 (n=2), the number of slime is 2^(n-1) = 2. At day 2, m= num slime present after (1) night, so it's 2^n

So for each question, I'll have the number of days (n), as well as m, the amount of slime present after n nights. 
m = 2^(n-1)

Hmm so how do I model this problem>? 

First, the total number n is either:
2**i where i < n
or 2**i + 2**j where i, j is the number of nights after panda has sneezed. 
or any number of those terms, where 

The final m can be composed of a couple of base 2 factors -> i.e. 2**7 + 2**1 + 2**3, etc. 

I would need to find out how to break m down as a sum of its factors, and then find out what are the exponents of each of the terms. 

One way would be to simply divide m by 2 recursively; For instance, if we take 128 / 2 recursively, we would run it 7 times before it becomes 1. Then we know that there is only 1 term, with the exponent of 7. Okay this is not the way to solve this. 

For instance, if you have 10, you divide it by 2 and it becomes 5, your'e screwed. 

10 is composed of 2*1 + 2**3. 

So this problem essentially becomes -> how do I break a number down to a sum of its constituent 2-based factors? 

Let's start with 10. Let's find the largest 2based factor that's under 10. That's 8. Then we find another largerst 2 based factor. 2. OK

What about 500? Largest 2 based factor: 2**8. 
500-256 = 244
Largest 2 based factor under 244: 128 (2**6)
244-128 = 116
Largest 2 based factor under 116 - 64
116-64 = 52
Largest 2 based factor under 52: 32
52-32 = 20
16
4
Okay this seems to work. But why? 

Let's try to implement this logic

****
Higher Level Implementation:
1. Decrement through n
2. Check that 2**n < 10
3. If it is, 

"""
def largestExponent(n, m) -> int:
    for i in range(n+1): # It might not reach the value of m, thus n+1
        if 2**i > m:
            return i-1
        elif 2**i == m:
            return i

def findExponents(n, m):
    if m <= 0:
        return []
    exp = largestExponent(n, m)
    return findExponents(exp, m-2**exp) + [exp]
    

# input = [int(i) for i in input().split()]

print(findExponents(13, 500))

"""
Explanation:
night-number: 1 2 3 4 5 6 7     8 9     10
slime-count:  0 0 0 0 0 0 0+1=1 2 4+1=5 10 
"""