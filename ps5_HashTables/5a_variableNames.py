'''
Ok now I think there's run time error. Most likely caused by my multiple
tracker. Right. So now what? This list should help keep track 
of how many multiples each c has. Like 1, etc. I can use a list, or 
I can just use a dict? The data of this list would be like:
1: 5
2: 2
3: 6        
'''
from collections import defaultdict

n = int(input()) # 200k

d = defaultdict(lambda: False)
multiple = defaultdict(lambda: 1)
for _ in range(n):
    c = int(input()) # size: 10000
    
    if d[c] == False:
        d[c] = True
        multiple[c]+=1
        print(c)
        continue
    else:
        while True:
            if d[multiple[c]*c] == False:
                d[multiple[c]*c] = True
                print(multiple[c]*c)
                multiple[c]+=1  
                break
            else:
                multiple[c]+=1


        # Check whether d[c*2] == False. 
        # If it's False, d[c*2] = True + print(c*2)
        # If it's true, check whether d[c*3] == False, 
        # and so on.
            
