#======list.append(item) -adds a new item to a list

# rec1=["James","Male", 34]
# rec2=["Martha","Female",45]


# print(rec1)
# rec1.append("Footballer")
# print(rec1)  

# rec1.append(rec2)
# print(rec1)





#======list.extend(iter) - add a new iterable to a list
# location= ["No 9 road","Lagos"]
# rec1.extend(location)
# print(rec1)

# set={ 2,4,6}
# tup=('j','k','k')
# x="Something"

# rec1.extend(x)
# print(rec1)

#======list.insert(index,item) - insert an item in the specified location
# rec1=["James","Male", 34]
# rec2=["Martha","Female",45]

# print(rec1)
# rec1.insert(1, "Handel")
# print(rec1)







#Value Assignment
# by value = primitive datatype -  float,integer, str
#reference = Derived datatype -list, tuple, dictionary, function arg etc


# rec1=["James","Male", 34]
# rec2=["Martha","Female",45]
# rec22=("Martha","Female",45)
# location= ["No 9 road","Lagos"]
# age1= 27
# age2=age1

# print('Age 1:', age1)
# print('Age 2:', age2)

# age2=18
# print('Age 1:', age1)
# print('Age 2:', age2)

# rec1=["James","Male", 34]

# rec3=rec1.copy()
# print('rec1 1:', rec1)
# print('rec 3:', rec3)

# rec1.append("footballer")
# # rec3.append(45)

# print('rec1 1:', rec1)
# print('rec 3:', rec3)


#======list.copy() - Make a copy of the list

# rec1=["James","Male", 34]

# rec3=rec1.copy()

# rec3=list.copy(rec1)

# print('rec1 1:', rec1)
# print('rec 3:', rec3)

# rec1.append("footballer")
# print('rec1 1:', rec1)
# print('rec 3:', rec3)





#======list.count(item) - return number of occurrences of an item in a list

# rec1=[88,23,7,66,88,23,7,88,7,2,88]
# rec2=["Apple","Mango","Banana","Apple"]

# total=rec2.count("Apple")

# print(total)














#======list.index(item) - returns the first position index of an item in thelist
# rec1=[88,23,7,66,88,23,7,88,7,2,88]
# rec2=["Apple","Mango","Banana","Apple"]


# index=rec2.index("Apple")

# index= list.index(rec1, 88)
# print(index)





#======list.pop(index) - remove items from a list from specified index pos

rec1=[88,23,7,66,88,23,7,88,7,2,88]
rec2=["Apple","Mango","Banana","Apple"]

# rec1.pop(3)
# rec1.pop(3)
# # rec1.pop()

# rec2.pop(1)
# rec2.pop()
# rec2.pop()
# list.pop(rec1,20)


# print('rec1:',rec1)
# print('rec2:',rec2)






#======list.remove(item) - remove the first occurrence of item from the list
# rec1=[88,23,7,66,88,23,7,88,7,2,88]
# rec2=["Apple","Mango","Banana","Apple"]

# # rec1.remove(23)

# list.remove(rec2,"Apple")
# list.remove(rec2,"Apple")

# print(rec2)





#=====list.clear() - empty/clear all the item in a list
rec1=[88,23,7,66,88,23,7,88,7,2,88]
rec2=["Apple","Mango","Banana","Apple"]



# rec2.clear()
# del rec2

# print(rec2)

#Clear and Delete
# del rec2[2]
# del rec2[0:2]
# del rec2
# print(rec2)







#======list.reverse() - reverse the items in a list
# rec1=[88,23,7,66,88,7,2,88,90]
# rec2=["Apple","Mango","Banana","Water Melon", "Apple"]

# print('record', rec1)
# # rec1.reverse()
# list.reverse(rec1)

# print('Reversed', rec1)



#======list.sort() - sort the items in the list
# rec1=[88,23,7,66,88,7,2,88,90]
# rec2=["Apple","Mango","Banana","Water Melon", "Apple"]

# print('Unsorted List', rec2)
# # rec2.sort()
# list.sort(rec2)
# print('Sorted List: ', rec2)

# rec1=[88,23,7,66,88,7,2,88,90]
# def removes(lst,item):
#     rems= lst.count(item)
#     if not rems:
#         return    
#     for i in range(rems):
#         lst.remove(item)
 
# removes(rec1,17)

# new_list = filter(lambda x: x != rec1, a)
# print(rec1)



# PYTHON LIST FUNCTIONS 

# len(list)
# max(list)
# min(list)
# list(iter)

rec1=[88,23,7,66,88,7,2,88,90]

# myiter=iter(rec1)
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# result=max(rec1)
# print(result)

# see={f"var{num}":f'{x**2}' for num,x in enumerate(rec1,1) if x%2==0} 
# print(see)

# list commprehension
names=["Brian","Sidi","Matthew","Ola","Emmanuel"] 

for name in names:
    print(name)



