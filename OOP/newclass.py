#Exampl 1- Create a class
# class Persons:
#     pass

# print(Persons)

#=========================================================



# Example 2: - Referenc a class attribute
# class Person:
#     name="Jane Hardik"
     
# print('Name:',Person.name)
# jeff=Person()
# print('Jeff:', jeff.name)
# jeff.name="Jefferson Od"
# print('Jeff2:', jeff.name)
# jeff.name=None
# print('Jeff3:', jeff.name)
# del jeff.name
# print('Jeff4:', jeff.name)





#=========================================================

# Example 2:INSTANTIATION - Define an empty class and create two instance/object of the class
# # 
# class Person:
#     name=""
    
#     def greet(self):
#         print("Hello", self.name)
    

# jane=Person()  # create an object from the defined class
# jack=Person()  # create an object from the defined class

# jane.name="Jane Hardik"
# jack.name= "Jack Benson"
# print("Jane Name:", jane.name)
# print("Jack Name:", jack.name)
# jane.greet()
# jack.greet()
#=========================================================
# Example 3 -Class Vs Instance Variable
# class Person:
#     name="Global Name"
    
# print("Class Person name:",Person.name)

# jane=Person() 
# print("Jane Person Name:",jane.name)

# jane.name="Jane Barak"
# print("Jane Person Name:",jane.name)

# jack=Person()
# jack.name="Jack Johnson"
# print("jack Person Name:",jack.name)

# del jack.name
# print("jack Person Name:",jack.name)
# print("jane Person Name:",jane.name)






#=========================================================
# Example 4.1- Self Keyword
# class Person:
#     def run(self):
#         print('Start Runing',)
        
# jane=Person() 
# jane.run()



# Example 4.2
# class Person:
#     def run(self, when):
#         print('Start Runing', when)
        
# jane=Person() 
# jane.run("Later")

#=========================================================
# Example 5.1 - Create Constructor - Instantiate with parameters

# class Person:
#     def __init__(self):
#         print('New Person Created')

# jane=Person()   
# jack=Person() 


# Example 5.2- Constructor with  parameters
# class Person:
#     def __init__(self,name):
#         self.name=name
#         print('Create Person', name)

# jane=Person("jane")    
# jack=Person("jack") 
# print('Jacks Name:',jack.name)   
# print('jane Name:',jane.name)   
# print('Person name:',Person.name)

#Example 6 -Doctrings
class Person:
    'Person Class documentation here'
    def __init__(self,name):
        'instantiate with name of person'
        self.name=name
        print('Create Person', name)

    def greet(self,day):
        ''' greet(self,day) greet method for person. in day parameter  
           sep"ecify daytime morning, afternoon or evening'''
        print("Good", day)
  
# print(Person.__doc__)
# help(Person.greet)
print(Person.__name__) 

 