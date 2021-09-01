M=int(input())
for i in range(1,M+1):
    if i%2==0:
        for j in range(5*i,5*(i-1),-1):
            print(j,end=' ')
        print("")
    else:
        for j in range(5*(i-1)+1,5*i+1):
            print(j,end=' ')
        print("")


#alternative
#M=int(input())
#N=5*M
#i=1
#while(i<N+1):
#    print(i,end=" ")
#    if i%5==0:
#        print("")
#        if i%10!=0 and i<N:
#            for j in range(i+5,i,-1):
#                print(j,end=" ")
#            print("")
#            i+=5
#    i+=1