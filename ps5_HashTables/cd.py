'''
Initial Problem analysis:
There are 2 arrays. We simply want to find the number of 
overlapping items in the 2 arrays. 

First, they don't need to be arrays. 
'''
import sys 

lines = sys.stdin.readlines()

n, m = list(map(int, lines[0].split()))

s = set()
for num in lines[1:n+m+1]:
    s.add(int(num))
print(n+m-len(s))
# n = int(line[0])
# m = int(line[1])
# i = 2

# s = set()

# while n!=0 or m!=0:
#     for _ in range(n+m):
#         s.add(int(line[i]))
#         i+=1
#     print(n+m-len(s))
#     n = int(line[i])
#     i+=1
#     m = int(line[i])
#     i+=1





# [n, m] = list(map(int,inputs[0].split()))
# l1 = []
# l2 = []
# for line in inputs[1:n+1]:
#     l1.append(int(line))
# for line in inputs[n+1:-1]:
#     l2.append(int(line))

# common = set(l1) & set(l2)
# print(len(common))
# [n, m] = list(map(int, input().split()))

# s1 = set()
# s2 = set()
# for _ in range(n):
#     s1.add(int(input()))
# for _ in range(m):
#     s2.add(int(input()))
# input()

# ans = len(s1 & s2)

# print(ans)