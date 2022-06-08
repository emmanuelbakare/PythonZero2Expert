class Node:
       def __init__(self, data=None, next=None):
              self.data=data
              self.next=next
              

class LinkedList:
    def __init__(self):
        self.head=None  
        self._size=0
    
    def insert_at_begining(self, data):
            node=Node(data, self.head)
            self.head=node
            self._size+=1
    
    def len2(self):
        return self._size

    
    def insert_at_end(self, data):
        if self.head is None:
            self.head=Node(data,None)
            self._size+=1
            return
        
        heads=self.head
        # traverse to the last node
        while heads.next:
            heads=heads.next
        #add a node to the last node
        heads.next=Node(data,None)
        self._size+=1
        
        
    def insert_values(self,value_list, new=False, at="end"):
        if new:
            self.head=None
        # if at=="begining": list.reverse(value_list)    
        for value in value_list:
            if at=="end":
                self.insert_at_end(value)
            elif at=="begining": 
                
                self.insert_at_begining(value)   
            
            
    def len(self):
        if self.head is None:
            return 0
        itr=self.head 
        count=0
        while itr:
            count +=1
            itr=itr.next
        return count 
                
    def print(self):
            if self.head is None:
                    print('Linked List is Empty')
                    return
            
            out='' 
            heads=self.head
            while heads.next:
                    out+=str(heads.data) + '--->'
                    heads=heads.next
            out+=str(heads.data)
            print(out)   
                     
if __name__=='__main__':
       llist=LinkedList() 
       llist.insert_at_begining(19)                    
       llist.insert_at_begining(15) 
       llist.insert_at_begining(54)  
       
       llist.insert_at_end(40)
       llist.insert_at_begining(7) 
       llist.insert_at_end(100)
       
       names=['Ahmed','Segun',90,4,'Olamide' ]
       llist.insert_values(names, at="begining")
       
       llist.print()
       print(llist.len2())                