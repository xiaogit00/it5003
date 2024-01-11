line = input()
try:
    [h, cmd] = line.split()
    h = int(h)
except:
    h = int(line)
    cmd = None

n = 2**(h+1)-1

if cmd:
    index = 1
    for i in cmd:
        if i == 'L':
            L = n - index 
            index *=2
            n=L
        elif i == 'R':
            R = n - index - 1
            index = index*2+1
            n=R
    print(n)
else:
    print(n)


### MEMORY LIMIT EXCEEDED ATTEMPT ###
# tree = [None] + [i for i in range(2**(h+1)-1,0, -1)]
# pos = 1

# if cmd:
#     for i in cmd:
#         if i=='L':
#             pos *= 2
#         if i=='R':
#             pos = pos*2 + 1
#     print(tree[pos])
# else:
#     print(tree[1])

#Right - my code has memory limit exceeded - this is because the tree array contains
# up to a billion items!

'''
Is there a way to not store the tree as an array? After all it's just a sequence of
numbers

The problem here is that I am trying to access the values via index arithmetics. 

Can I still access the values via index without an array? 

In some ways, it's just a sequence of numbers. The problem is, we're traversing 
downwards. So starting from 15, for instance, if we want to find the L, 
index = 1
1*2 = 2
L = 15 - (index*2-1) = 14
R = 15 - (index*2) = 13
R_Index = 3

L_index = 2
L = L - (L_index*2-1) = 14 - (2*(2-1)) = 12
R = R - (L_index*(2)) = 14 - (2*2-1) = 11

HMMMMMM

From the first 
'''
