import sys 

#### CLASS DEFINITION STARTS ######
class Node: 
    def __init__(self, name):
        self.name: str = name
        self.next: Node = None
        self.prev: Node = None
        self.partnerNode: Node = None
    
class LL:
    def __init__(self):
        headNode = Node('dummyHead')
        tailNode = Node('dummyTail')
        self._head = headNode
        self._tail = tailNode
        headNode.next = tailNode
        tailNode.prev = headNode
    
    def append(self, name):
        node = Node(name)
        if self._head.next == self._tail: # empty node
            self._head.next = node
            self._tail.prev = node
            node.prev = self._head
            node.next = self._tail
        else:
            prevLast = self._tail.prev
            prevLast.next = node
            self._tail.prev = node
            node.prev = prevLast
            node.next = self._tail


    def assignPartner(self, prevNode, currNode):
        prevNode.partnerNode = currNode
        currNode.partnerNode = prevNode

    def moveToBack(self, tmp):
        if tmp == self._tail.prev:
            return self._head.next
        prev = tmp.prev
        next = tmp.next
        lastNode = self._tail.prev
        lastNode.next = tmp
        self._tail.prev = tmp
        tmp.next = self._tail
        tmp.prev = lastNode
        prev.next = next
        next.prev = prev
        return next

    def moveBehindPartner(self, tmp):
        prev = tmp.prev
        next = tmp.next
        partnerNode = tmp.partnerNode
        partnerNodeNext = partnerNode.next 
        partnerNode.next = tmp
        partnerNodeNext.prev = tmp
        tmp.prev = partnerNode
        tmp.next = partnerNodeNext
        prev.next = next
        next.prev = prev
        if next == self._tail:
            return self._head.next
        return next
    
    def get(self, i: int) -> Node:
        ptr: Node = self._head
        for _ in range(i):
            ptr = ptr.next
        return ptr 

    def lprint(self):
        tmp = self._head.next
        while tmp != self._tail.prev:
            print(tmp.name)
            tmp = tmp.next
        print(self._tail.prev.name)

#### CLASS DEFINITION ENDS ######


n = q = 0
llst = LL()

for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    if line == '':
        break
    
    if i == 0:
        [n, q] = list(map(int, line.split()))
    elif i == n+1:
        instructions = line
    else:
        couple = line.split()
        llst.append(couple[0])
        llst.append(couple[1])
        llst.assignPartner(llst._tail.prev.prev, llst._tail.prev)


tmp = llst._head.next
for command in instructions:
    if command == 'F':
        tmp = tmp.prev
    if command == 'B':
        tmp = tmp.next
    if command == 'P':
        print(tmp.partnerNode.name)
    if command == 'R':
        tmp = llst.moveToBack(tmp)
    if command == 'C':
        tmp = llst.moveBehindPartner(tmp)
        
print('\n')
llst.lprint()


