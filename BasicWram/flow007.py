for _ in range(int(input())):
    n = int(input())
    rev_n=0
    while(n>0):
        rev_n=10*rev_n+n%10
        n//=10
    print(rev_n)