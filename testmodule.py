# def greetMe(name):
#     print("Hello", name)

# def simple():
#     print("Something simpple")
    
    
# keys="9483787nh3io37378744"    


from queue import Queue  as que
import inspect

class Queue(que):
    def __init__(self, item):
        super().__init__(item)
        
    def content(self):
        result=[]
        print(self)
        for i in range(self.qsize()):
            result+=q.get(i)
        return result
    
    
    def test(self,item):
        return self.put(item)    

q=Queue(4)
print(q)
q.put(45)
q.put(45)
q.put(9876)
print(q.qsize())
q.get()
print(q.qsize())
print('*'*50)
print(q.test(100))
# print(q.content()) 


# print(inspect.getsource(Queue))

