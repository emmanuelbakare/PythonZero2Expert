

def movezeros(lst:list[int]):
    temp=0
    print('before: ',lst)
    for index,num in enumerate(lst):
        if index < len(lst)-1:
            first=index
            second=index+1
            # print('index::',index)
            print(f'index {index}, first: {lst[first]}, second: {lst[second]}') 
         
        
    return lst    
        # if i==0:
        #     lst[i+1],lst[i]=lst[i],lst[i+1] 
       
             

input=[0,1,0,3,12]

result=movezeros(input)

print('After:',result)