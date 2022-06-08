import csv, webbrowser
title='custom Title'
table='''
<table class='table'>
    <thead>
        <tr>
            <th scope="col"> head1 </th>
            <th scope="col"> head2 </th>
        </tr>
    </thead>
    
    
    <tbody>
        <tr>
            <td> row 1 col 1</td>
            <td>  row 1 col 2</td>
        </tr>
        <tr>
            <td> row 2 col 1</td>
            <td>  row 2 col 2</td>
        </tr>
    </tbody>

</table>
''' 
content=f'''
<div class='container'>
    <h1>HTML testing </h1>
    {table}
</div>

    
'''



bootstrap='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
html=f'''
<html>
    <header>
        <title> {title}</title>
        {bootstrap}
    </header>
    <body>
        {content}
    </body>
</html>
'''



with open('testweb.html','w') as webfile:
    webfile.write(html)

filename=""
webbrowser.open_new_tab('testweb.html') 

print(html) 







 
# with open('file2.csv') as file:
#     csvread=csv.reader(file,delimiter=',')
#     count=0
#     headerfound=0
#     for row in csvread:
#         if count==0:
#             print('HEADER START'.center(30,"*"))
#             print(row)
#             count +=1
#             headerfound=1
#             print('HEADER ENDS'.center(30,"*"))
#             continue
#         print(row)
#         count +=1
#     print(f'Total Rows: {count-headerfound}')