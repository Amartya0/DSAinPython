for _ in range(int(input())):
    K,I0,I1=map(int,input().split())
    I2=((I0%10)+(I1%10))%10
    sum=I0
    if K==2:
        sum+=I1
    elif K==3:
        sum+=I1+I2
    elif K>3:
        sum+=I1+I2
        if I2%5!=0:
            sum+=(20*((K-3)//4))
        fac=(K-3)%4
        for j in range(fac):
            I2=((I2*2)%10)
            sum+=I2
    if sum%3==0:
        print("YES")
    else:
        print("NO")
