'''
3 Operations: peek at head, euqueue (at tail), dequeue (at head)
'''

class Vertex: 
    def __init__(self, data):
        self.item: int = data
        self.next: Vertex = None
    
class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def peek(self):
        return self._head

    def enqueue(self, v):
        vtx = Vertex(v)
        if self._tail == None:
            self._head = vtx
        else: 
            self._tail.next = vtx
        self._tail = vtx
    
    def dequeue(self):
        if self._head == None: return
        self._head = self._head.next
        del self._head
