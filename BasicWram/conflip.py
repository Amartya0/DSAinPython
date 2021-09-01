for _ in range(int(input())):
    for G in range(int(input())):
        I,N,Q=map(int,input().split())
        h_count=0
        t_count=0
        if I==1:
            if N%2==0:
                h_count=N//2
                t_count=h_count
            else:
                h_count=N//2
                t_count=h_count+1
        else:
            if N%2==0:
                t_count=N//2
                h_count=t_count
            else:
                t_count=N//2
                h_count=t_count+1
        if Q==1:
            print(h_count)
        else:
            print(t_count)