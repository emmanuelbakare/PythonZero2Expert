class Node(object):
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
    

        
class BinaryTree(object):
    def __init__(self,root):
        self.root =Node(root) 
    
    def print_tree(self,traversal_type):
        if traversal_type=="preorder":
            return self.preoder_print(self.root,"")
            # return self.preoder_print(tree.root,"")
        elif traversal_type=="inorder":
            return self.inorder_print(self.root,"")
        else:
            print(f'traversal Type: {traversal_type} is not supported')
            
    def preoder_print(self, start,traversal):
        if start:
            traversal +=(str(start.value) + "-")
            traversal =self.preoder_print(start.left,traversal)
            traversal =self.preoder_print(start.right,traversal)
        return traversal
     
    def inorder_print(self,start,traversal):
        if start:
            traversal=self.inorder_print(start.left, traversal)
            traversal +=( str(start.value) +"-")
            tranversal =self.inorder_print(start.right,traversal)
        return traversal
                 
        


tree=BinaryTree(1)
tree.root.left=Node(2)
tree.root.right=Node(3)
tree.root.left.left=Node(4)
tree.root.left.right=Node(5)
tree.root.right.left=Node(6)
tree.root.right.right=Node(7)
# tree.root.right.right.right=Node(8) 

preorder=tree.print_tree("preorder")
print('Preorder BT:',preorder)
  
inorder=tree.print_tree("inorder")
print('Inorder BT:',inorder)