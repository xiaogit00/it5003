N, t = map(int, input().split())
A = list(map(int, input().split()))
print(7)

if A[0] > A[1]:
    print("Bigger")
elif A[0] == A[1]:
    print("Equal")
else:
    print("Smaller")

print(sorted(A)[1])

print(sum(A))

A1 = list(map(lambda x: chr(x%26+97), A))

print(''.join(A1))

i = 0
