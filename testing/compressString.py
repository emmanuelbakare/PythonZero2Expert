# make AAAABBBBBBCC to be A4B6C2
# AAAaa will return A3a2



# def stringCompress(str1):
    
#     prevChar=''
#     total=0
#     compChar=""
#     prevChar=currChar=str1[0]
#     for item in range(len(str1)-1):
#         if str1[item]==str1[item+1]:
#             total +=1
#         else:
#             if total!=0:
#                 compChar+=str1[item]+str(total+1)
#                 total=0
    

#     return compChar   


def stringCompress(str1):
    
    total=0
    compChar=""
    prevChar=str1[0]
    for currChar in str1[1:]:
       
        if prevChar==currChar:
            total +=1
        else:
            # print( f'{prevChar} == {currChar}? {prevChar==currChar}')
            compChar+=prevChar+str(total+1)
            total=0
            prevChar=currChar
    compChar+=prevChar+str(total+1)
    
    

    return compChar   


str1="AAAABBBBBBCC" 
print(stringCompress(str1))       
        
        

