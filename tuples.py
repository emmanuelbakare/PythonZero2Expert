
# Tuple Examples - Creating Tuples
t0=tuple() 
t1 = () 
t2 = (45,) 
t3= (34,65,2,56,7,0,4)
t4=("Banana", "Mango","Orange")
t5=("Emmanuel",45,"Male",57.5)

t6=(1,2,3)
t7=(10,20,30)
t8=[1,2,3,4,5,5,4,3,2,1]

print(t3[-5:-2]) 
# records=[
#     ("Moses","Male", 25),
#     ("Rosemary","Female",18),
#     ("Mandy", "Female", 19)
#     ]

# for name, gender, age in records:
#     print(f'my name is {name}, I am {age} years old and a {gender}')




# Tuple Functions  - len min max tuple
# result=tuple(range(30))
# print(result)



#Concatenate +, repeatition *, membership in
# print(t5)
# print(t6)
# print(t5+t6)

# t5+=t6
# print(t5)

# print(t5*3)

# print( 10 not in t6)

# for item in t5:
#     print(item)
















# print('t0= ',t0)
# print('t1= ',t1)



#Accessing Items in a Tuple (Indexing & Slicing)
# print('t3=',t3[-3])

#slice prints subset of the tuple
# tuple[startIndex:lastItem] or tuple[startIndex:lastindex-1]
# print(t3[:3])
# Reverse tuple[item:index]

# print(t3[-5:-2])

#Deleting Tuple
# print(t4)

# del t4
# print(t4)



















# records=[
#     ("Moses","Male", 25),
#     ("Rosemary","Female",18),
#     ("Mandy", "Female", 19)
#     ]

# for rec in records:
#     print("Name:{0}\nGender:{1}\nAge:{2}".format(rec[0],rec[1],rec[2]))
#     print('*'*20) 

    



# current=0 
# for _ in records:
#     print("Record {0}".format(current+1).center(20,'*'))
#     print("Name: {}\nMonth: {}\nAmount: {}".format(
#         records[0][current],
#         records[1][current],
#         records[2][current]))
#     current +=1 
    # print("="*30)
    
# records=[("Moses","Male",25),
#         ("Roseline","Female",23),
#         ("Mandy","Female",19)]
# # for rec in records:
# #     print( rec[0])

# for rec in records:
#     print("Name:{} Gender:{} Age:{}".format(rec[0],rec[1],rec[2]))
    
    
# for rec in records:
#     print("Name:{}\nGender:{}\nAge:{}".format(rec[0],rec[1],rec[2]))
#     print("*"*10)