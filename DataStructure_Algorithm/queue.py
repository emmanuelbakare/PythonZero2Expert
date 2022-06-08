# Queue - Queue(), enqueue(item),
# dequeue(),size(), isEmpty

class Queue:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,item):
        self.items.append(item)
        self.print()
    
    def dequeue(self):
        self.items.pop(0)
        self.print()
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items==[]
    def print(self):
        print(self.items)
    
q=Queue()

q.enqueue(4)
q.enqueue(67)
q.enqueue(32)
q.dequeue()
q.enqueue(19)
q.dequeue()