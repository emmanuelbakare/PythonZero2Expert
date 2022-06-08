# arr=[1,3,6,4,1,2]
# arr2= [-1,-3]

# def solution(arr):
#     arr.sort()
#     total=len(arr)
#     for item in range(1,total):
#         if item not in arr:
#             return item
    
#     return total+1   
        

# print(solution(arr))  
# msg1="Codility we test coders"
# mgs2="Why not"

# def solution(msg,k):
#     msglen=len(msg)
#     currword=""
#     nextword=""
#     if msglen > k:
#         msglist=msg.split(" ")
#         for word in msglist:
#             nextword=len(f'{currword} {word}')
#             if nextword > k:
#                 return currword.strip()
#             else:
#                 currword+=word +' '
                
#         return currword.strip()
#     return msg.strip()            
                
#     return currword.strip()        

# print(solution(mgs2,100))


# def solution(msg,k):
#     wordlen=len(msg)
#     remainder=k-wordlen
#     remword=msg[:remainder]
#     wordcut=msg.split()
#     rcut=remword.split()
#     if wordcut[-1]==rcut[-1]:
#         return wordcut
#     else:
#         return [word+'' for word in rcut]
#     return remword
    
    
# print(solution(msg1,14))

# p=[1,4,1]
# s=[1,5,1]

# p2=[4,4,2,4]
# s2=[5,5,2,5]

# p3=[2,3,4,2]
# s3=[2,5,7,2]

# def solution(people, seats):
#     leftcar=0
#     for item in range(len(people)):
#         if people[item] < seats[item]:
#             leftcar=leftcar +1
#     return leftcar


# print(solution(p,s))
a=[5,19,8,1]
def solution(pol):

    pol2=pol.copy()
    total=sum(pol)
    half=total/2
    nearest=0
    for item in range(len(pol)):
       pol2[item]=pol2[item]/2
       if sum(pol)/2  <
       
        
        
    return pol


print(solution(a))
