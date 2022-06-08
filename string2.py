# STRING OPERATORS
# +,*, [], [:], in, not In, r''

# + Operator
# firstname="Andrew"
# lastname="Martins"

# name=firstname +" "+ lastname

# print(name)

# * OPERATOR
# print("="*40)

# in OPERATOR
# info="Subscribe to this channel and get a gift"

# print("dollar" not in info)

# [] OPERATOR


# greet="Hello World"
# print(greet[4])

# Slice Operator [startIndex:endIndex:step]
# print(greet[3:])









# ESCAPE , SPECIAL CHARACTERS
# \ =escape
# \n = new feed
# \r = carriage return
# \t = tab

# print("Hello \t\tWorld")


#String Output Formating

# name="Joan"
# age=45
# # print(name, age)
# print("my name is {0} and I am {1}  {0}years old".format(age,name))









# STRING METHODS
# str="WELCOME to learning Python - Your best programing tutorial"

# print(str)
# print("="*35)

# print(str.lower())
# print("="*35)

# print(str.upper())
# print("="*35)

# print(str.capitalize())
# print("="*35)
 
# print(str.swapcase())
# print("="*35)

# print(str.title())
# print("="*35)

# FINDING AND COUNTING STRINGS
# str="WELCOME to learning Python - Your best programing tutorial"
# print(str)
# print("="*35)

# print(len(str))
# print("="*35)

# print(str.count('to'))
# print("="*35)

# print(str.endswith('python'))
# print("="*35)

# print(str.startswith('WELCOME'))
# print("="*35)

# print(str.find('to'))
# print("="*35)

# print(str.rfind('to'))
# print("="*35)


# print(str.index('top'))
# print("="*35)

# print(str.rindex('to'))
# print("="*35)

# CHECK THE STRING CONTENT TYPE
# str="wordDds1232---"
# print(str)
# print("="*35)

# print(str.isupper())
# print("="*35) 

# print(str.islower())
# print("="*35)

# print(str.isdigit())
# print("="*35)

# print(str.isalnum())
# print("="*35)

# print(str.isalpha())
# print("="*35)

# print(str.isascii())
# print("="*35)

# JUSTIFY STRING METHODS
# str="Welcome to Python"
# print(str)
# print("*"*35)

# print(str.center(30))
# print("*"*35)

# print(str.center(40,"="))
# print("*"*35)

# print(str.ljust(40,"*"))
# print("*"*35)

# print(str.rjust(40,"*"))
# print("*"*35)

# STRIPPING OUT SPACE

# str1="   Python is Good   "  
# str2="-   you bet" 
# print(str1.rstrip()+str2) 
 

#SPLIT STRING
# str1="Welcome To Python"
# str2="James**John**Michael**Joan"
# str3="James.John.Michael.Joan"
# # print(str3.split("."))
# print(str2.rsplit("**",2))


# str="This is the language of the future"

# print(str.rpartition('the'))


str='''this is a text broken into
different lines. It is been used as a
program example in the best Python tutorial 
on YouTube
'''

# print(str.splitlines())

# print("Can I break this\
#  line into two")







# STRING FORMAT
name="Emmanuel"
age=22
weight=68.04 #150lbs

print("My name is %s  and I am %d years old and i weigh %f" %(name, age,weight)) 


 








 






