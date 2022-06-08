# DICTIONARY
# Dictionary are iterables i.e. sequence of values stored inside a curly brace
# They are stored using  key, value pair format.  e.g { key:value }
# Unlike Tuple and List that hold a single value in every item, dictionary items has a key 
# describing what the value is meant for. The key is like a description of the value
d1={'name':'Emmanuel', 'age':12}
# Dictionary items are ordered,  changeable and the keys does not allow duplicates
# dictionary is 

# Declare Diction - Two ways
d2=dict()
d3={}


 






# Sample dictionary
records={'name':'Emmanuel', 'age':33,'job':'programmer'}

cars= [
    {
        "brand":"Toyota",
        "Model":"Camry",
        "Year": 2020
    },
    {
        "brand":"Toyota",
        "Model":"Highlander",
        "Year": 2015
    },
    {
        "brand":"Ford",
        "Model":"Explorer",
        "Year": 2021
    },
    {
        "brand":"Honda",
        "Model":"Accord",
        "Year": 2020
    },
    
]

cars2= [
    {
        "brand":"Toyota",
        "model":"Camry",
        "Year": 2020
    },
    {
        "brand":"Toyota",
        "model":"Highlander",
        "year": 2015
    },
    {
        "brand":"Ford",
        "model":"Explorer",
        "year": 2021
    },
    {
        "brand":"Honda",
        "model":"Accord",
        "year": 2020
    }, 
    
]
test=[{'age':34},{'age':13},{'age':77}]
# nested dictionary with different datatype
Person={
    'name':'Mandy Mcclurkins',
    'age':45,
    'result':{
        
        'subjects':['Maths','English'],
        'marks':[89, 85],
    }, 
    'qualification':{
        'university':'Bsc',
        'professional':['PMP','Python'],
        'year':{
            'from': '2000',
            'to': '2005'
        }
        
    }
       
}


#Accessing  Dictionary items
records={'name':'Emmanuel', 'age':33,'job':'programmer'}
# print(Person['result']['subjects'])
# print(Person['qualification']['professional'][0])

#dict.get(item) Method
# result=Person.get('result').get('subjects')
# print(result)


#Dict.keys() – Returns a list of all keys in the dictionary

# result=Person['qualification'].keys()
# print(result)

#Loop Through a Dictionary
# for item in Person.keys():
#     print(item)

#Dict.values() – Returns a list of all values in the dictionary
# print(records.values())

# for item in records.values():
#     print(item)


# Dict.items() – return a list of all the items in a dictionary 
# grouped in a tuple
records={'name':'Emmanuel', 'age':33,'job':'programmer'}

# result=records
# print(result)
# print(result.items())

# for key, value in records.items():
#     print(f'{key} is {value}')
 
 
# result=records.setdefault('aged','Age Doesnt Exist')
# print(result)

#Change Dictionary Item Dictionary
# print(records['name'])
# records['name']= 'Bryan'
# print(records['name'])



# dict.update(dict) - add a new key:value to a dictionary
# rec1={}
# rec1.update({'firstname':'Matthew'})
# rec1.update({'lastname':'Emmanuel'})
# rec1.update({'age':33})
# print(rec1)

# records={'name':'Emmanuel', 'age':33,'job':'programmer'}
# rec2=records
# # print(rec2)

# rec2['name']='James'
# print('rec2:',rec2)
# print('records:',records)

# print('*'*60)
# rec3=records.copy()
# print(rec3)
# print(records)
# rec3['name']="Andrew"

# print('*'*60)
# print('rec3',rec3)
# print('records',records)

#dict.fromkeys(iterable,values) – this creates new dictionary from an iterable
# headers=['name','age','job']

# rec=dict.fromkeys("Man")
# print(rec)

records={'name':'Emmanuel', 'age':33,'job':'programmer'}

# records.clear()
# print(records)


# Dict.popitem() –removes the last inserted item in the dict
# records.popitem()
# records.popitem()
# records.popitem()
# print(records)


# Dict.pop(item, defaultVal) – Remove specified item from the dict
# rem=records.pop('ages')
# print(records)
# print(rem)












  