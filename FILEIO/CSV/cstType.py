import csv

#PRINT OUT ALL DATA
# with open('file5.csv') as file:
#     csvfile=csv.reader(file)
    
     
#     for row in csvfile:
#         print(row)   

#PRINT SPECIFIC ROW DATA
# with open('file5.csv') as file:
#     csvfile=csv.reader(file)
    
     
#     for row in csvfile:
#         print(row[10])   

#PRINT HEADER AND DATA SEPERATELY

# with open('file5.csv') as file:
#     csvfile=csv.reader(file)
#     header=next(csvfile)
#     print(header)
#     print("*"*50)
     
#     for row in csvfile:
#         print(row) 

#PRINT SPECIFIC NUMBER OF RECORD FROM CSV FILE
# with open('file5.csv') as file:
#     csvfile=csv.reader(file)
#     header=next(csvfile)
#     print(header)
#     print("*"*50)
#     total=1
#     for row in csvfile:
#         print(row) 
#         total+=1
#         if total >10:break


#PRINT THE CSV RECORD VERTICALLY
# with open('file5.csv') as file:
#     csvfile=csv.reader(file)
#     header=next(csvfile)
#     for row in csvfile:
#         num=0
#         for value in row:
#             print(f'{header[num]}: {value}')
#             num+=1
#         print() 



#1. USE DictReader TO GET CSV INSIDE A DICTIONARY
# with open('file5.csv', 'r') as file:
#     csvfile=csv.DictReader(file)
#     for row in csvfile:
#         print(row)
        
#1. USE DictReader TO PRINT RECORD VERTICALLY
# with open('file5.csv', 'r') as file:
#     csvfile=csv.DictReader(file)
#     for row in csvfile:
#         for key in row:
#             print(f'{key}: {row[key]}')
#         print()


#2. USE DictReader TO PRINT RECORD VERTICALLY
with open('file5.csv', 'r') as file:
    csvfile=csv.DictReader(file)
    for row in csvfile:
        for key,val in row.items():
            print(f'{key}: {val}')
        print()



#WRITE DATA
header=['firstname', 'lastname', 'age']  
rec1=['Deji','Bakare','32']
rec2=['Mandy','Barker','43']
  
with open('rec1.csv','w',newline='', encoding='utf-8') as newcsv:
    csvwriter=csv.writer(newcsv)
    csvwriter.writerow(header)
    csvwriter.writerow(rec1)
    csvwriter.writerow(rec2)




#WRITE DATA
# header=['firstname', 'lastname', 'age']  
# rec1=['Deji','Bakare','32']
# rec2=['Mandy','Barker','43']
# rec3=['Olusegun','Adeniji','69']  
  
# with open('rec1.csv','w',newline='', encoding='utf-8') as newcsv:
#     csvwriter=csv.writer(newcsv)
#     csvwriter.writerow(header)
    
#     while True:
#         firstname=input('First Name: ')
#         lastname=input('Last Name: ')
#         age=input('Age: ')
#         allrec=firstname.strip()+lastname.strip()+age.strip()
#         if allrec=='':break
#         record=[firstname, lastname,age]
#         csvwriter.writerow(record)
#         print()





# tbody=''
# thead=''
# with open('file5.csv','r') as file:
#     csvfile=csv.DictReader(file)
#     for row in csvfile:
#         tbody+=f'<td>'