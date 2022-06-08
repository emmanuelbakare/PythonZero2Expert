# PROBLEM
# Given an integer  array, output all the unique pair that sums up to a value k 
# def pair_sum(arr,sum_total)
# so output pair_sum([1,3,2,2],4) 
# returns 2 pairs = [1,3] and [2,2]

def pair_sum(arr,sum_total):
    result=set()
    for num in arr:
        diff=sum_total - num
        if diff in arr:
            paired=(num, diff)
            result.add((min(paired), max(paired)))
    
    # return '\n'.join(map(str,list(result)))
    return [len(result),result]
    
lst=[1,3,2,2,5,3,-5,1]   
print(pair_sum(lst,4)) 