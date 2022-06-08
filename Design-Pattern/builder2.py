class Computer:
    def __repr__(self):
        return ''.join([f'{x}->{y}' for x,y in self.__dict__.items()])

class ComputerBuilder:
    def __init__(self):
        self.computer=Computer()
        
    def memory(self, name):
        self.computer._memory=name
        return self 
    
    def keyboard(self, name):
        self.computer._keyboard=name
        return self 

    def hdd(self,name):
        self.computer._hdd=name
        return self
    
    def build(self):
        return self.computer

comp=ComputerBuilder()
# print(type(comp))
comp1=comp.memory('Add Memory')\
    .hdd('Hard Disk Drive')\
    .keyboard('Keyboard')\
    .build()

print(comp1)  
 
        