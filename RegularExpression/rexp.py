import re
text_to_search='''
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha Haha

MetaCharacters (need to be escaped):
. ^ * + ? { } [ ] \ | ( ) 

coreyms.com

321-555-4321
123.555.1234
123*555*1234
123-555-1234
800-555-4321
900.555.1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mrs Jackson
Mr Bakare
Mr R59328
 
cat
mat
bat


CoreyMSchafer@gmail.com
core.schafer@university.edu
core-321-schager@my-work.net
admission@nsuk.co.uk
admission_msc@nsuk.co.uk
admission+phd@nsuk.co.uk




http://tutorials.com
http://www.lynda.com
https://www.python.org
https://python-code.co.uk 
http://www.maths-teacher.edu


'''

sentence = "Start a sentence and then bring it to an end"
# numbers starting with 800 or 900 followed by 3 digits and another 4 digits with
# '.' or '-' as separators
# pattern=r'\d\d\d[.-]\d\d\d[.-]\d\d\d\d' 
pattern=r'\d{3}[.-]\d{3}[.-]\d{4}'  # as as above
#digits(0-9) min of 3 max of 4. {4} will show only 4 digits.
# pattern=r'[0-9]{3,4}'  
 # every thing that ends with at but not begin with b
# pattern=r'[^b]at'
#Returns Mr or Mr. Search Mr with optional '.' in front
# pattern=r'Mr\.?'
#ret as above wit space (\s) 
# upper case first letter[A-Z]
# 0 or occurrence of order words e.g Mr. Bakare, or Mr T
# pattern=r'Mr\.?\s[A-Z]\w*'
# pattern=r'Mr\.?\'
# 3 lines below produces similar result
pattern=r'M(r|s|rs).?\s\w+'
pattern=r'M(r|s|rs).?\s[A-Z]\w+'
pattern=r'M(r|s|rs).?\s[A-Z]\w*' 
#email
pattern=r'[a-zA-Z0-9_.+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
#url
pattern= r'(https?://)?(www.)?([a-zA-Z0-9_-]+\.[a-zA-Z-.]+)'
pattern=r'(?ba)'
cpattern=re.compile(pattern)
# matches= cpattern.sub(r'\3',text_to_search)
matches=cpattern.finditer(text_to_search) 
 
for match in matches:
    print(match)
    
    
# with open('file1.txt') as file:
#     content=file.read()

# pattern=re.compile(r'\d\d\d.')   
# matches= pattern.finditer(content)
# for match in matches:
#     print(match)