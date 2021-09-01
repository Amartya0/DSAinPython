for _ in range(int(input())):
    s = input()
    l = len(s)
    if l % 2 == 0:
        s1 = sorted(list(s[:l//2]))
        s2 = sorted(list(s[l//2:]))
    else:
        s1 = sorted(list(s[:l//2]))
        s2 = sorted(list(s[l//2+1:]))
    if s1 == s2:
        print("YES")
    else:
        print("NO")