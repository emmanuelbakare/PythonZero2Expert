

# with open('file5.csv','r') as file:
#     csvfile=csv.DictReader(file, delimiter=',')

#     for row in csvfile:
#         print(row)

# with open('file5.csv','r') as file:
#     csvfile=csv.DictReader(file, delimiter=',')

#     for row in csvfile:
#         for key, value in row.items():
#             print(f'{key} : {value}')
#         print()


# header=['firstname','lastname','age']
# rec1=["Matthew", "Henry","25"]
# rec2=["Jacob", "Jackson","35"]

# with open('rec1.csv', 'w', newline='', encoding='utf-8') as newcsv:
#     csvwriter=csv.writer(newcsv, delimiter=',')
#     csvwriter.writerow(header)
#     csvwriter.writerow(rec1)
#     csvwriter.writerow(rec2)

# with open('rec2.csv', 'w', newline='', encoding='utf-8') as newcsv:
#     csvwriter=csv.writer(newcsv, delimiter=',')
#     csvwriter.writerow(header)
#     while True:
#         firstname=input("First Name: ")
#         lastname=input("Last Name: ")
#         age=input("Age: ")
#         allrec=firstname.strip()+lastname.strip()+age.strip()
#         if allrec=='':break
#         record=[firstname, lastname, age]
#         csvwriter.writerow(record)
#         print()


import csv
import webbrowser

# boostrap='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
# thead=''
# tbody=''
# with open('file5.csv','r') as file:
#     csvfile=csv.DictReader(file)
    
#     for row in csvfile:
#         print(row)
        
        
import webbrowser
import csv

with open('file3.csv', 'r') as file:
    csvfile=csv.reader(file)
    
    thead=''
    tbody=''
    #CREATE THE HEADER HTML
    header=next(csvfile)
    thead+='\t<thead>\n'
    thead+='\t\t<tr>\n'
    for th in header:
        thead+=f'\t\t\t<th scope="col">{th}</th>\n'
    thead+='\t\t</tr>\n'
    thead+='\t</thead>\n'
    
    #CREATE THE BODY HTML
    tbody+='\t<tbody>\n'
    for row in csvfile:
        tbody+='\t\t<tr>\n'
        for td in row:
            tbody+=f'\t\t\t<td>{td}</td>\n'
        tbody+='\t\t</t>\n'
    
    tbody+='\t</tbody>\n'
    
    table=f'''
    <table class="table">
        {thead}
        {tbody}
    </table>
    '''

bootstrap='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'

title="Our CSV"
html=f'''
    <html>
    <head> 
        <title>{title} </title>
        {bootstrap}
    </head>
    <body>
    <div class='container'>
        <h2>{title}</h2>
        {table}
    </div>
    </body>
    <html>
'''     
with open('csvreader.html', 'w') as webfile:
    webfile.write(html)


webbrowser.open('csvreader.html')    