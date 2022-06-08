# ADT stack(), pop(), push(item), peak(),isEmpty(), size()

class Stack:
    def __init__(self):
        self.items=[]
    
    def isEmpty(self):
        return self.items==[]
    def clear(self):
        self.items.clear()
        
    def push(self,item):
        self.items.append(item)
    
    def pushes(self,items=[]):
        self.items+=items
        
    def pop(self):
        self.items.pop()
    
    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print(self):
        print(self.items)
    
    def read(self):
        return self.items
    
stack=Stack()
stack.push(5)
stack.push(2)
stack.push(4)
stack.print()
stack.pop()
stack.print()
print(stack.peek())
stack.pushes([3,4,5])
stack.print()
print(stack.isEmpty())
stack.clear()
print(stack.isEmpty())
stack.print()
stack.pushes([3,4,5,6])
stack.print()
print(stack.isEmpty())
print(stack.size())

