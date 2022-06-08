#=========================Zero division error=====================
# x,y=12,0

# try:
#     z=x/y
# except:
#     print('{}/{} is not possible'.format(x,y))
#     z="==ERROR=="
# else:
#     print("Correct!!")
# finally:
#     print("Division Result ",z) 
    
#======================================================    
# Exception name and multiple exception

x,y=12,0
z=0
try:
    z=x/y
except FileExistsError:
    print('{}/{} is not possible'.format(x,y))
    z="==ERROR==" 

print("Division Result ",z) 