class House:
    def __repr__(self):
        return ''.join([f'{x} -> {y}' for x,y in self.__dict__.items()])

class HouseBuilder:
    
    def __init__(self):
        self._floor=None
        self._door=None
        self._roof=None
    
    def buildFloor(self, name):
        self._floor=name
        return self
    
    def buildDoor(self,name):
        self._door=name
        return self

    def buildRoof(self,name):
        self._roof=name
        return self
    
    #build a house using the buildHouse function
    def buildHouse(self):
        house=House()
        house._floor=self._floor
        house._door=self._door
        house._roof=self._roof
        return house 


house1=HouseBuilder()\
        .buildRoof('Build Roof')\
        .buildDoor('build Door')\
        .buildFloor('buildFloor')\
        .buildHouse()
house2 = HouseBuilder()\
        .buildFloor('Build Floor')\
        .buildDoor('build Door')\
        .buildHouse()


print(house1)
# print(house2)
    