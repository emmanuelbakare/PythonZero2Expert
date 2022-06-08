# PROBLEM
# Given an array of integers (positive and negative) find the largest
# continous sum 
# e.g 
# largest_cont_sum([1,2,-1,3,4,10,10,-10,-1])
# result = 29
def largest_cont_sum(lst):
    if len(lst) ==0:
        return 0
    current_sum=max_sum=lst[0]
    for num in lst[1:]:
        current_sum=max(current_sum+num, num)
        max_sum=max(current_sum,max_sum)
    return max_sum


lst=[1,2,-4,3,4,10,10,-10,-1]
print(largest_cont_sum(lst))