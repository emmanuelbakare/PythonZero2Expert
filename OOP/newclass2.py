# init
#docstring 
# class Person:
#     ''' Person example.
#         init method defiled in this example
#         call the class with Person(string)
#     '''
#     def __init__(self,name):
#         self.name=name
    
#     def greet(self,day):
#         "This is the traditional greeting style for Person"
#         print("Good", day)
        


# jane=Person("Jane Mallock")
# mark=Person("Mark")
# # __doc__
# # help()
# help(Person.greet)




class Record:
    
    def __init__(self, first="", last=""):
        self.firstname=first
        self.lastname=last
    
    def __str__(self):
        return f"{self.firstname} {self.lastname}"

from enum import Enum

class Locations(Enum):
    NORTH="North"
    SOUTH="South"
    WEST="West"
    EAST="East"


dire=Locations.NORTH
dire2=Locations.SOUTH
print(dire)
print(dire2 )

# EmpRec=Record("Deji","Bakare")
# SalesRec=Record("Kolade", "James")


# print(EmpRec)
# print(SalesRec)

# print(f'Class: {EmpRec.__class__.__name__}') 





#Example of a Class
# class Person:
#     name="Global Name"
#     def running(self,when):
#         print('Start Running', when)

# jane=Person()
# jane.running("Now")
# jane.running("Tomorrow")




# print("Class Person Name:", Person.name)    

# jane=Person() 
# print("Jane Person Name:", jane.name)

# jane.name="Jane Barak"
# print("Jane Person Name:", jane.name)

# jack=Person()
# print("Jack Person: ", jack.name)

# jack.name="Jack Johnson"
# print("Jack Person 2: ", jack.name)

# del jack.name
# print("Jack Person3:",jack.name)
# print("Jane:", jane.name)


#__init__() Method
