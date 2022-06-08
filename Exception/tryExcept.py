# TRY/CATCH  try/except
# y=100/0
# try:
#     # y=100/0
#     y=open('file1.txt')
#     z=10
# except (FileNotFoundError, FileExistsError): 
#     print('There is an error')
# else:
#     print('This file exist')
#     print(y.read())
#     y.close()
# finally:
#     print()
#     print('We are done with our try catch: Clean up')

  
 

#exampl 1
# (10/0))


#exampl 2
# with open('file1.txt') as file:
#     doc=file.read() 
#     print(doc)
     

#TRY CATCH
# try:
#     x=12
#     y=100/0
#     z=10
# except:
#     print('There is an error') 

#MULTIPLE EXCEPTION ERROR -EXAMPLE 1
# try:
#     x=12
#     y=100/0
#     with open('sample.txt') as file:file.read()
#     z=10
# except FileExistsError:
#     print('The file is not found')
# except ZeroDivisionError:
#     print('Zero division error here')
# except:
#     print('There is an error') 

#MULTIPLE EXCEPTION ERROR -EXAMPLE 2
# try:
#     x=12
#     y=100/0
#     with open('sample.txt') as file:file.read()
#     z=10
# except (FileExistsError,ZeroDivisionError):
#     print('The file is not found')

# except:
#     print('There is an error') 
    
 

