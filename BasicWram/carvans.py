for _ in range(int(input())):
    m=int(input())
    temptop=0
    count=0
    a=list((map(int,input().split())))
    for i in range(m):
        speed=a[i]
        if temptop==0:
            temptop=speed
            count+=1
        elif temptop>speed:
            temptop=speed
            count+=1
        elif temptop==speed:
            count+=1
    print(count)