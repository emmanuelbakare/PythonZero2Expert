
#IF Command
# if 40 <130:
#     print('That is true')
# else:
#     print('That is not true')

  


# product ="This production is good"
# if 'bad' in product:
#     print(" This product is good, go ahead and purchase")
# else:
#     print("I cant guarantee")
    


 
#IF STATEMENT EXAMPLE
# firstname =input("Enter your Firstname: ")
# lastname = input("Enter your Lastname: ")
# age= int(input("Enter your age: "))

# if age >= 18:
#     print("Welcome {0} {1}".format(firstname, lastname))
# else:
#     print("Sorry {0} {1} we dont take under age, come back in {2} years time".format(firstname, lastname, 18-age))











# # #if EXAMPLE
# balance=4000
# withdrawal = int(input("How much are you withdrawing: "))

# if withdrawal < balance:
#     print("You current balance is {}".format(balance - withdrawal) )
# else:
#     print("You have withdraw more than {} you have with us ".format(balance))

 

#ELIF EXAMPLE
age=int(input("How old are you: "))

if age>0 and age<13:
    print("You are just starting")
elif age>13 and age<20:
    print("You are a teenager")
elif age>19 and age<45:
    print(" You are a grown adult")
elif age>45 and age<60:
    print("You are so getting old")
elif age>60:
    print("You are a senior citizen: You are old")
else:
    print("We cannot process you - are you an alien?")


 