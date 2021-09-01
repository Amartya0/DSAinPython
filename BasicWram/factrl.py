for _ in range(int(input())):
    n = int(input())
    i=5
    count=0
    while(n//i>0):
        count+=n//i
        i*=5
    print(count)
