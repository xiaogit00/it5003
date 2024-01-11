'''
Given a list, look for the index of a particular number
'''

def lookFor(lst, num):
    n = len(lst)
    i = 0
    
    while i < n:
        if lst[i] == num: 
            print(f'{num} is found at index ', i)
            break
        i+=1

lst=[10, 99, 98, 85, 45, 59, 65, 66, 76, 12, 35, 13, 100, 80, 95]

lookFor(lst, 45)