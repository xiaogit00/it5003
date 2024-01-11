import sys 

class Node: 
    def __init__(self, name):
        self.name: str = name
        self.next: Node = None
        self.prev: Node = None
        self.partnerNode: Node = None
    
class LL:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def append(self, name):
        node = Node(name)
        if self._head == None: # an important corner case
            self._tail = node
            self._head = node
        else:
            self._tail.next = node 
            node.prev = self._tail
            self._tail = node
    
    def assignPartner(self, prevNode, currNode):
        prevNode.partnerNode = currNode
        currNode.partnerNode = prevNode

    def moveToBack(self, tmp):
        if tmp == self._tail:
            return self._head
        if tmp == self._head:
            next = tmp.next
            self._head = next
            next.prev = None
            tmp.prev = self._tail
            self._tail.next = tmp
            self._tail = tmp
            self._tail.next = None
            return next
        else:
            prev = tmp.prev 
            next = tmp.next
            tmp.prev = self._tail
            self._tail.next = tmp
            self._tail = tmp
            prev.next = next
            next.prev = prev
            self._tail.next = None
            return next

    def moveBehindPartner(self, tmp):
        if tmp == self._tail:
            return self._head
        partner = tmp.partnerNode
        next = tmp.next
        prev = tmp.prev
        if partner == self._tail:
            partner.next = tmp
            tmp.prev = partner
            tmp.next = None
            if tmp == self._head:
                self._head = next
                next.prev = None
            else:
                prev.next = next
                next.prev = prev
            self._tail = tmp
            return next
        else:
            partnerNext = partner.next
            partnerNext.prev = tmp
            partner.next = tmp
            tmp.prev = partner
            tmp.next = partnerNext
            if tmp == self._head:
                self._head = next
                next.prev = None
            else:
                prev.next = next
                next.prev = prev
            return next
    # def popPrintLeft(self):
    #     tmp = self._head
    #     self._head = self._head.next
    #     print(tmp.name)
    #     del tmp
    
    def get(self, i: int) -> Node:
        ptr: Node = self._head
        for _ in range(i):
            ptr = ptr.next
        return ptr 
    def lprint(self):
        tmp = self._head
        while tmp != self._tail:
            print(tmp.name)
            tmp = tmp.next
        print(self._tail.name)


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
        llst.assignPartner(llst._tail.prev, llst._tail)


tmp = llst._head
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


