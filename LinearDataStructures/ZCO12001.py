m=int(input())
n=list(map(int,input().split()))
arr=[]
count,maxseq,pos_maxseq,cur_depth,depth,fpos=0,0,0,0,0,0
for i in range(0,m):
    if n[i]==2 and len(arr)==0:
        break
    if n[i]==1:
        arr.append(n[i])
    elif len(arr)!=0:
        arr.pop()
        count+=2
        if len(arr)>cur_depth:
            cur_depth=len(arr)+1
    if len(arr)==0:
        if cur_depth>depth:
            depth=cur_depth
            fpos=i-depth
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