def get_max(arr,n,count=0):
    if n==1:
        return count + arr[0]
    elif n==0:
        return count
    temp = arr[0]
    flag=0
    for i in range(0,n):            
        if arr[i] < temp:
            temp = arr[i]
            flag=i
    
    count+=temp*(n-flag) + get_max(arr[:flag], flag, count)
    return count
    

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(get_max(arr,n))