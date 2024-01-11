'''
Could it be possible this qn doesn't need DFS? 

Let's say my inputs are
1 2 
2 3
1 3

I am just going to create a CC = set()
Whenever I see an input, I check if at least 1 of the items is already in the set, if yes, I add both to the set. 
pilotCount++
However, if both are already in the set, that means they're already connected. skip. pilotCount don't change

what the. 
'''
tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    cc = set()
    pilotCount = 0
    for _ in range(m): 
        a, b = map(int, input().split())
        if a not in cc or b not in cc:
            cc.add(a)
            cc.add(b)
            pilotCount+=1
        else:
            continue
    print(pilotCount)
