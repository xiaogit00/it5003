'''
Divisible by 7: n%7==0
Multiples of 5: n%5==0

'''
ans = []
for i in range(1500, 2701):
    if i%7==0 and i%5==0:
        ans.append(i)

print(ans)