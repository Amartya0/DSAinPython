def nth(Num,n):
    c=0
    while(c<n):
        Num+=1
        for i in range(2,Num+1):
            if(Num%i==0):
                break
        if(i==Num):
            n=n+1
    return Num


def main():
    a=int(input().split())
    Num=a[0]
    n=a[1]
    print(nth(Num,n))
    
main()