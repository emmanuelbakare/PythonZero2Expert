# Example 1
# fileObj=open('myfile1.txt','r')
# print("OUTPUT OF FILE1")
# print(fileObj.read())
# fileObj.close()

# Example 2

# with open('myfile1.txt','r') as file:
#     print("OUTPUT OF FILE1")
#     print(file.read())
#     print('Is file Closed? ',file.closed)
# print('Is file Closed? ',file.closed)

# with open('myfile1.txt','r') as file:
#     for line in file:
#         print(line)


# with open('file2.txt', 'w+') as file:
#     while True:
#         text=input("Enter Text: ")
#         if not len(text):break
#         file.write('\n')
#         file.write(text)



# with open('myfile1.txt','r') as file:
#     mylist=file.readlines()
# print(mylist)  
  
# with open('myfile1.txt','r') as file:
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print(file.read(50))
#     print("Pointer @: ", file.tell())
#     print(file.read(50))
#     print(file.read(50))
#     print(file.read(50))


# CODE EXAMPLE 
# search for words in myfile1.txt using input from the terminal



# with open('myfile1.txt','r') as file:
#     codeline=0
#     search=""
#     while (search!="exit()"):
#         search=input('Enter your search: ')
#         # if not len(search): break
#         for line in file:
#             codeline+=1
#             if search in line:
#                 print(codeline,line) 
#         file.seek(0)
#         codeline=0



 
     











# #1
# with open('myfile1.txt','r') as file:
#     codeline=0
#     for line in file:
#         codeline+=1
#         print(codeline,line) 

# 2 - make static search through file
# with open('myfile1.txt','r') as file:
#     codeline=0
#     for line in file:
#         if "shine" in line:
#             codeline+=1
#             print(codeline,line)     
 
#3 - get search from keyboard input
# with open('myfile1.txt','r') as file:
#     codeline=0
#     search=input('Enter your search: ')
#     for line in file:
#         if search in line:
#             codeline+=1
#             print(codeline,line)  

#4 - allow for multiple search       
# with open('myfile1.txt','r') as file:
#     codeline=0
#     search=""
#     while (search!="exit()"):
#         search=input("Enter your search: ")
#         if not len(search):break
#         for line in file:
#             if search in line:
#                 codeline+=1
#                 print(codeline,line)
#         file.seek(0)
#         codeline=0
                


#WRITE Operation               
# w,w+,wb,wb+
#overwrite existing file, create a new file if it doesnt exist.
# print('File2.txt Now')
# print('==============')
# with open('file2.txt','w+') as file:
#     file.write("Record on Line 1\n")
#     file.write("Record on Line 2\n")
#     file.write("Record on Line 3\n") 
#     file.write("Record on Line 4\n")
#     file.write("Record on Line 5\n")
#     file.write("Record on Line 6\n")
#     file.seek(0) 
#     print(file.read()) 

 
# print('File2.txt AGAIN')
# print('==============')
# with open('file2.txt','a+') as file:
#     file.write("Side  1\n")
#     file.write("Side  2\n")
#     file.seek(0) 
#     print(file.read())  
 
#Append
#a, a+, ab, ab+

# with open('file22.txt', 'w+') as file:
    
#     while True:
#         text=input(' Enter your text: ')
#         if not len(text): break
#         file.write(text)
#         file.write("\n")
#     print("File22.txt Output")
#     print("==========")
#     file.seek(0)
#     print(file.read())
    




#wb Binary files wb
#Example : Download and image from the internet using requests module and File wb

# import requests

# img=requests.get('https://cdn.britannica.com/67/19367-050-885866B4/Valley-Taurus-Mountains-Turkey.jpg')

# with open('image1.jpg', 'wb') as file:
#     file.write(img.content)

# print(img)



    
    


    


