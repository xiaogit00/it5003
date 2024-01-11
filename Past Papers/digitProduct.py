nums = list(map(int, list(input())))


while True:
    multiple = 1
    for i in nums:
        if i == 0 : continue
        multiple *= i
    if multiple < 10:
        print(multiple)
        exit()
    else: 
        nums = list(map(int, list(str(multiple))))