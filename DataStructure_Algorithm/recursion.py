# def sum(n):
#     if n==0:
#         return 0
#     else:
         
#         return n+sum(n-1)

# print(sum(5)) 

def grid_path(n,m):
    if n==1 and m==1:
        return 1
    else:
        return grid_path(n,m-1)+ grid_path(n-1,m)

print(grid_path(3,3))