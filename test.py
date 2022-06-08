# class Node:
#        def __init__(self, data=None, next=None):
#               self.data=data
#               self.next=next
              

# class LinkedList:
#        def __init__(self):
#             self.head=None  
       
#        def insert_at_begining(self, data):
#               node=Node(data, self.head)
#               self.head=node
              
#        def print(self):
#               if self.head is None:
#                      print('Linked List is Empty')
#                      return
              
#               out=''
#               heads=self.head
#               while heads:
#                      out+=str(self.head.data) + '---->'
#                      heads=self.head.next
#               return out  
                     
# if __name__=='__main__':
#        llist=LinkedList() 
#        llist.insert_at_begining(5)                   
#        llist.insert_at_begining(15)                    
#        # llist.insert_at_begining(54)  
       
#        llist.print()                 



# class Node:
#        def __init__(self,val):
#               self.value=val
#               self.next=None
       
#        def __str__(self):
#               return f'{self.value}-->{self.next}'

# def reverse(head):
#        previous=None,
#        current=head
#        next=None 
       
#        while current:
#               next=current.next
#               current.next=previous
              
#               previous=current
#               current=next
#        return previous
              
                       
# # node=Node(1) 
# # node2=node.next=Node(2)
# # node3=node2.next=Node(3)
# # node4=node3.next=Node(4)
# # node5=node4.next=Node(5)
# a,b,c,d=Node(1),Node(2),Node(3),Node(4)
# a.next=b
# b.next=c 
# c.next=d


# print(a)
# print(a.next)
# print(b.next)
# print(c.next)
# print(d.next)

# reverse(a)
# print('*'*20)
# print(d.next)
# print(c.next)
# print(b.next)
# print(a.next)



# def allnodes(node):
#        pass
    

from queue import Queue as que  


class Queue(que):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def listq(self):
        return [self.get() for item in range(self.qsize())]

q=Queue()
q.put(343)       
q.put(454)       
q.put(234)
q.put('Multiples')
q2=Queue()
q2.put('Another')
q2.put(34)
q2.put(True)
q.put(q2)
print(q.qsize()) 
print(q.listq())       
