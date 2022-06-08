
p1="[{()}]"

def balance_check(str1):
    
    if len(str1)==0:
        return False
    
    opening=set('[{(')
    matches = set([("[","]"),("{","}"),("(",")")])
    stack=[]
    for paren in str1:
        if paren in opening:
            stack.append(paren)
            print(f'{paren},Stack: {stack}')
        else:
            if len(stack)==0:
                return False
            last_open=stack.pop()
            print(last_open,paren) 
            if  (last_open,paren) not in matches:
                  return False
    return len(stack)==0



def balance_check2(str1):
    count=0
    matches=(('(',')'),('[',']'),('{','}'))
    lst=list(str1) if str1 is not list else str1
    if len(lst)%2!=0:
        return False
    
    if len(lst)==0:
        return True
    front=lst.pop(0)
    rear=lst.pop()
    if (front,rear) in matches:
        return balance_check2(lst)
    else:
        return False    
    
    
p1="[({[{()}]})]"
p1="[]"
# p1=['[', '{', '(', ')', '}', ']']
result=balance_check2(p1)
print(result)


# lst1=list(p1) if p1 is not list else p1
# print(lst1)

matches=(('(',')'),('[',']'),('{','}'))
 