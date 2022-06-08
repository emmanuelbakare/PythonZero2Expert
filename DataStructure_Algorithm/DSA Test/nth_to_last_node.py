class Node:
    def __init__(self, val):
        self.value=val 
        self.nextnode=None 
    def print(self):
        currentNode=self
        # nextnode=currentNode.nextnode
        compile=""
        while(currentNode.nextnode):
            compile+=f'{currentNode.value}->'
            currentNode=currentNode.nextnode
        compile+=f'{currentNode.value}'  
        return compile
    def get_node(self, val):
        pass
    
   
    
    def len(self):
        
        node=self
        count=0
        if not node:
            return count
        while(node):
            count+=1
            node=node.nextnode
        return count         
 
a=Node(1)       
b=Node(2)       
c=Node(3)       
d=Node(4)       
e=Node(5)  
f=Node(6)  
g=Node(7)  

a.nextnode=b      
b.nextnode=c      
c.nextnode=d      
d.nextnode=e      
f.nextnode=g      


def get_last_node(head):
    count=0
    while(head):
        count+=1
        print(head.value)
        lasthead=head
        head=head.nextnode 
    return (count,lasthead)

def nth_to_last_node(nth, head):
    total_node=get_last_node(head)[0]
    return total_node
    
if __name__=='__main__':
    print(a.print())  
    print(a.len())  
    # print(get_last_node(a)) 
    print('Total Nodes:',nth_to_last_node(2,a))
    
# print('something')  


     

 
    
    # while
