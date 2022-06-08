#example 1 : Inheritance Person and Teacher
# class Person:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
#         print('create a person')
        
#     def greet(self,day):
#         print('Good', day)
        
# class Teacher(Person):
#     pass
        
        
# t1=Teacher("Emmanuel",22)
# t1.greet("Afternoon")


#example 2 : Overite Teacher constructor
# class Person:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
#         print('create a person')
        
#     def greet(self,day):
#         print('Good', day)
        
# class Teacher(Person):
#     def __init__(self,school, students):
#         self.school=school
#         self.students=students
        
        
        
#example 3 : Use the super() class
# class Person:
#     def __init__(self,name, age):
#         self.name=name
#         self.age=age
#         print('create a person')
        
#     def greet(self,day):
#         print('Good', day)
        
# class Teacher(Person):
#     def __init__(self,name,age,school,students):
#         super().__init__(name,age)
#         self.school=school
#         self.students=students
#         print('create a Teacher')
       
# t1=Teacher("Name",32,"ICL",20)        
 

# print(Teacher.__mro__)




# example 4 - Multiple Inheritance
# class Person:
#     def __init__(self,name):
#         self.pname=name
#         print('create a Person')
 
        
# class School:
#     def __init__(self, name, principal):
#         self.sname=name
#         self.principal=principal
#         print('create a School')
    
# class Teacher(Person, School):
#     def __init__(self,pname,principal, sname,position):
#         Person.__init__(self,pname)
#         School.__init__(self,sname,principal)
#         self.position=position 
#         print('Create a Teacher')
        
       
# t1=Teacher("Oladele","Mrs Manford","RTL","Primary")
# print('Person:{} | School: {}'.format(t1.pname,t1.sname))
# print('Principla:{} | Position:{}'.format(t1.principal,t1.position))


# Super Class

# class Cloth:
#     def __init__(self,name, size):
#         self.name=name
#         self.size=size
        
#     def greet(self,day):
#         print("Good",day)
        
# class TShirt(Cloth):
#     def __init__(self,name, size,label):
#         super().__init__(name, size)
#         self.label=label

# tshirt1=TShirt("Graffiti Special",24,"Graffiti")

# print("Name",tshirt1.name)
# print("Tshirt Size:", tshirt1.size)
# print("Tshirt Label:", tshirt1.label)
# tshirt1.greet("Evening")



#Multiple Inheritance


class Person:
    def __init__(self,name):
        self.name=name
        print('Create a Person')
        
class School:
    def __init__(self,name, principal):
        self.name=name
        self.principal=principal 
        print('Create a School')
        
class Teacher(Person, School):
    def __init__(self,pname, sname,principal, position):
        Person.__init__(self,pname)
        School.__init__(self,sname,principal)
        self.position=position

t1=Teacher("Oladele", "RTL","Mrs Manford","Primary")
print("Person {}|Principal:{}| position: {}".format(t1.name, t1.principal, t1.position))
    