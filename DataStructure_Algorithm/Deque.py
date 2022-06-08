# Deque - can remove and add from the front and back
# ADT - addfront, addback, removefront, removeback, size, isEmpty, size

class Deque():
    def __init__(self):
        self.items=[]
    
    def addfront(self,item):
        self.items.insert(0,item)
        self.print()
    
    def addback(self,item):
        self.items.append(item)
        self.print()
    
    def removefront(self):
        self.items.pop(0)
        self.print()
    
    def removeback(self):
        self.items.pop()
        self.print()
    
    def isEmpty(self):
        return self.items==[]

    def size(self):
        return len(self.items)
    
    def print(self):
        print(self.items)

dq=Deque()
dq.addfront(4)
dq.addfront(34)
dq.addback(94)
dq.addfront(3)
dq.addback(101)
dq.removeback()
dq.removefront()
print(dq.isEmpty())
print(dq.size())
dq.addback(33)