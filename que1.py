def fact(n):
    f=1
    while(n>=1):
        f=f*n
        n = n-1
    return f

def combi(n, r):
    return(int(fact(n)/fact(n-r)/fact(r)))

def printpascal(line):
    line = line+1
    for i in range(1,line):
        r=0
        for j in range(1,line):
            if(j>=line-i) and (j<=line-2+i):
                print(combi(i-1,r), end=' ')
                r+=1
            else:
                print('', end=' ')
        print('')

printpascal(5)
