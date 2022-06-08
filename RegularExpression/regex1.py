import re



#SPECIAL CHARACTERS
# EXAMPLE 1  Using . - Period
# ================================
# string='go and do good to all the gods'
# pattern=r'....'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)


# EXAMPLE 2  Using ^ - Caret - string start with 
# ================================

# string='go and do good to all the gods'
# pattern=r'^go'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)

#EXAMPLE 3 Using $ dollar  -string end with
# ================================
# string='go and do good to all the gods'
# pattern=r'gods$'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)

#EXAMPLE 4 Using * asteriks  -0 or more occurence
# ================================
# string='go and do good to all the gods'
# pattern=r'go*d'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)

#EXAMPLE 5 Using + Plus- 1 or more occurrence of a string
# ================================
# string='go and do good to all the gods'
# pattern=r'go+'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)

#EXAMPLE 6 Using ?	- 0 or one occurrence(optional string)
# ================================
# string='go and do good to all the gods'
# pattern=r'goo?'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)

#EXAMPLE 7 Using {min,max} –min or up to max
# ================================
# string='go and do good to all the gods'
# pattern=r'go{1}'
# matches=re.finditer(pattern,string)
 
# for match in matches:
#     print(f'{match.span()}=>{string[match.start():]}')
    
#EXAMPLE 8 Using |	-	 regex OR operator 
# ================================
# string='go and do good to all the gods'
# pattern=r'do|all'
# matches=re.finditer(pattern,string)
 
# for match in matches:
#     print(f'{match.span()}=>{string[match.start():]}')
    

    

#EXAMPLE 9 Using ()	- Group- used to group patterns  
# ================================
# A
# string="abcd"
# pattern='(a(b)c)d'
# match=re.match(pattern,string )
# print('Group 0:',match.group()) #group 0 
# print('Group 1:',match.group(1)) #group 1 
# print('Group 2:',match.group(2)) #group 2 


#B

# with open('headertext.txt') as file:
#     string=file.read()
# pattern=r'(.*)[:](.*)'
# matches=re.finditer(pattern,string)

# for match in matches:
#     # print(match.group(1),"=>",match.group(2))
#     print(match)
# string='gerald, go and do good to all the gods '
# pattern=r'g(o|eral)d'
# matches=re.finditer(pattern,string)
 
# for match in matches:
#     print(f'{match.span()}=>{string[match.start():]}')

# OPEN A FILE TO SEARCH
# with open('file2.txt') as file:
#     string=file.read()
    
#EXAMPLE 10 Using \	- Used to escape special characters.  
# ================================
# string="dont delay. the story."
# pattern=r'...\.'
# matches=re.finditer(pattern,string)
# for match in matches:print(match)



#EXAMPLE 11 Using []	- item in string matches any item inside [].  
# ================================
# pattern=r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d'  or
# pattern=r'...\....\....\.' 
# pattern=r'\d{3}[.-]\d{3}[.-]\d{4}'  
# pattern=r'[89]00'
# pattern=r'[89][0][0-9]'
# pattern=r'[12][0-9][0-9]\.[0-9]+\.[0-9]+\.[0-9]+'
# pattern=r'[12][0-9][0-9](\.[0-9]+){3}'
# pattern=r'(\.?[0-9]+){4}'
# pattern=r'[^89][0-9][0-9](\.[0-9]+){3}'
# pattern=r'Mr\.?\s\w+' 
# pattern=r'Mr[.,]?\s\w+' 
# pattern=r'M(r|s|rs)[.,]\s\w+'

#Email
# pattern=r'[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# url 
# pattern= r'(https?://)?(www.)?([a-zA-Z0-9_-]+\.[a-zA-Z-.]+)'

# matches=re.finditer(pattern,string)
# for match in matches:print(match)

#TEST

#EXAMPLE 12 Match
# ================================
# string="infootball is a great foo way to stop being foolish"
# pattern=r'foo'
# match=re.match(pattern,string)
# if match:
#     print(f'{match.span()} =>{string[match.start():]}')
# else:
#     print('no result')


#EXAMPLE 13 -GROUP NAME
#=========================
with open('headtext.txt') as file:
    string=file.read()
pattern=re.compile(r'(.*)[:](.*)')
pattern=re.compile(r'(?P<keys>.*)[:](?P<value>.*)')
pattern=r'(?P<keys>.*)[:](?P<value>.*)'
matches=re.finditer(pattern,string)
# matches=pattern.finditer(string)  

for match in matches:
    print(match.group('keys'),"=>",match.group('value'))
    # print(match.group(1),"=>",match.group(2))  


#EXAMPLE 14 LOOKAHEAD ASSERTION
# =============================

# with open('filepaths.txt') as file:
#     string=file.read()
 
# pattern=r'.*[.].*'
# pattern=r'.*[.](?!bat$).*'
# pattern=r'.*[.](?!bat$)[^.]*$'


# pattern=r'.*[.](?!bat$).*'  #wont work without re.M
# pattern=re.compile(r'.*[.](?!bat$).*', re.M)
# pattern=re.compile(r'.*[.](?!bat$)\w*', re.M)
# pattern=re.compile(r'.*[.](?!bat$|py$).*', re.M)


# matches=re.finditer(pattern,string)
# num=0
# for num,match in enumerate(matches,1):
#     print(f'{num}: {match.span()} =>{string[match.start():match.end()]}')








