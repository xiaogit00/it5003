import sys 
from heapq import heappush, heappop
from math import inf
from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Node:
    pos: (int, int)
    index: int

    def __lt__(self, other):
        return self.index < other.index

input = sys.stdin.readlines()
m = int(input[0])
if m==0:
    print('-')
    exit()
n = m+2
s = Node(tuple(map(int, input[-2].split())), 0)
dest = Node(tuple(map(int, input[-1].split())), m)
nodes = [s]
for i, line in enumerate(input[1:-2]):
    x, y = map(int, line.split())
    v = Node((x, y), i)
    nodes.append(v) # i is the index, used for printing later 
nodes.append(dest)
d = defaultdict(lambda: inf) # Hash table used to store shortest distance. key = coordinate
d[s.pos] = 0

p = defaultdict(lambda: None) # parent of each coordinate, stored as node
p[s.pos] = None
q = []
finalOrder = []
heappush(q, (0, nodes[0])) # sort by weight
while q:
    (w, V) = heappop(q)
    if d[V.pos] > d[dest.pos]: continue
    
    if V.pos == dest.pos:
        parentNode = p[V.pos]
        while True:
            if parentNode.pos == s.pos: 
                if len(finalOrder) == 0: 
                    print('-')
                    exit()
                for i in range(len(finalOrder)):
                    print(finalOrder.pop())
                exit()
            finalOrder.append(parentNode.index)
            parentNode = p[parentNode.pos]

    r, c = V.pos[0], V.pos[1]
    for U in nodes:
        if V.pos == U.pos: continue
        r1, c1 = U.pos[0], U.pos[1]
        dSquared = abs(r1-r)**2 + abs(c1-c)**2
        # print(type(w), type(d[U.pos]))
        if w + dSquared < d[U.pos]:
            d[U.pos] = w + dSquared
            heappush(q, (d[U.pos], U))
            p[U.pos] = V