T = int(input())

for _ in range(T):
    i, n = map(int, input().split())
    top = 1
    btm = 1
    seq=[]
    while n > 1:
        if n%2 == 0: #even
            seq.append('L')
        else:
            seq.append('R')
        n = n//2
    seq.reverse()
    for j in seq:
        if j == 'L':
            btm = top + btm
        else:
            top = top + btm 
    print(f'{i} {top}/{btm}')

