


# class Pill:
#     def __init__(self,user):
#         self._unplug=None 
#         self._name=""
#         self.user=user 
        
#     def red(self):
#         self._name="Red"
#         self._unplug=True
    
#     def blue(self):
#         self._name="Blue"
#         self._unplug=False
    
#     def __str__(self):
#         return f"{self.user} Took the {self._name} Pill: Unplugged? {self._unplug} "


# class Matrix(Pill):
#     pass
    
    
    
# neo=Pill("Neo")
# neo.blue()
# print(neo)


# print("*"*30)

# trinity=Pill("Trinity")
# trinity.red()
# print(trinity)


# print("*"*30)

# trinity=Pill("Trinity")
# trinity.name="Yellow"
# trinity.unplug=True
# print(trinity)


        


















#public Method

# class Matrix:
#     def __init__(self,user):
#         self.unplug=None
#         self.name=""
#         self.user=user
    
#     def red(self):
#         self.name="Red"
#         self.unplug=True
        
#     def blue(self):
#         self.name="Blue"
#         self.unplug=False
    
#     def __str__(self):
#         return "*{0} Took the {1} Pill* \nUnplugged:{2}\n".format(self.user,self.name,self.unplug)

# matrix=Matrix("Neo")
# matrix.red()
# print(matrix)
# matrix.blue()
# print(matrix)
# matrix.name="Yellow"
# print(matrix) 



    
        # print(self.blue())
        

#PROTECTED -Example  2


# class Matrix:
#     def __init__(self,user):
#         self.unplug=None
#         self._name=""
#         self.user=user
    
#     def red(self):
#         self._name="Red"
#         self.unplug=True
        
#     def blue(self):
#         self._name="Blue"
#         self.unplug=False
    
#     def __str__(self):
#         return "*{0} Took the {1} Pill* \nUnplugged:{2}\n".format(self.user,
#                                                                   self._name,
#                                                                   self.unplug)

# matrix=Matrix("Trinity")
# matrix.red()
# print(matrix)

# print("*"*30)
# matrix.name="Yellow"
# print(matrix) 



#PRIVATE VARIABLE

# class Car:
#     def __init__(self, speed, color):
#         self.__speed=speed
#         self.__color=color
    
#     def getSpeed(self):
#         return self.__speed

#     def setSpeed(self,value):
#         if value < 90:
#             self.__speed=100
#         else:
#             self.__speed=value
                 
#     def setColor(self, value):
#         self.__color=value
#     def __str__(self):
#         return f'Car Speed:{self.__speed}, Color:{self.__color}'
        
# honda=Car(230,'red')
# print(honda)

# print('speed is', honda.getSpeed())
# honda.setSpeed(50)
# print('speed is', honda.getSpeed())
# honda.setColor("Blue")
# print(honda)

# honda.setSpeed(10)
# print('speed is', honda.getSpeed())
 
















# PRIVATE -SETTERS AND GETTERS
# class Car:
#     def __init__(self,speed,color):
#         self.__speed= speed
#         self.__color=color 
        
#         def getSpeed():
#             return self.__speed
        
#         def setSpeed(value):
#             self.__speed= speed
        
# honda=Car(230,'Red')
# print(honda._Car__speed)








# INNER CLASSES


            
# class Person():
#     def __init__(self, first,last):
#         self.name=Person.Name(first,last)
#     def __str__(self):
#         return f'{self.name.first}, {self.name.last}'
    
#     class Name():
#         def __init__(self,first,last):
#             self.first=first
#             self.last=last 
 
# p=Person("Niife","Bakare") 
# print(p)

 


 
    
         
        

            


 
     
    
        








# protected Method
# class Person:
#     def __init__(self,name):
#         self._name=name
    

# class Student(Person):
    
#     def get_name(self):
#         return self._name

# std1=Student("James")
# pers=Person("Matthew")

# print(std1.get_name())
# print(pers.name)



# private Mode

# class Car:
#     def __init__(self, speed, color):
#         self.__speed=speed
#         self.__color=color

#     def getSpeed(self):
#         return self.__speed
    
#     def setSpeed(self, value):
#         self.__speed=value
    

# honda=Car(123,'red')
# print("Speed:",honda.getSpeed())
# honda.setSpeed(500)
# print("New Speed:",honda.getSpeed())


        



#Inner Class


    
    
        
        

class Student:
    class Grade:
        def __init__(self, subject, mark):
            self.subject=subject
            self.mark=mark
            
        def __str__(self):
            return f"subject:{self.subject},mark:{self.mark}"
        
    def __init__(self, name, subject, mark):
        self.name=name
        self.grade=Student.Grade(subject, mark)
        
        
    def __str__(self):
        return f" Name:{self.name}, {self.grade}"

st1=Student("Jacob","Computer", 89)
print(st1)




























# class Grade:
#     def __init__(self, subject, grade):
#         self.subject=subject
#         self.grade=grade
#     def __str__(self):
#         return f" Subject:{self.subject}, Mark:{self.grade}"
        
# class Student:
#     def __init__(self,name,subject, mark):
#         self.name=name
#         self.grade=Grade(subject, mark)
        
#     def __str__(self):
#         return f"Name:{self.name}, {self.grade}"

# st1=Student("James","Maths", 80)
# print(st1) 


        
# class Student:
#     def __init__(self,name,subject, mark):
#         self.name=name
#         self.grade=Student.Grade(subject, mark)
        
#     def __str__(self):
#         return f"Name:{self.name}, {self.grade}"
    
#     class Grade:
#         def __init__(self, subject, grade):
#             self.subject=subject
#             self.grade=grade
#         def __str__(self):
#             return f" Subject:{self.subject}, Mark:{self.grade}"

# st1=Student("James","Maths", 80)
# print(st1) 

        