
#BINARY GAP

from decimal import ConversionSyntax


def bingap(num):
   
    
    binum=bin(num).replace('0b','')
    count=0  
    binstore=[] 
    for num in range(len(binum)):
        if binum[num]=='1':
            binstore.append(count)
            count=0
        else:
            count+=1
    return max(binstore)

lst=[1,2,5]
lst2=[5,7,1,1,2,3,22]
def nonConstructibleChange(coins):
    coins.sort()
    print(coins)
    container=0
    for coin in coins:
        if coin > container+1:
            return container +1
        container +=coin
            
    
    return 1

# print(nonConstructibleChange(lst2))


data1={'val1':23,'val2':4,'val3':29}
print(max(data1.values()))