'''
Let me try to generate my own test cases 
In this particular case, I want to generate 100 random catalogue IDs each, 
each of them between 0 to 1000000000
'''
import random, pyperclip


inputs = '1000000 1000000\n'
for _ in range(2000000):
    newline = str(random.randint(0,1000000000))+'\n'
    print(newline)
    inputs += newline
inputs += '0 0'
pyperclip.copy(inputs)