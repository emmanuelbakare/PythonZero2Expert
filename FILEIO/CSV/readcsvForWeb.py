import csv, webbrowser

tbody,thead='','' 

#table Generation
with open('file5.csv') as file: 
    csvfile=csv.DictReader(file)
    #Table Body Generation
    for row in csvfile:
        tbody+='<tbody>\n'
        tbody+='\t<tr>\n'
        for td in row:
            tbody+=f'\t\t<td>{row[td]}</td>\r'
        tbody+='</tr>\n'
        tbody+='</tbody>\n'
        
    #Table Header Generation
    thead+='<thead>\n'
    thead+='\t<tr>\n'
    for th in row.keys():
        thead+=f'\t\t<th scope="col">{th}</th>\r'
    thead+='\t<tr>\n'
    thead+='\t<thead>\n'
        
bootstrap='<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">'
title="Our CSV Example"

table=f'''
<table class='table'>
    {thead}
    {tbody}
</table>
'''

html=f'''
<html>
    <head>
        <title>  {title} </title>
        {bootstrap}
    </head>
    <body>
       <div class='container'> 
        <h2> {title} </h2> 
            {table} 
       </div>
    </body>
    
<html 
'''

with open('readcsv.html', 'w') as webfile:
    webfile.write(html)
# webbrowser.open('readcsv.html')  