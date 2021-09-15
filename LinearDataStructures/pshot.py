def gd(n):
    s= input()
    ap,bp=0,0
    ar,br=n,n
    for i in range(2*n):
        if i%2 == 0:
            ar-=1
            if s[i] == '1':
                ap+=1
        else:
            br-=1
            if s[i] == '1':
                bp+=1

        if ap> bp+br or bp> ap+ar :
            return(i+1)
    return(2*n)

for _ in range(int(input())):
    n= int(input())
    print(gd(n))
    

