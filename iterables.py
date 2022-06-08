#Iterables are sequence of  datatypes put together as one  derived datatype
#its a collection of datatypes stored inside a "",(),[],{}
# iterables can return its members one after the other.
#Examples of iterables are list, tuple,string,set, dictionary

lst=[12,34,56,23,4,12,41,4,7,34]
lst2=["Emmanuel", 47,"Male"]
lst3=[("James", 34),("Emmanuel", 23),("Deji",27)]
tup= (12,34,56,23,4,12,43,4,7,34)
str1="12,34,56,23,4,12,41,4,7,34"
str2="Subscribe to my Channel"
set1={12,34,56,23,4,12,41,4,7,34}
set2= {23,54,78,29}
data1={'name':'Emmanuel', 'age':47,'gender':'Male'}
data2={'names':['Emmy','Brian'], 'grades':[78,78],'ids':['29s9','9le2']}
run=False
sit=False




# 16. comprehensions  expression- a shorter way to loop through an iterable
#using a one like code
# lst5=[]
# for item in lst2:
#     lst5.append(item)
# print(lst5)


# lst5={ name:age for name,age in lst3}
# print(lst5)

 
# 15. enumerate - Add an index number to each iterable

# for num,item in enumerate(lst,1):
#     print(f'{num}: {item}')
    



# 14. for loop  -- loop through the items in an iterable

# for item in lst2:
#     print(item)



# 13. multiple assignment - unpacking iterable -

# x=lst2[0]
# y=lst2[1]
# z=lst2[2]
# x,y,z=data1.items()

# print(x,y,z)
# print(z)



# 12. all function: returns True if all of the item or expression 
# in iterable is true
# lst5=[10>3, 10>8, 20 < 10]
# lst6=[23 in lst, "Subscribe" in str2,47 in lst]
# result=all(lst6)
# print(result)



# 11. any function - returns True if any of the item or expression 
# in iterable is true
 
# lst4=[10 <3,10 > 14,10>50]
# result= any(lst4)
# print(result)




# 10. sorted function: return a list of the sorted contents of an interable
# result=sorted(lst)
# print(result)




# 9. sum function - return the sum of all the values in the iterable

# result=sum(tup)
# print(result)




# 8. in keyword - return bolean if a value is in the iterable

# result="12" in lst
# print(result)


# 7. [start:end+1:step] slice sytax- returns a sub string or part of an iterable 

# result=str2[::-1]
# print(result)



# 6. [index] syntax - returns an item in the iterable at a specified index location

# result=data2['names']
# print(result)


#5 max function - returns the maximum number in the iterable
# print('maximum',max(lst))

# print(lst)
# 4. min function - returns the mininum number in the iterable
# print('minimum',min(lst))

# 3. len function - returns the number of item in the iterable
# print(len(lst2))

# 2. list,dict,set,str class
# var=str()
# print(var)

# 1. type class
# print(type(lst))


# 0. print function
# print(lst2)


# 1.print 2. type 3.len 4 min 5. max 6. [] 7.[:]
# 8. in or not in 9. sum 10. sorted 11. any 12. all  
# 13. multiple assignment 14. for loop 15. enumerate 16. comprehension


 