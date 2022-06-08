
# names=["James","Mike","Daniel","Jordan"]   # list of names
# nums=[23,45,233,78,53]  # list of numbers
# alphas=['a','c','f','G','Q'] # list of alphabets
# record= ["Mathew Brown", "Male","American"] #list of record
 


#ACCESSING LIST
# names=["James","Mike","Daniel","Jordan"]
# print(names[2:4]) 




# record= ["Mathew Brown", "Male","American"] 
# print(record)
# record[1]="Female"
# print(record)
# record[2]="African"
# print(record)

# del record[1]
# print(record)



# list and operators
# names=["James","Mike","Daniel","Jordan"]   # list of names
# nums=[23,45,233,78,53]  # list of numbers
# record= ["Mathew Brown", "Male","American"] #list of record
# [23,45,233,78,53,"James","Mike","Daniel","Jordan"] 

# list1=list(("Hello","Welcome","James"))
# print(list1)





# rec1, rec2=["James","Male",34],["Martha", "Female",45]
#list.append(item),
# print(rec1) 
# rec1.append("Footballer")
# print(rec1)
 
# list.extend(list), list.count(item), list.index(item)
# location=["No 9 Road","Lagos"]
# print(rec2)
# rec2.extend(location)
# print(rec2)

#list.insert(index, item)
# print(rec2)
# rec2.insert(1,"Andrew")
# print(rec2)
# , list.copy()
# rec21=rec1.copy()
# print("Record 1", rec1)
# print("Record 21", rec21)
# print("*"*50)
# rec22=rec2
# print("Record 2 ", rec2)
# print("Record 22 ", rec22)

# #DIFFENT 
# print("*"*50)
# rec1.append("New Item")
# print("Record 1", rec1)
# print("Record 21", rec21)
# print("*"*50)
# rec2.append("New Item")
# print("Record 2", rec2)
# print("Record 22", rec22)

# ,list.pop(index),
# rec1=["James","Male",34]
# rec2=["Martha", "Female",45]
# rec2.pop(1)
# print(rec2)
# list.remove(item),
# rec1.remove("james")
# print(rec1)
# list.clear(),
# print(rec2)
# rec2.clear()
# print(rec2)
# list.reverse()
# print(rec2)
# rec2.reverse()
# print(rec2)
# .list.sort()
# rec3=[45,32,65,45,875,65,4,45,66,65,35]
# print(rec3)
# rec3.sort()
# print(rec3)
#list.count(item)
# print(rec3.count(45))
#list.index(item)










# change list record
# record= ["Mathew Brown", "Male","American"]
# print(record)
# record[1]="Female"
# print("After changing \n", record)
# print("*"*40)
# print(max(nums))
# li=list((1,3,5,6,4))
# print(li)

#add list content
# record= ["Mathew Brown", "Male","American"]
# newlist=record + names #conbines item in 
# print(newlist)

# print(nums)
# nums+=alphas
# print(nums)

# #Deleting
# print(names)
# del names[2]
# print("After deleting from index 2 \n",names)

# print("*"*40)
# print(nums[0:7])
# print(max(nums))
#APPENDING
# rec1,rec2=["James","Male",34],["Martins","Female",45]
# rec1+=["Footballer"]
# rec2.append("Sailor")
# print(rec1)
# print(rec2)

# print(rec1.count("Footballer"))

# Looping through a List
#List is an iterable. You can access each item in a list using the loop command
#For..Loop, While Loop, List Comprehension 

# names= ['Matthew', 'Ryan','Boyles','Junior']
# ages=[2,45,6,3,33,21,15]

#for __loop
# for age in ages:
#     if age % 2 !=0:
#         print(age)
# for name in names:
#     print(name,'Bakare')

# total=len(names)
# ind=0

# while ind < total:
#     print(names[ind])
#     ind +=1 



# LIST COMPREHENSION
# shorter way of accessing item in a list or creating another list from 
#a previously existing list
names= ['Matthew', 'Ryan','Boyles','Junior']
ages=[2,45,6,3,33,8,21,15,24]

# newage=[]
# for age in ages:
#     if age < 20:
#         newage.append(age)
# print(newage)

# newage=[ age*2 for age in ages if age <20]
# print(newage)

newname=[ name+' Bakare' for name in names]
print(newname)

