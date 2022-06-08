import csv

#EXAMPLE 1 - 
# with open('file2.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     count=0
#     for row in csvfile:
#         if count==0:
#             count+=1
#             print(row)
#             print("*"*30)
#             continue
#         print(row)


#EXAMPLE 1.1 -Better implementation
# with open('file2.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     #get header and print out
#     header=next(csvfile)
#     print(header)
#     print("*"*30)
#     #loop through rows and print out
#     for row in csvfile:
#         print(row)
        
#EXAMPLE 1.2 -PRINT SPECIFIC NUMBER OF RECORDS
# with open('file5.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     header=next(csvfile)
#     print(header)
#     print("*"*30)
#     #loop through rows and print out
#     total=1
#     for row in csvfile:
#         print(row)
#         total+=1
#         if total >5: break
       
        
        
#PRINT ONLY THE FIRST HEADING
# with open('file4.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     headrow=next(csvfile)
#     print(headrow)
     
#PRINT ALL THE CONTENT + THE HEADERS
# with open('file4.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     for row in csvfile:
#         print(row)
        
        
#PRINT ONLY A ROW (SECOND ROW row[1])FROM THE CSV.       
# with open('file5.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     for row in csvfile:
#         print(row[1])
  
#VERTICAL DISPLAY OF KEY AND VALUES        
# with open('file5.csv') as file:
#     csvfile=csv.reader(file, delimiter=',')
#     headrow=next(csvfile)
#     for row in csvfile:
#         for num,values in enumerate(row):    
#             print(f'{headrow[num]}: {values}')
#         print('*'*30)  


#READ CSV USING DICTREADER
# with open('file5.csv') as file:
#     csvfile=csv.DictReader(file)
#     for row in csvfile:
#         print(row)

#VERTICAL READ USING DICTREADER
# with open('file5.csv') as file:
#     csvfile=csv.DictReader(file)
#     for row in csvfile:
#         for key in row:
#             print(f'{key}: {row[key]}')
#         print()

header=['firstname','lastname','age']
rec1=['Deji','Bakare','32']
rec2=['Mandy','Barker','43']
rec3=['Olusegun','Adeniji','69']

# while True:
    
#     firstname=input('First Name: ')
#     lastname=input('Last Name: ')
#     age=input('Age: ')
#     allrec=firstname.strip()+lastname.strip()+age.strip()
#     if allrec=='':break 
#     record=[firstname,lastname,age]
#     print(record)
#     print(len(record))
#     print()
header=['firstname','lastname','age']
# with open('rec1.csv', 'wb') as newcsv:
with open('rec1.csv', 'a',newline='', encoding='utf-8') as newcsv:
    csvwriter=csv.writer(newcsv)
    csvwriter.writerow(header) 
    while True:
        firstname=input('First Name: ')
        lastname=input('Last Name: ')
        age=input('Age: ')
        allrec=firstname.strip()+lastname.strip()+age.strip()
        if allrec=='': break
        record=[firstname,lastname,age]
        csvwriter.writerow(record)
        print()
        
    
         
 

# with open('record1.csv') as file:
#     csvfile=csv.reader(file)    
#     for row in csvfile:
#         print(row)