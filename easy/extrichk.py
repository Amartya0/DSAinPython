A,B,C=map(int, sorted(list(map(int,input().split()))))
if C<A+B:
    if C==A:
        print('1')
    elif (C==B and C!=A) or (B==A and B!=C):
        print('2')
    else:
        print('3')
else:
    print('-1')