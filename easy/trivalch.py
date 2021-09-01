A,B,C=map(int, sorted(list(map(int,input().split()))))
if C<A+B:
    print('YES')
else:
    print('NO')