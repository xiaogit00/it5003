n = int(input())

keywords = set()
for _ in range(n):
    s = input()
    s = s.lower()
    s = s.replace('-', ' ')
    keywords.add(s)

print(len(keywords))