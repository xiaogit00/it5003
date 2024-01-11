'''
AND: &
OR: |
XOR: ^
NOT: ~ -> not an actual negation -> works on signed integers
Shifting: 
'''
n1 = 23477
n2 = 31213

n3 = n1 & n2

# print(bin(n1)[2:])
# print(bin(n2)[2:])
# print(bin(n3)[2:])

n4 = n1 | n2

# print(bin(n4)[2:])

#XOR -> can't have both. Has to be different

n5 = n1 ^ n2 

# print("0" + bin(n5)[2:])

# Negation

# print(bin(0b1111 - 0b1010))

# Shifting
# Basically dividing by 2 and multiplying by 2

number = 20
print("0"+bin(number)[2:])
number <<= 1 # shift to left

print(bin(number)[2:])
# Effect: you're increasing the power of each bit by 1,
# effectively doubling each power 2-> take everything x 2

number >>= 2
print(bin(number))