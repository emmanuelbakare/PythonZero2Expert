'''
e.g. 
    items=[23,25,37,77,93]
    keySearch=25

1. The array in binary search must be sorted for it to work
2. The first Item in the list (@ index 0) is regarded as low value e.g. 0
3. the last item in the list  ( @ len(items)-1) is regarded as high value e.g 4
4. the mid value is calculated  mid=(low+high)/2 e.g. mid=(0+4)/2=
5. If the mid value (items[2]=37) is same as the keySearch then we found our number
5. If mid value is less than keySearch (e.g. 37 < 25), 
    a. then we search the lower half of items
    b. high = mid-1   -- he high value is changed the low value is not
6. If mid value is greater than keySearch (e.g. 37 >25) 
    a. then we search the upper half of items
    b. low=mid+1    -- low value is changed but high is not changed
7. If the low and high cross each other during search (ie. low >high) the keySearch is not found

'''



def binarySearchLinear(mylist,keySearch):
    low=0
    high=(len(mylist)-1)
    
    while low  <=  high:
        mid=(low+high)//2
        if keySearch==mylist[mid]:
            return True
        elif keySearch < mylist[mid]:
            high=mid-1
        else:
            low=mid+1
    return False
            
items=[23,25,37,77,93]
keySearch=77
print(binarySearchLinear(items,keySearch))        

 


# Recursive search 
