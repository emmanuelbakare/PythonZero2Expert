arr=[12,3,1,2-6,5,-8,6]
tag= 0

def threeNumberSum(arr,targetNum):
    totalarr=len(arr)
    last=totalarr
    for num,i in enumerate(range(totalarr),1):
        point=arr[i]
        left=arr[i+1]
        right=arr[last-num]
        print(point,left,right)

threeNumberSum(arr,0)
        