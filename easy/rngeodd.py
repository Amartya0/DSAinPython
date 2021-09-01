L,R = map(int,input().split())
if L%2==0:
    L=L+1
for i in range(L,R+1,2):
    print(i,end=" ")