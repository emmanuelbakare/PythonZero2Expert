import collections
def groupAnagram(strs:list[str]):
    if not strs:
        return []
    
    result = collections.defaultdict(list)
    
    for word in strs:
        s=tuple(sorted(word))
        print(s,word)
        result[s].append(word)
    
    return result




strlst=['eat','tea','tan','ate','nat','bat']
s=tuple(sorted(strlst[0]))
ll= collections.defaultdict(list)
ll[s].append(('eat'))
ll[s].append(('tea'))
ll[s].append(('tan'))
print(ll)
print('*'*20)

result=groupAnagram(strlst)
print(result)
print('*'*20)
print(result.values())