#STRING OPERATORS
# +,*, [], [:], in, not In, r''  


























#STRING METHODS
# methods used to manipulate strings

str1="WELCOME to learning Python - The best tutorial on how to program in Python"

# #===CHANGING STRING CASE====#
# print(str1.capitalize())
# print(str1.lower())
# print(str1.upper())
# print(str1.swapcase())
# print(str1.title())

# #===FINDING AND COUNTING CHARACTERS====#
# print(str1.len(str1))
# print(str1.count('to'))
# print(str1.endswith('PYTHON'))
# print(str1.startswith('Welcome'))
# print(str1.find('to'))
# print(str1.rfind('to'))
# print(str1.index('to'))
# print(str1.rindex('to'))


#===CHECK STRING CONTENT TYPE====#
strtest="thisisPTOROalpha"
# print(strtest.isupper())
# print(strtest.islower())
# print(strtest.isdigit())
# print(strtest.isalnum())
# print(strtest.isalpha())













#===JUSTIFY String====#
str2="Welcome to Python"
# print(str2.center(100))  
# print(str2.center(50,'*'))   
# print(str2.ljust(50,'='))
# print(str2.rjust(50,'='))






 




 
#===STRIPPING OUT SPACES====#
str4="    Python is a Good    "
str5=" Language"
# print(str4+str5)  
# print(str4.strip()+str5)  
# print(str4.lstrip()+str5)  
# print(str4.rstrip()+str5)  



 
 


 

#===SPLIT CHARACTERS====#
str5="Welcome to python "
str6="James**John**Michael**Joan"
str7="James,John,Michael,Joan"

# print(str5.split())
# print(str6.rsplit('**'))
# print(str7.rsplit(','))
# print(str7.rsplit(',',2))






#== Partition Character====
str5="This is the Language of the Future"

# print(str5.partition(' the '))
# print(str5.rpartition(' Language '))






#=====SPLIT STRING INTO LINES======
text= '''this is a text broken into
different lines. It is been used as a
program example in the best Python tutorial 
on YouTube '''

print(text.splitlines())
 
