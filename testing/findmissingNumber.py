# PROBLEM
# Consider an Array of Non Negative number. A second array is formed by
# shuffling the element of the first array and and deleting a random
# element. Giving this two arrays, find the element missing in the 
# second array

# e.g.
# lst1=[1,2,3,4,5,6,7]
# lst2=[3,7,2,1,4,6]
# finder(lst1, lst2)
# missing number is 5



        
               

def finder2(lst1,lst2):
    lst1.sort()
    lst2.sort()
    
    for item in range(len(lst1)):
        if lst1[item]!=lst2[item]:
            return lst1[item]      
    # return result

def finder3(lst1,lst2):
    result=0
    lsts=lst1+lst2
    for item in lsts:
        result^=item 
        # print(result)
    return [result,lsts]

lst1=[1,2,3,4,5,5,6,7]
lst2=[3,7,2,1,4,5,6] 
print(finder3(lst1,lst2))
