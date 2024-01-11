import sys

data = []
for line in sys.stdin.readlines():
    line = line.rstrip()
    data.append(line)

record = []
records = []

for i, line in enumerate(data):
    if len(line) != 0:
        record.append(line)
    elif len(line) == 0:
        records.append(record)
        record = []
    if i == len(data) - 1:
        records.append(record)


for i, record in enumerate(records):
    r = len(record) - 1
    c = len(record[0]) - 1

    curr_r = r
    total = 0

    while curr_r>=0:
        row_asterisks = record[curr_r].count('*')
        newRow = '.'*(total) + '*'*row_asterisks + '.'*(c+1 - row_asterisks - total)
        record[curr_r] = newRow
        curr_r-=1
        total+=row_asterisks

    for row in record:
        print(row)
    print('\n') if i != len(records) - 1 else None
