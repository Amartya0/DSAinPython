for _ in range(int(input())):
    n = str(input())
    if n[0] == '>':
        print(0)
        continue
    else:
        arr=[]
        arr.append(n[0])
        count,fcount=0,0
        for i in range(1,len(n)):
            if n[i]=='>' and len(arr)==0:
                break
            if n[i]=='<':
                arr.append(n[i])
            elif len(arr)!=0:
                arr.pop()
                count+=2
            if len(arr)==0:
                fcount+=count
                count=0
    print(fcount)