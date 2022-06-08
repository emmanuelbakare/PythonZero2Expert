# def happyNumber(num):
#     sum=0
#     vals=""
#     for i in str(num):
#         vals+=f'{i}(2)+' 
#         sum+=int(i)**2
#     print(f'{vals} = {sum}')
#     if sum==1:
#         return True
#     happyNumber(sum)
def answer(ans):
    if ans:
        return "Yes"
    else:
        return "No"
def happyNumber2(num):
 
    sum=0
    vals=""
    numstr=str(num)
    for count,i in enumerate(numstr,1):
        vals+=f'{i}^2 + ' if count<len(numstr) else f'{i}^2'
        sum+=int(i)**2
    print(f'{vals} = {sum} ')
    if sum==1:
        return answer(True)
    elif sum==0 :
        return answer(False)
    
    return happyNumber2(sum)        

happy=19  

print(f'Is {happy} a Happy number? {happyNumber2(happy)}')

