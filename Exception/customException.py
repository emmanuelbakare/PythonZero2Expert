# class AgeLimit(Exception):
#     pass

# class TooYoung(AgeLimit):
#     pass
# class TooOld(AgeLimit):
#     pass

# # Correct age is 18-25
# age=11

# try:
#     if age < 18:
#         raise TooYoung  
#     if age >25:
#         raise TooOld
# except TooYoung:
#     print('You are too Young for this party')
# except TooOld:
#     print('You are too OLD for this party')
# else:
#     print('Welcome in ')
# finally:
#     print('Have a great day') 



# class AgeLimit(Exception):
#     def __init__(self, msg):
#         self.msg=msg
#         super().__init__(self,msg)
#     def __str__(self):
#         return f"ERROR: {self.msg}"

# class TooYoung(AgeLimit):
#     pass
# class TooOld(AgeLimit):
#     pass

# # Correct age is 18-25
# age=110

# try:
#     if age < 18:
#         raise TooYoung('You are too Young')  
#     if age >25:
#         raise TooOld('You are too OLD')
# except TooYoung as msg:
#     print(msg)
# except TooOld as msg:
#     print(msg)
# else:
#     print('Welcome in ')
# finally:
#     print('Have a great day') 

#Raise Exception 
import datetime
class AgeLimit(Exception):
    def __init__(self, msg):
        super().__init__(self,msg)
        self.msg=msg
        try:
            with open('log.txt','a') as file:
                file.write(f'\n{datetime.datetime.now()} \t - {msg}')
        except FileNotFoundError: 
            print('issues writing to the log file')
                
        
    def __str__(self):
        return f'Error Message:{self.msg}'

class TooYoung(AgeLimit):
    pass
class TooOld(AgeLimit):
    pass 

try:
    # age=int(input("Enter Your Age: "))
    age=23
    # age limit 18 -25
    if age < 18: 
        raise TooYoung("You are too YOUNG")
    if age > 25:
        raise TooOld("You are too OLD")
except (TooYoung, TooOld) as errorMsg:
    print(errorMsg)
else:
    print("You are Qualified: Come in")