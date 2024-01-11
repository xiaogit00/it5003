class Vertex: 
    def __init__(self, data):
        self.item: int = data
        self.next: Vertex = None
    
class SLL:
    def __init__(self):
        self._head = None
        self._tail = None

    def get(self, i: int) -> Vertex:
        ptr: Vertex = self._head
        for _ in range(i):
            ptr = ptr.next
        return ptr 

    def appendleft(self, v):
        vtx = Vertex(v) # create new vertex vtx from item v
        vtx.next = self._head # link this new vertex to the (old) head vertex
        if self._head == None: self._tail = vtx # if previously it was an empty SLL, then tail = head too
        self._head = vtx # the new vertex becomes the new head

    # https://visualgo.net/en/list?slide=3-12
    def append(self, v):
        if self._head == None: # an important corner case
            self.appendleft(v)
        else:
            vtx = Vertex(v) # create new vertex vtx from item v

            # The O(N) version (if we do not use tail pointer)
            # tail = self.head # we have to start from head
            # while tail.next != None: # while we have not reached the last element, O(N) - the slow part
            #     tail = tail.next # the pointers are pointing to the higher index
            # now we can use the tail pointer, after searching for it in O(N)

            self._tail.next = vtx # just link this, as tail is the i = (N-1)-th item, O(1)
            self._tail = vtx # now update the tail pointer, O(1)
    def insert(self, i, v):
        pre: Vertex = self.get(i-1)
        aft = pre.next
        vtx = Vertex()
        vtx.item = v
        vtx.next = aft
        pre.next = vtx

    def front(self):
        if self._head == None: return None # avoid crashing when the SLL is empty
        return self._head.item

    def back(self):
        if self._tail == None: return None
        return self._tail.item

    # https://visualgo.net/en/list?slide=3-15   
    def popleft(self):
        if self._head is None: return # avoid crashing when SLL is empty
        self._head = self._head.next # book keeping, update the head pointer
        if self._head == None: self._tail = None # if the SLL is now becomes empty, then tail = NULL too
        # remarks: as nothing points to old head, Python's garbage collector will remove it

    def empty(self):
        return self._head == None
    
    def remove(self, i):
        pre: Vertex = self.get(i-1)
        target: Vertex = pre.next
        aft = target.next
        pre.next = aft
        del target 
    
    def popright(self):
        pre: Vertex = self._head
        tmp = self._head.next
        while (tmp.next != None):
            pre = pre.next
            tmp = tmp.next
        pre.next = None
        del tmp
        self._tail = pre



    


# l = SLL()
# l.appendleft(5)
# l.appendleft(2)
# l.appendleft(7)

# print(l.back()) # output 7 as the SLL is 7 (head)->2->5 now
# l.popright()
# print(l.back())
