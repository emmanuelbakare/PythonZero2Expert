# Standard output 
# print("The Best Python Tutorial online")

# # Standard input 
# yourguess = input("Take a guess: ")
# print("you guessed ", yourguess)

#Example 1: Simple Read
 

# Exampe 2-  using With keyword 
# with open('myfile1.txt','rt') as fileObj:
#     print(fileObj.read())
#=================================================
# Example 2.2 in With the file object closes outside the open block                     
# with open('myfile1.txt','r') as file:
#     cont=file.read()
#     print(cont)
#     print("Total Lenght",len(cont))
#     print('Closed inside open:',file.closed)  
# print("Total Lenght",len(cont))
# print('Closed Outside open:',file.closed)  
#=================================================
# Example 3 - read each line
# with open('myfile2.txt','r') as file:
#     codeline=0
#     for line in file:
#         codeline+=1
#         print("line:",codeline)
#         print(line)
#=================================================
# Example 3.2 - remove extra paragrah
# with open('myfile1.txt','r') as fileObj:
#     parag=0
#     for line in fileObj:
#         if len(line) >2: 
#             parag+=1
#             print("Paragraph:",parag)
#             print(line)
#=================================================
# Example 4 - Search command line
with open('myfile1.txt','r') as file:
    codeline=0
    search=""
    while True:
        search=input("Enter Your Search: ")
        if not len(search):break
        for line in file:
            if len(line) >2: 
                codeline+=1
                if search in line:
                    print("Line No:",codeline)
                    print(line)
        file.seek(0)
        codeline=0  

# str="This is a sample code line that we are printing/n"
# print(len(str))




#=================================================
#Seek, tell, 
  


# with open('myfile2.txt') as file:
    # file.read()
    # print("Pointer @",file.tell())    
    # print(file.seek(50))
    # print("Pointer @",file.tell())
    # content1=file.readline()
    # print("Pointer @",file.tell())
    # content2=file.readline()
    # print("Pointer @",file.tell())
    # file.seek(0)
    # print(file.read())
#=================================================
# Readline and Seek position
# with open('myfile2.txt') as file:
#     put=file.readlines()
# for p in put:print(p.strip('\n'))        
 
#=================================================
# WRITE TO A NEW FILE WITH 'w' 
# with open('file4.txt','w+') as file:
#     file.write('Record on line 11\n')
#     file.write('Record on line 21\n')



# with open('file4.txt','w') as file:
#     file.write('Record on line 3 \n')
#     file.write('Record on line 4 \n') 

#=================================================
# READ/ WRITE TO A FILE WITH 'w+'
# with open('file4.txt','w+') as file:
#     file.write('Record on line 111\n')
#     file.write('Record on line 211\n')
#     file.seek(0)
#     print(file.read()) 

# READ/ WRITE TO A FILE WITH 'r+ 
# with open('file4.txt','r+') as file:
#     file.write('Record on line 10\n')
#     file.write('Record on line 20\n') 
#     file.seek(0)
#     print(file.read())


 #=================================================
# Append to File with 'a' and 'a+'
 
# with open('myfile2.txt','a') as file:
#     print("Last Line:",file.tell())  # check current line - last
#     file.write("Write Something on the last line\n")
#     file.seek(0)    #go to the first line
#     print("First Line:",file.tell())  #print current line - first
#     file.write("SHOULD BE FIRST line\n")  # writes on last line again 'a' always write on last line
    









# with open('myfile2.txt','w+') as file:
#     flist=file.readlines()
#     # print(flist)
#     flist.insert(1, '***A good Christmas Song***\n')  
#     file.write("".join(flist))  
#     file.seek(0)
#     print(file.tell()) 
#     print(file.read()) 
# print("NEW Lyrics".center(40,"*"))
# print("".join(flist))    
 
     
 
     
      
 

 

    
    


                    


                
                    





# with open('myfile1.txt','r') as file:
#     codeline=0
#     search=input('Enter Search: ')
#     for line in file:
#         if len(line) >1: 
#             codeline+=1
#             if search in line:
#                 print("Line No:",codeline)
#                 print(line)