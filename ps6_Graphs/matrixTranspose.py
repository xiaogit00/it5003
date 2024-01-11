from collections import defaultdict

m, n = map(int, input().split())

matrix = defaultdict(list)
newMatrix = defaultdict(list)
for i in range(1, m+1):
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    if line1 == [0]:
        matrix[i] = []
        continue
    for j in range(line1[0]):
        matrix[i].append((line1[j+1], line2[j]))

for rowIndex, elems in matrix.items():
	for elem in elems:
		newMatrix[elem[0]].append((rowIndex, elem[1]))

print(n, m)
for rowIndex, elems in newMatrix.items():
	elemIndexes = list(map(str, [elem[0] for elem in elems]))
	elemValues = list(map(str, [elem[1] for elem in elems]))
	print(len(elems), ' '.join(elemIndexes))
	print(' '.join(elemValues))

