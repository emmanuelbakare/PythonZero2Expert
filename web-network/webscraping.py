from bs4 import BeautifulSoup

#PRINT LOAD AND PRINT OUT HTML
# with open('sample.html', 'r') as file:
#     webfile=file.read()
    
# soup = BeautifulSoup(webfile,'lxml')
# print(soup.prettify())

# RETRIEVE ONLY A TAG INFORMATION FROM THE HTML
# with open('sample.html', 'r') as file:
#     webfile=file.read()
    
# soup = BeautifulSoup(webfile,'lxml')
# courses=soup.find('h5')  # print first occurent of h5
# courses= soup.find_all('h5')
# # print(courses)  # print all h5 in a list

# #print out the content of the h5
# for course in courses:
#     print(course.text)

#GET INNER TAG - TRANSVERSE THROUGH THE HTML
# with open('sample.html', 'r') as file:
#     webfile=file.read()
    
# soup = BeautifulSoup(webfile,'lxml')
# #get all <div class="card>" in the html
# card_divs=soup.find_all('div', class_='card')

# for course in card_divs:
#     name= course.h5.text
#     price=course.a.text.split()[-1]
#     print(f'{name} costs: {price}') 




#SCRAP LIVE SITE
import urllib.request
import requests
# urlget=urllib.request.urlopen('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=')
html= requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=').text
# html=str(urlget.read()) 

soup = BeautifulSoup(html,'lxml')
# # print(soup.prettify()) 
jobs=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
# print(job) 
for job in jobs:
    company_name=job.find('h3',class_='joblist-comp-name')
    skills= job.find('span', class_='srp-skills')
    print(f'Company Name: {company_name.text.strip().title()}') 
    print(f'Needed Skills:{skills.text.replace(" ","").strip().title()}')
    print("*"*40)
      

