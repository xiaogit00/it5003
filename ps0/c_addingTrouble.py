"""
Takes a string, add up the first 2 numbers, make sure they're the third. 

"""

numStr = input()
# Split them into diff strings on whitespace
nums = numStr.split()

if int(nums[2]) == int(nums[0]) + int(nums[1]):
    print('correct!')
else: 
    print('wrong!')

"""
Code Golf answer: 

A, B, C = map(int, input().split())
print("correct!" if A+B==C else "wrong!")
"""
