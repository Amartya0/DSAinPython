for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    max1=max(arr)
    arr.remove(max1)
    max2=max(arr)
    min1=min(arr)
    if (max1-min1)*max2>(max2-min1)*max1:
        print((max1-min1)*max2)
    else:
        print((max2-min1)*max1)