
#Create a Set -- set(iterables)   iterables =List,tuple,string
# lst=["Monday","Tuesday","Wednesday"]
# days=set(lst)
# print(days)

# months={'January', 'February', 'March'}

# s1={1,2,3,1,2,3,1,2,3}
# print(s1)

# r1=set(range(10))
# print(r1)

# str1="Subcribe to my channel"
# print(set(str1))

data={"name":"Emmanuel", 'age':23, 'gender':'Male'}

dataset=set(data.items())
print(dataset)













#SET INTERACTION METHODS
# UNION, INTERSECTION, DIFFERENCE, MEMBERSHIP


# women= {"shoes", "bags", "necklace", "skirt", "blouse","socks"}
# men = {"shirt", "pants", "shoes","tie","socks"}






#MEMBERSHIP -isdisjoint(iterable),issubset(iter),.issuperset(iter)

# num1= {1,2,45,76,8,99}
# num2={2,8,1}
# num3={10,20,30}
# num4=[45,76,99]


#Common Set Functions - len, min, max, copy

# MIN, MAX, LEN
# result=len(num3)
# result=min(num3)
# result=max(num3)
# print(result)

#COPY SET
# num22=num2.copy()
# num21=num2

# for item in num1:
#     print(item)






# DISJOINT: - returns true if none of the items in the sets are similar
# result=num2.isdisjoint(num3)
# print(result)


# ISSUBSET –returns true if every item on the left side (num2) is on the right side(num1)
# result=num2.issuperset(num1)
# print(result)

# ISSUPERSET – returns true is set A is the parent set of Set B i.e. B is in A
# result=num1.issuperset(num2)
# print(result)

# print(len(num3))




#UNION
# allclothes=women.union(men)
# print(allclothes)

#INTERSECTION
# similar=women.intersection(men)
# print(women)
# women.intersection_update(men)
# print(women)

# print(similar)

#DIFFERENCE
# difference= women.difference(men)
# # print(difference)

# print(women)
# women.difference_update(men)
# print(women)


 


# Adding Item To set- set.add(item), set.update(iterable)
# print(months)
# months.add("April")
# print(months)

# print('Days:',days)
# months.update(days)
# print('Days & Month:', months)



#REMOVE ITEM- set.remove(item), set.discard(item), set.pop(), set.clear()
months={'January', 'February', 'March','April'}

# print(months)
# months.clear()
# print(months)
# months.remove("March")
# print(months)

# months.discard("February")
# print(months)

# months.pop()
# print(months)




























# names={"Matthew","Deji","Shadrach","Segun"}
# info={("Shirt", "Pants"),("Bag","Necklace"),"Fashion",30.2,True}
# info2={("Shirt", "Pants"),("Bag","Necklace"),"Fashion",30.2,True}

# print('info2',info2)
# print('info',info)
#CREATE A SET set(iterable) list|tuple|set|range
# days= set(["Monday","Tuesday","Wednesday"])
# months={'January', 'February', 'March'}
# test=set(range(10))
# print(days)
# print(months)
# print(test)
# print(set("Welcome"))




 #ADD ITEM TO SET
# print(days)
# days.add("Thursday")
# print(days)
#UPDATE(iterable)
# weekend=["Monday", "Friday", "Saturday", "Sunday"]
# days.update(weekend)
# print(days)

# totaldays=days.union(weekend)
# print(totaldays)


 







# days.add("Thursday")
# print(days)
# print(months)
 
# days.update(months)
# print(days)
 

# days.update(["April", "May"])
# print(days)


#DELETE SETS
# days.remove("Monday")
# print(days)
# months.discard("May")
# print(months)
# print(months)
# del months
# print(months)


# day2=days.copy()
# print(day2)
# day3=days
# print(day3)

# LOOP
# for day in days:
#     print(day)

#SET UNION AND INTERSECTION

#UNION
# days.update(months)
# dayMmonth=days.union(months)
# weekend=["Friday","Saturday", "Sunday"]
# day2=days.union(weekend)
# print(dayMmonth)
# # print(days)
# print(day2)

# INTERSECTION
# women= {"shoes", "bags", "necklace", "skirt", "blouse"}
# men = {"shirt", "pants", "shoes","tie"}


# similar= women.intersection(men)
# # print(similar)

# print(women)
# women.intersection_update(men)
# print("Women now contains: ",women)




#DIFFERENCE - 
# print("Women:", women)
# print("Men:", men)
# womenItems=women.difference(men)
# print(womenItems)

#difference_update
# print(women)
# women.difference_update(men)
# print(women)

# print("*"*50)


#symmetric_difference
# diffMerge=women.symmetric_difference(men)
# print(diffMerge)

# print(women)
# women.symmetric_difference_update(men)
# print(women)










# AVAILABILITY

# num1= {1,2,45,76,8,99}
# num2={2,8,1}
# num3={10,20,30}
# num4=[45,76,99]

# print("num1: ",num1)
# print("num2: ",num2)
# print("num3: ",num3)
# print("num4: ",num4)

# print("*"*30)
#ISDISJOINT
# print(num2.isdisjoint(num3))

#ISSUBSET
# print("Num2 is a subset of num1 : ",num2.issubset(num1))

#ISSUPERSET
# print("Num1 is a superset of num2", num1.issuperset(num2))

#COPY
# men2=men.copy()
# men3=men
# print(men2)
# print("Men", men3)

# LOOP
# print(women)
# print()
# print("Women Items".upper().center(30,"*"))
# i=1
# for item in women:
#     print("{0}. {1}".format(i,item))
#     i+=1


# SET DELETION-
# days= set(["Monday","Tuesday","Wednesday"])
# months={'January', 'February', 'March'}
# remove(), 
# print(days)
# days.remove("Monday")
# print(days)

# discard(), 
# days.discard("Tuesday")
# print(days)
# pop(), 
# print(months)
# months.pop()
# print(months)
# months.pop()
# print(months)

# clear()
# print("The Months:",months)
# months.clear()
# print("The Months:",months)

 







# print("1: ISDISJOINT: num2 and num1 as no item in common: ",num2.isdisjoint(num3))
# print("3: ISSUBSET: num1 inside num2: ",num2.issubset(num1))
# print("2: ISSUPERSET: num1 inside num2: ",num2.issuperset(num1)) 
# print("4: ISDISJOINT MIXED: num2 and num4(list) as no item in common: ",num2.isdisjoint(num4))


# DIFFERENCE
# print("Men:\t",men)
# print("women:\t",women)
# print('*'*50)
# stuff=men.difference(women)
# stuff2=men.symmetric_difference(women)
# print("Men", men)
# men.symmetric_difference_update(women)
# print("Men after symmetric difference update", men)
# print("Different: \t",stuff)
# print("Symetric Diff: \t",stuff2)
# import calendar
# print(calendar.month(2020,10))

# names={('name','school'),('Boyles','DONRS')}
# names.add("Record")
# info={("Shirt", "Pants"),("Bag","Necklace"),"Fashion",30.2,True}
# print(info) 
 