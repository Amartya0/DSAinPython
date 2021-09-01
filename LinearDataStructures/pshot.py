def golecount(a):
    count = 0
    for i in range(len(a)):
        if a[i] == 1:
            count += 1
    return count

for _ in range(int(input())):
    n=int(input())
    s=int(input())
    a,b=[],[]
    i=1
    revs=0
    while(s>0):
        revs=revs*10+s%10
        s=s//10
    while(revs>0):
        if i%2!=0:
            a.append(revs%10)
        else:
            b.append(revs%10)
            if golecount(a)-golecount(b)>2*n-i:
                print(i-1)
                break
        revs=revs//10
        i+=1

    
    

