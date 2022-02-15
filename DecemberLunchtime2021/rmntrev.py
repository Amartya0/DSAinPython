def reverse(s):
    return s[::-1]

for _ in range(int(input())):
    n,k=map(int,input().split())
    s=input()
    for i in range(k,1,-1):
        s=reverse(s[:i])+s[i:]
        
    print(s)