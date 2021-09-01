a=[]
b=[]
for _ in range(int(input())):
    a.append(int(input()))
a=sorted(a)
for i in range(len(a)):
    b.append(a[i]*(len(a)-i))
print(max(b))