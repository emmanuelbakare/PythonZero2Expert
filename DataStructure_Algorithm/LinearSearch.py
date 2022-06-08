#Linear Searches a list one after the other

def linearSearch(mylist,key):
    position=0
    flag=False
    
    while position < len(mylist) and not flag:
        if mylist[position]==key:
            flag=True
        else:
            position +=1
    return flag
            
li=[34,45,15,7,67,54,22,54]        
print(linearSearch(li, 54))
            