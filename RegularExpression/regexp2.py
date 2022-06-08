import re 

#findall
#finditer
#search
#match 
# string="good Everthing good comes in another come go come"
# pattern=r'go'
# myMatch=re.match(pattern, string)

# print (myMatch)


# print(re.match(r'go','go and do good'))

# for match in re.finditer(r'go','go and do good'):
#     print(match)
    


# ., ^ *,$, +,? {min,max},|, (), [] \

# string='go and do good to go all the good gods'
with open('file2.txt') as file:
    string=file.read()
# pattern=r'\d'    #[0-9]
# pattern=r'\D'    #[^0-9]
# pattern=r'\w'    #[a-zA-Z0-9]
# pattern=r'\s'    #[\t \n\r\f\v] 
# pattern=r'sample'     #  
# pattern=r'...\....\....\..'     #  
# pattern=r'\d\d\d\.\d\d\.\d\d\d\.'     #  
# pattern=r'(\d{1,3}\.){3}(\d{1,3})'     # Ip address Regex 
# pattern=r'(\d{1,3}\.){3}(\d{1,3})'     # Ip address Regex 
# pattern=r'([0-9]+\.){3}([0-9]+)'      # Ip address Regex 
# pattern=r'[89][0-9][0-9]' #800-899 or 900-999
# pattern=r'[^89][0-9]{2}\.([0-9]+\.){2}[0-9]+'  #100-199 -200-299 (100-299)
# pattern= r'M(r|rs)[,.]?\s(\w+)' 
# # pattern= r'[a-zA-Z0-9_+.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
# # pattern=r'(https?://)?(www.)?[a-zA-Z0-9-.]+\.[a-zA-Z0-9-]+'
# pattern=r'(https?://)?(www.)?([a-zA-Z0-9-.]+\.[a-zA-Z-]+)'
# matches=re.finditer(pattern,string)


# for match in matches:
#     print(match.group())  

# with open('headtext.txt') as file:
#     string=file.read()
    
# pattern=r'(?P<key>.+)[:](?P<value>.+)'
# matches=re.finditer(pattern,string)
# #(?P<name_of_group>regex)
# for match in matches:
#     print(match.group('value'))

# string="abcd"
# pattern=r'(a(b)c)d'
# match=re.match(pattern,string)
# print('GROUP 0:', match.group(0))
# print('GROUP 1:', match.group(1))
# print('GROUP 2:', match.group(2))


with open('filepaths.txt') as file:
    string=file.read()
# (?=regex)
#(?!regext)
# pattern=re.compile(r'.*[.](?!bat$).*',re.M)
# # pattern=r'.*[.](?!bat$).*'

# matches=re.finditer(pattern,string)

# for match in matches:
#     print(match.group())

#split
string="Good, come on Tuesday, Tuesday, Tuesday"
pattern=r'Tuesday'
replace="Monday"
match=re.subn(pattern,replace,string)
print(match)

#sub