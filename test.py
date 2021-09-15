for _ in range(int(input())):
    n = str(input())
    if n[0] == '2':
        print(0)
        continue
    else:
        arr=[]
        arr.append(n[0])
        count,maxseq,pos_maxseq,depth,fpos=0,0,0,1,0
        for i in range(1,len(n)):
            if n[i]=='2' and len(arr)==0:
                break
            if n[i]=='1':
                arr.append(n[i])
            elif len(arr)!=0:
                arr.pop()
                count+=2
            if len(arr)==0:
                if count>maxseq:
                    maxseq=count
                    count=0
                    pos_maxseq=i-maxseq+2
                else:
                    count=0
            if len(arr)>depth:
                depth=len(arr)
                fpos=i+1 
    print(depth,fpos,maxseq,pos_maxseq)



    
        






