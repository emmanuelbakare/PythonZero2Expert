
from datetime import datetime, timedelta,date

# print(dir(datetime)) 
# print('Today:',datetime.today())
# print('Today:',datetime.utcnow())
# print('Today:',datetime.now())  
# print('*'*50)
# print(help(datetime.utcnow))
# print(dir(timedelta))

# year=int(input('Enter the year you were born: '))
# month=int(input('Enter the month '))
# day=int(input('Enter the day  '))

# dob=date(year, month,day)
# today=date.today()
# daysUsed=today-dob
# print(f'Number of days lived {daysUsed} You are {daysUsed//365} years old')


dt1=datetime(year=2022, month=10, day=21)
print(dt1)


dt2=datetime(year=2022, month=5, day=7)
print(dt2)

diff=dt1 - dt2 
print(type(diff))
print(diff)