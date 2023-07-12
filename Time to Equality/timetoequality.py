def timetoequality(arr): 
    sum=0
    mx=float("-inf")
    for i in arr:
        if i>mx:
            mx=i
    for i in arr:
        sum=sum+(mx-i)
    return sum
arr=list(map(int,input().split()))
print(timetoequality(arr))