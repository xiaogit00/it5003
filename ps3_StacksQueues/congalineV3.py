import sys 
inputs = sys.stdin.readlines()
N, Q = map(int, inputs[0].split())
cmds = inputs[-1]

class TLL:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    def append(self, node):
        # If only have head and tail 
        if self.head.next == self.tail:
            self.head.next = node
            self.tail.prev = node
            node.prev = self.head
            node.next = self.tail
        else:
            prev = self.tail.prev
            prev.next = node
            node.prev = prev
            node.next = self.tail
            self.tail.prev = node
    def get(self, i):
        res = self.head
        for _ in range(i):
            res = res.next
        return res.name
        

class Node:
    def __init__(self, name, prev, next, partner):
        self.name = name
        self.prev = prev
        self.next = next
        self.partner = partner

# Hmm this should be enough right? 
head = Node('DummyHead', None, None, None) # Dummy head
tail = Node('DummyTail', None, None, None) # Dummy tail
head.next = tail
tail.prev = head
tll = TLL(head, tail)

for line in inputs[1:-1]:
    c = line.split()
    V = Node(c[0], None, None, None)
    U = Node(c[1], None, None, None)
    V.partner = U
    U.partner = V
    tll.append(V)
    tll.append(U)

tmp = head.next

for cmd in cmds:
    if cmd == 'F':
        tmp = tmp.prev
    elif cmd == 'B':
        tmp = tmp.next
    elif cmd == 'R':
        if tmp.next == tll.tail:
            tmp = tll.head.next
        else:
            prev = tmp.prev
            next = tmp.next 
            secondLast = tll.tail.prev
            secondLast.next = tmp
            tmp.prev = secondLast
            tmp.next = tll.tail
            tll.tail.prev = tmp
            prev.next = next
            next.prev = prev
            tmp = next
    elif cmd == 'C':
        if tmp.next == tll.tail:
            tmp = tll.head.next
        else:
            prev = tmp.prev
            next = tmp.next
            prev.next = next
            next.prev = prev
            partnerNode = tmp.partner
            partnerPrev = partnerNode.prev
            partnerNext = partnerNode.next
            partnerPrev.next = tmp
            partnerNext.prev = tmp
            tmp.prev = partnerPrev
            tmp.next = partnerNext
            tmp = next
    elif cmd == 'P':
        print(tmp.partner.name)

print()

curr = tll.head.next
for _ in range(N*2):
    if curr.name == "DummyTail": break
    print(curr.name)
    curr = curr.next
