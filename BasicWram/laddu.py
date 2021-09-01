for _ in range(int(input())):
    A,N=map(str,input().split())
    b=[]
    A=int(A)
    for i in range(A):
        b.append(list(map(str,(input()).split())))
    count=0
    for i in range(A):
        if b[i][0]=="CONTEST_WON" :
            count+=300
            if int(b[i][1])<20:
                count+=20-int(b[i][1])
        elif b[i][0]=="TOP_CONTRIBUTOR":
            count+=300
        elif b[i][0]=="BUG_FOUND":
            count+=int(b[i][1])
        elif b[i][0]=="CONTEST_HOSTED":
            count+=50
    if N == "INDIAN":
        print(count//200)
    else:
        print(count//400)