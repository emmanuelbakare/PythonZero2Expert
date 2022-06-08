''' 
1. A function is a block of code that runs whenever it is 
initiated or called.
''' 

'''
2. A function helps us to break a very large 
program into smaller understandable and 
reusable pieces. It is like putting an 
piece of action or task in your program into a
block of codes
'''
'''
3. With Functions, repetitive codes or actions does 
not have to be written over again, you only have 
to call the function to do it as many times as you 
want.
'''


# Function Syntax
# def function_name():
#     codes
#     code





# sample function 
def greet(msg):
    print("Hello", msg)

# greet("Emmanuel")


# def makeLemonade(igr1,igr2,igr3):
#     # print("Mix {},{},{} to make Lemonade".format(igr1,igr2,igr3))
#     return 45

# print(makeLemonade("Lemon","Sugar","Water"))

# def add2(a,b):
#     return a+b

# sum1=add2(14,10)
# print(sum1)
# sum2=add2(47,50)
# print(sum1)
# print(sum2)

# a,b=40,50
# def add3():
#     return a+b

# print(add3())
# print(add3())








   



   
# 1. takes in argument but doesn not return a result   
# result=0
# def add(a,b):
#     # global result
#     result=a+b
#     print("Result inside def:",result)
# print("Result outside def",result)
# add(5,10)
# print("Result after add func",result) 


# 2. Takes in an argument and returns a result
# def add2(a,b):
#     return a+b 


# print(add2(49,33))
# or
# result=add2(49,33)
# print(result)
 

# 3.  does not take in an argument, does not return result but
# prints out an output  
# a,b,result=4,5,0
# def add3():
#     print("A + B=",a+b)
    
# add3()


# 4. does not take an argument put returns a value
# a,b=40,5
# def add3():
#     return a+b
    
# result=add3()
# print(result)
# or
# print(add3())

# ARGUMENTS

# 1. Required Arguments
# def add2(a,b):
#     return a+b 







# 2. Keyword argument
# def greetings(name, moment):
#     print("Hello", name, "How are you this",moment)

# # greetings(moment="afternoon", name="Abraham")
# greetings(name="James", moment="evening")











# def greetings(age,name, moment):
#     print("Hello", age,"years old,",name, "How are you this",moment)

# # greetings(15,moment="afternoon", name="Abraham")  #works
# greetings(moment="afternoon", name="Abraham",15) #throw error




# 3.Default Argument   argument
# The function definition as a predefined value in the argument
# def intro(name="unspecified", info="I am unknown"):
#     return "My name is {}  {}".format(name,info)

# print(intro())
# print(intro(info="I am a Nurse"))
# print(intro("Matthew",info="I am a Doctor"))
# print(intro(name="Silvester",info="I am an Artist"))










# 4. Variable Length
# def addall(*nums):
#     sum=0
#     for num in nums:
#         sum+=num
#     return sum

# result = addall(2,323,54,23,6,43,2,87,90,88)

# print(result)









# 5. Arbitrary Keyword argument ---Variable length keyword argument

# def info(**kwargs):
#     for key in kwargs:
#         print("{} : {}".format(key,kwargs[key]))

# info(name="Mathew", age=45, date="Jan 2021", gender="Male", group="First")


# def test(rec,*args, **kwargs):
#     print("record: ", rec)
#     print("All args", args)
#     print("All kwargs", kwargs)

# test("rec233",2,3,4,5,67, name="Emmanuel", age=67, gender="male")







# VARIABLE SCOPE
# result=40
# def add(a,b):
#     sum=a+b
#     return sum + result

# print(add(3,4))
# print(result)

# result=40
# def add(a,b):
#     result=a+b
#     return result  

# print(add(3,4))
# print(result)

 

# PASSING VALUE BY REFERENCE

mylist=[10,20,30]

# def addlist():
#     mylist.append(40)
#     print(mylist)

# print(mylist)
# addlist()
# print(mylist)






# example 2  --Mutable object like String
# name= "Abraham"

# def namer():
#     greet="Welcome "+name
#     print(greet)
    

# namer()
# print(name)
    

# lister2=[1,3,5]

# def lister():
#    lister2.append(lister2)
    

# lister(45)
# print(lister2)


# VARIABLE SCOPE
# ======================
# name="Emmanuel"
# season='winter'

# def show_name():
#     name="Matthew"
#     print('I am ', name)

# def show_season():
#     season='Autum'
#     print('its', season, name)
    
# def greet_name(day):
#     name='Nicole'
#     print('Good', day,name,' it is ', season)

# print(name)
# show_name()
# show_season()
# greet_name('afternoon')


 

















#LAMBDA EXPRESSION
#  Lambda expression are python function which are anonymous. They have no name and does not use the def keyword. 
# It takes in any number of arguments but return only one expression

# Syntax
# lambda argument(s): expression

# def greet(day):
#     print("Good ", day) 


# greet('morning') 

# greet= lambda day:print('Good', day)

# greet('Afternoon')

# sum= lambda a,b : a+b

# print(sum(12,19))


# print((lambda a,b : a+b)(15,10))

#filter (function(), iterable) 

# list1=[23,45,65,32,33,12,44]

# f1=filter(lambda x:x<60,list1)
# print( list(f1))


# name="Joan"
# age=22

# print("My name is {0} and I am {1} years old".format(name, age))


