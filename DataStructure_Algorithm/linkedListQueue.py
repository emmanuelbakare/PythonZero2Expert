class Node:
    def __init__(self, value):
        self.value=value 
        self.next=None 
        
class Queue:
    def __init__(self):
        self.first=None 
        self.last=None 
        self.count=0
    
    def enqueue(self, value):
        # if self.last is None:
        if not self.count:
            self.first=self.last=Node(value)
        else:
            self.last.next=Node(value)  
            self.last=self.last.next
        self.count+=1
    
    def dequeue(self):
        # if self.first is None:
        if not self.count:
            return "Queue is Empty"
        else:
            self.first=self.first.next 
            self.count -=1
        
    def print(self):
        result=""
        # if self.last is None:
        if not self.count:
            return 'No Queue'
        queue=self.first
        while(queue.next):
            result+=f'{queue.value}-->'
            queue=queue.next
        result+=f'{queue.value}'
        
        return result
    def print2(self):
        result="\n"
        # if self.last is None:
        if not self.count:
            return 'No Queue'
        queue=self.first
        while(queue.next):
            result+=f'{queue.value}\n'
            queue=queue.next
        result+=f'{queue.value}\n'
        
        return f'Queues:\n {result}Total:{self.count}\n'+'*'*50
            
    def len(self):
        return self.count
        

q=Queue()
q.enqueue({
    'name':'Segun',
    'age':43,
    'gender':'Male'
})
q.enqueue({
    'name':'Carol',
    'age':19,
    'gender':'Female'
})
q.enqueue({
    'name':'Martins',
    'age':34,
    'gender':'Male'
})
# q.enqueue(29)
# print(f"Queues: { q.print2()}Total: {q.len()}\n",'*'*50 )
q.print()  
q.dequeue()
# print(f"Queues :{ q.print2()} Total: {q.len()}" )
q.print()
q.enqueue({
    'name':'Hadiza',
    'age':22,
    'gender':'Female'
})
# print(f"Queues :{ q.print2()} Total: {q.len()}" ) 
q.print()
 
             
    