"""
Initial problem analysis 

For any given input, multiple its non-zero outputs repeatedly
This seems like a recursive function, with the terminating condition being that it's 
a single digit. 

Higher level implementation
1. Step 1: Strip of 0
2. Step 2: Multiply all digits 
3. Step 3: feed the results into the function again
"""

def digitalProduct(digits):
    if len(digits) == 1:
        return digits
    stripped = digits.replace('0', '')
    result = 1
    for num in stripped:
        result *= int(num)
    return digitalProduct(str(result))

print(digitalProduct(input()))


