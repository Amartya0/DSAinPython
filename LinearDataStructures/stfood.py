for _ in range(int(input())):
    a=[]
    maxprice=0
    for i in range(int(input())):
        a.append(list(map(int,input().split())))
    for i in range(len(a)):
        temp=((a[i][1]//(a[i][0]+1)))*a[i][2]
        if temp > maxprice:
            maxprice=temp
    print(maxprice)

