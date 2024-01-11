N= 5000 # line 1 
ans =0 # line 2 
for i in range(N//2): # line 3
    j= 1
    while j < N:
        j *= 3
    for k in range(N): # line 7
        ans += 5       # line 8
print(ans) 