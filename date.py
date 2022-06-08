
# from datetime import date

# today=date.today() 
# print(today)
# print("YEAR:", today.year)
# print("MONTH:", today.month)
# print("DAY:", today.day)

# print(dir(date))
# print("*"*40)
# print(help(date.weekday))

# from datetime import time
# # (hh:mm:ss.ms)
# print(time(23,12,23, 382772))
# # time(hour,minute, second)

#datetime class
from datetime import datetime

# datetime(year,month,day, hour,minute,second,microsecond)

newdate=datetime(2021,10,28,10,33,23,54334)
# print(newdate)
# print("YEAR:",newdate.year)
# print("MONTH:",newdate.month)
# print("DAY:",newdate.day)
# print("HOUR:",newdate.hour)
# print("MINUTES:",newdate.minute)
# print("SECONDS:",newdate.second)
# print("MICROSECONDS:",newdate.microsecond) 

# print(newdate.date())
# print(newdate.time())

dt1=datetime(2021,10,28,10,33,23,54334)
# print(dt1)

# dt2=datetime(2022,3,10)
# diff=dt2 -dt1
# print(type(diff))
# print(diff)


# TIMEDELTA
# ============
#returns difference between 2 date object. Comparing date objects
# Mathematical operations includes add, subtract, unary (plus, minus), dt/int etc
from datetime import timedelta,date


# timedelta(days, seconds, microseconds, milliseconds, minutes,hours,weeks)
# timed=timedelta(weeks=2, days=10, hours=2)
# print(timed)

# diff=dt1+timed
# print(dt1,'------',diff)

# print(dt1)
# dt1-=timedelta(days=10)
# print(dt1)

# print(dt1.date(),'---------',dt1-timedelta(days=10)*2,'------')

#COMPARISM
dt2=datetime(2022,2,23)
dt3=datetime(2022,2,10)

# datetime +/- timedelta #returns datetime
# datetime-datetime  # returns timedate

# if (dt2 > dt3 + timedelta(days=15) ):
#     print('DT2 won')
# else:
#     print('DT3 won')

# result=dt2-timedelta(days=10)    
# print(result, type(result))

# result=dt2-dt3    
# print(result, type(result))

# Exercise -- Return the age(year, months, days)  from today
# ===========================================PRINT AGE PROGRAM====================
from datetime import datetime,date 

today= date.today()
datestr=input("Enter Your Date of Birth: YYYY/MM/DD  ")
# datestr="1909/02/03"

# Method one
# dob_= list(map(int, datestr.split('/')))
# print(datestr.split('/'))  #returns ['1909', '02', '03']
# print(dob_)   #returns [1909, 2, 3]
# print(*dob_) # return 1909 2 3

#Method 2
# dob_=[ int(val) for val in datestr.split('/')]


# dob=date(*dob_)   #from date([1909,02,03])  to date(1909,02,03)

#method 3
dob=(datetime.strptime(datestr,"%Y/%m/%d")).date()

print("Today's Date:", today)
print("Date of Birth:", dob)

total_days=(today - dob).days

print('Total Days:', total_days)

years= total_days // 365 
months=(total_days-years*365)//30
#Calculate dates
days=total_days-years*365 - months*30

print('Years:', years,', Months:', months, ', Days:', days)












# print("Date unformatted", dt2)
# date1f=dt2.strftime("%a %d, %Y ")
# print("Date Formatted", date1f)

# newdt=datetime(2021,10,28,10,33,23,54334)
# print(newdt)
# newdtf=newdt.strftime("%b %d, %Y @ the %Hth Hour, %Mrd Minute)")
# print(newdtf)

# str1="2021 09 06"
# date11=datetime.strptime(str1,"%Y %m %d")
# print(date11)
# print(type(date11))




 


 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 

# print("="*30)

# TIME
# from datetime import time 
# time1=time()
# print("default time:",time1)
# time2= time(23,43,23)
# print("Time 2:",time2)
# time3= time(7,19,17)
# print("time 3:",time3)

# time4= time(3,30,35,654334)
# print("time 3:",time4)


# print("="*30)
#DATETIME 
# from datetime import datetime
# newdate=datetime(2021,10,28,10,33,23,54334)
# print(newdate)
# print("Year:", newdate.year)
# print("month:", newdate.month)
# print("day:", newdate.day)
# print("hour:", newdate.hour)
# print("minute:", newdate.minute)
# print("second:", newdate.second) 
# print("microsecond:", newdate.microsecond) 


#TIMEDELTA
# date1=date(2020,10,23)
# date2=date(2021,9,12)
# datediff1 =date1 - date2 


# print("({}) -  ({}) => {}".format(date1,date2,datediff1))
# print(type(datediff1))
# print("date1-date2 in secs:",datediff1.total_seconds())

# #Negative Timedelta

# from datetime import timedelta

# td1=timedelta(seconds=14)
# td2=timedelta(seconds=35)
# td3= td1- td2
# print("Time Diff:",td3)
# print("Time Diff:",abs(td3))
 
# newtd=timedelta(2021,10,28,10,33,23,54334)
# print("New Time Delta:",newtd)

# # DATE FORMAT 
# #STRFTIME  ==
# print("="*30)
# newdt=datetime(2021,10,28,10,33,23,54334)
# print(newdt)
# print("Format:",newdt.strftime("%b %d %Y %H:%M:%S"))

# print( newdt.strftime("%b/%d/%Y")) # returns  Oct/28/2021

# print( newdt.strftime("%A, %b-%d, %Y")) # returns Thursday, Oct-28, 2021
# kk=newdt.strftime("%A, %b-%d, %Y")


# print("="*30)
# #STRPTIME  -- convert string to date
# # strptime(string,format)
# str='2021/09/06'
# date11=datetime.strptime(str,"%Y/%m/%d")
# print("Datetime strptime:",date11)