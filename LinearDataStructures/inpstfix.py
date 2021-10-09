def infixtopostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opstack = []
    postfixlist = []
    tokenlist = list(infixexpr)
    for token in tokenlist:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            postfixlist.append(token)
        elif token == '(':
            opstack.append(token)
        elif token == ')':
            try:
                topToken = opstack.pop()
                while topToken != '(':
                    postfixlist.append(topToken)
                    topToken = opstack.pop()
            except:
                return ''
        else:
            while (not len(opstack) == 0) and (prec[opstack[-1]] >= prec[token]):
                postfixlist.append(opstack.pop())
            opstack.append(token)
    while not len(opstack) == 0:
        postfixlist.append(opstack.pop())      
    return ''.join(postfixlist)

for _ in range(int(input())):
    m=int(input())
    exp=input()
    exp = exp.replace(' ', '')
    print(infixtopostfix(exp))