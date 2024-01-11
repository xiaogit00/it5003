'''
I'll implement a stack data structure with 3 operations: peek, push, pop
'''

class Vertex: 
    def __init__(self, data):
        self.item: int = data
        self.next: Vertex = None
    
class Stack:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def peek(self):
        return self._head

    def push(self, v):
        vtx = Vertex(v)
        if self._head == None:
            self._tail = vtx
        else: 
            self._head.next = vtx
        self._head = vtx
    
    def pop(self):
        if self._head == None: return
        self._head = self._head.next
        del self._head
