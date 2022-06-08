


#ELSE AND FINALLY  EXAMPLE 1
try:
    w=12
    x=10/10
    y=open('file1.txt')
    z=10
except ZeroDivisionError:
    print('Cannot divide by Zero')
except FileNotFoundError:
    print('The file is not found')
except :
    print('Error Occurred')
else: 
    print('Program sucessfull') 
    print(y.read())
    y.close()
finally:
    print("End of program")
