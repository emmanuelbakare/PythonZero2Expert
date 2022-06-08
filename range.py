#Range is a built in function used to create a sequence of numbers.
# SYNTAX - range(start,end-1, step)
# Allows you to generate a series of numbers within a given range.
# The most common use is to create an iterable of numbers 
# and also to perform an action a specific number of times
# result=list(range(0,51,10)) #(start + end)/step   - upper limit
# print(result)

# result=list(range(0,30,5))
# print(result)
# Operations it can implements include in, 
# not in, [],[x:y:z],len,min,max.range.index(), range.count()

# val=range(0,30,5)

# print(len(val))

# for i in range(10,100,10):
#     print(i)

for i in range(2,13):
    print('*'*22)
    print(f'{i} MULTIPLICATION TABLE')
    print('*'*22)
    for x in range (1,13):
        print(f'{i} x {x} = {i*x}')
    print()