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

for record in records:
    print(list(zip(*record)))