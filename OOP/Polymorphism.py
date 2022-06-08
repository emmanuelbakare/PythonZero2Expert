#Method Overriding
# class Animal:
#     def __init__(self, name):
#         self.name =name
    
#     def sound(self):
#         return "Animal Sound"
    
#     def greet(self,day):
#         return "Good {0}, {1}".format(day,self.name)
    
#     def __str__(self):
#         print(self.name)

# class Cat(Animal):
#     def sound(self):
#         return "Meow"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"
     
# d1=Dog("Doggy")
# print("Dog Name:", d1.name)
# print("Sound:",d1.sound())
# print("Greetings: ",d1.greet('Morning'))
# print("*"*30)

# c1=Cat("Kitty")
# print("Cat Name:", c1.name)
# print("Cat Sound:",c1.sound() )
# print("Greetings:", c1.greet("Afternoon"))

    
#Method Overloading
class Maths:
    def add(self,*args):
        
        if type(args[0]) is int or type(args[0]) is float:
            total=0
        elif type(args[0]) is str:
            total=""
        for val in args:
            total +=val
        print(total)

math=Maths()
math.add(1,2,50,5.4,4.5)

math.add(0.9,0.5, 1.283)

math.add("Good", " Morning")
 
        
 

























# class Person:
#     def __init__(self, name):
#         self.name=name
    
#     def get_name(self):
#         return self.name
    
# class Student(Person):
#     def __init__(self,fname):
#         super().__init__(fname)
        
#     def get_name(self):
#         return "Student: "+self.name 
     

# std1=Student("Emmanuel Bakare")
# print('Name:',std1.get_name())

# class Student:
#     def get_name(self):
#         return "Student Name"
        
# class Teacher:
#     def get_name(self):
#         return "Teacher Name"

# def people(pers):
#     print(pers.get_name())

# st1=Student()
# t1=Teacher()

# people(st1)
# people(t1)

 
 


 


# class Animal:
#     def __init__(self, name):
#         self.name =name
    
#     def sound(self):
#         return "Animal Sound"
    
#     def greet(self, day):
#         return "Good {0}, {1}".format(day,self.name)
    
#     def __str__(self):
#         print(self.name)

# class Cat(Animal):
#     def __init__(self, name):
#         self.name =name + " Purr"
        
#     def sound(self):
#         return "Meow"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"

# d1=Dog("Dog")
# print("Name:",d1.name)
# print("Sound:",d1.sound())
# print("Greetings:",d1.greet("Morning"))
# print("*"*30)
# c1=Cat("Cat")
# print("Name:",c1.name)
# print("Sound:",c1.sound())
# print("Greetings:",c1.greet("Morning"))

# for animal in (Dog('Dog'),Cat('Cat')):
#     print(animal.name)
#     print(animal.sound())
#     print(animal.greet("Morning"))
#     print("*"*30)



#Method Overloading
# def add(*args):
#     if type(args[0]) is (int or float):
#         total=0
#     elif type(args[0]) is str: 
#         total=""
    
#     for val in args:
#         total = total + val
#     return total
 
# print(add(23,45))
# print(add(23,45,0.3,10.43))
# print(add("Jane","Matthew"))
 
                

