# x = 20
# y = 50 // 3
# print(y)

# 1. ARITHMETIC OPERATORS
# ========================
#   + addition
#   -  Subtraction
#   *  Multiplication
#   / Division
#   % Modulus
#   ** Exponent
#-  // floor division


# 2. Comparison/Relational Operators
#       ==  equals 
# -     != not equal
#       <> not equal
#       > greater than
#       < lesser than
#       <= lesser than or equals to
#       >= greater than or equals to

from typing import Sequence


x=10
y=20
z=30
k=10

# print(x < y) 
# print(x != y)



#3. Assignment Operators
# ====================
#   =  assign value from right to left  
#   += add right operand to left  
#   -= subtract right operand to left  
#   *=multiply right operand to left  
#   /= divide right operand to left
#   %= modulus right operand to left
#   **= Exponent right operand to left
#- //= Floor Divide right operand to left

x=10
y=20
z=30
k=10+48-59/20

# z=y
z /=y



# 4. Logical Operators
# =======================
#   and - all expression must be true to have true result
#   or  -  one expression must be true to have true result
#   not

#     Expr 1   | Expr 2 |   AND   |   OR
# =========================================
#     True     |  False |  False  |  True
#     False    |  True  |  False  |  True
#     True     |  True  |  True   |  True
#     False    |  False |  False  |  False
x=10
y=20
z=30

a=True
b=False
c= True

# Membership Operators 
# ====================
# test for occurence  in a Sequence

#       in 
#       not in 

# print('bad'  in  'this is a good product')

sentence='this is a good product'
search='production'

print( search in sentence)

