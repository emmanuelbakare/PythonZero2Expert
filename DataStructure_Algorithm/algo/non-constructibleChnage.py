

def nonConstructibleChange(coins):
    
    coins.sort()
    
    currentChangeCreated=0
    for coin in coins:
        if coin > currentChangeCreated+1:
            
            return currentChangeCreated+1
        currentChangeCreated+=coin
        
    return currentChangeCreated+1


test1=[1,1,3,5]
test2=[5,7,1,1,2,3,22]
test3= [1, 5, 1, 1, 1, 10, 15, 20, 100]
result=nonConstructibleChange(test3)
print(result) 