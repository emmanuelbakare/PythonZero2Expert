
def anagram(word1,word2):
    word1=''.join(sorted(word1.lower())).strip()
    word2=''.join(sorted(word2.lower())).strip()
    if word1==word2:
        return True
    return False

def anagram2(word1,word2,count={}):
    word1=word1.replace(' ','').lower() 
    word2=word2.replace(' ','').lower()
    
    if len(word1) !=len(word2):
        return False
    # count={}
    
    for letter in word1:
        if letter in count:
            count[letter] +=1
        else:
            count[letter]=1
            
    for letter in word2:
        if letter in count:
            count[letter] -=1
        else:
            count[letter]=1
    print(count)
    for i in count:
        if count[i]!=0:
            return False
    return True
            
        
    
     
        

w1="clint eastwood"
w2="old west action"
count={}
w3="public relations"
w4="crap built on lies"
print(anagram2(w3,w1,count))

# some="Subscribe to my channel"

# k=''.join(sorted(w1.lower())).strip()
# l=''.join(sorted(w2.lower())).strip()
# print(k,len(k))
# print(l, len(l))
# print(anagram(w1,w2)) 