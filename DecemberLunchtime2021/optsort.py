def ifsorted(lst,n):
    for i in range(n-1):
        if lst[i+1]<lst[i]:
            return False
    return True

for _ in range(int(input())):
    n= int(input())
    arr=list(map(int,input().split()))
    if ifsorted(arr,n):
        print(0)
    else:
        print(max(arr)-min(arr))